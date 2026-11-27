#!/usr/bin/env python3

import os
import subprocess
import re 

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

from langchain.tools import tool
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_nvidia_ai_endpoints import ChatNVIDIA

from dofbot_interfaces.action import AgentPrompt
from dofbot_interfaces.srv import ClearSession

def _run_ros2_cli(args: list[str], label: str) -> str:
    """Helper to execute a ros2 CLI introspection command safely."""
    try:
        result = subprocess.run(
            ['ros2', *args],
            capture_output=True,
            text=True,
            check=True,
            timeout=5.0,
        )
        output = result.stdout.strip()
        if not output:
            return f"No {label} found."
        return f"Available ROS 2 {label}:\n{output}"
    except subprocess.TimeoutExpired:
        return f"Error listing {label}: ros2 CLI command timed out."
    except subprocess.CalledProcessError as e:
        err = e.stderr.strip() if e.stderr else str(e)
        return f"Error listing {label}: {err}"
    except Exception as e:
        return f"Error listing {label}: {str(e)}"

def _is_valid_ros_name(name: str) -> bool:
    """Validate that a ROS 2 identifier (package, topic, node, service) contains safe characters."""
    return bool(name and not name.startswith('-') and re.match(r'^[a-zA-Z0-9_/~]+$', name))

@tool
def get_ros_distro() -> str:
    """Get the current ROS 2 distribution name from the ROS_DISTRO environment variable."""
    ros_distro = os.environ.get('ROS_DISTRO')
    if ros_distro:
        return f"Current ROS distribution: {ros_distro}"
    return "The ROS_DISTRO environment variable is not set."


@tool
def get_domain_id() -> str:
    """Get the current ROS_DOMAIN_ID. Defaults to 0 if not set."""
    domain_id = os.environ.get('ROS_DOMAIN_ID', '0')
    return f"Current ROS domain ID: {domain_id}"

@tool
def list_topics() -> str:
    """List all available ROS 2 topics currently active in the system."""
    return _run_ros2_cli(['topic', 'list'], 'topics')


@tool
def list_nodes() -> str:
    """List all running ROS 2 nodes currently active in the system."""
    return _run_ros2_cli(['node', 'list'], 'nodes')

@tool
def list_services() -> str:
    """List all available ROS 2 services currently active in the system."""
    return _run_ros2_cli(['service', 'list'], 'services')

@tool
def list_actions() -> str:
    """List all available ROS 2 actions currently active in the system."""
    return _run_ros2_cli(['action', 'list'], 'actions')

@tool
def list_dofbot_packages() -> str:
    """List all installed ROS 2 packages related to Dofbot (matching 'dofbot')."""
    try:
        result = subprocess.run(
            ['ros2', 'pkg', 'list'],
            capture_output=True,
            text=True,
            check=True,
            timeout=5.0,
        )
        dofbot_pkgs = [
            line.strip()
            for line in result.stdout.splitlines()
            if 'dofbot' in line.lower()
        ]
        if not dofbot_pkgs:
            return "No Dofbot ROS 2 packages found."
        return "Available Dofbot ROS 2 packages:\n" + "\n".join(dofbot_pkgs)
    except subprocess.TimeoutExpired:
        return "Error listing Dofbot packages: ros2 CLI command timed out."
    except subprocess.CalledProcessError as e:
        err = e.stderr.strip() if e.stderr else str(e)
        return f"Error listing Dofbot packages: {err}"
    except Exception as e:
        return f"Error listing Dofbot packages: {str(e)}"

@tool
def list_package_executables(package_name: str) -> str:
    """List all executables available inside a specific ROS 2 package.

    Args:
        package_name: Name of the ROS 2 package (e.g., 'dofbot_interfaces' or 'demo_nodes_cpp').
    """
    pkg = package_name.strip()
    if not _is_valid_ros_name(pkg):
        return f"Invalid package name: '{package_name}'"
    return _run_ros2_cli(['pkg', 'executables', pkg], f"executables in '{pkg}'")

@tool
def get_topic_info(topic_name: str) -> str:
    """Get detailed information about a ROS 2 topic, including message type, publisher count, and subscriber count.

    Args:
        topic_name: Full name of the ROS 2 topic (e.g., '/joint_states' or '/tf').
    """
    topic = topic_name.strip()
    if not topic.startswith('/'):
        topic = f'/{topic}'
    if not _is_valid_ros_name(topic):
        return f"Invalid topic name: '{topic_name}'"
    return _run_ros2_cli(['topic', 'info', '-v', topic], f"info for topic '{topic}'")

@tool
def get_node_info(node_name: str) -> str:
    """Get subscribers, publishers, services, and actions associated with a running ROS 2 node.

    Args:
        node_name: Full name of the running ROS 2 node (e.g., '/dofbot_ai_agent').
    """
    node = node_name.strip()
    if not node.startswith('/'):
        node = f'/{node}'
    if not _is_valid_ros_name(node):
        return f"Invalid node name: '{node_name}'"
    return _run_ros2_cli(['node', 'info', node], f"info for node '{node}'")

@tool
def get_service_type(service_name: str) -> str:
    """Get the interface type of an active ROS 2 service.

    Args:
        service_name: Full name of the ROS 2 service (e.g., '/clear_session').
    """
    srv = service_name.strip()
    if not srv.startswith('/'):
        srv = f'/{srv}'
    if not _is_valid_ros_name(srv):
        return f"Invalid service name: '{service_name}'"
    return _run_ros2_cli(['service', 'type', srv], f"type for service '{srv}'")

@tool
def show_interface_definition(interface_name: str) -> str:
    """Show the field definitions of a ROS 2 message, service, or action interface.

    Args:
        interface_name: Full interface name (e.g., 'dofbot_interfaces/action/AgentPrompt' or 'sensor_msgs/msg/JointState').
    """
    iface = interface_name.strip()
    if not _is_valid_ros_name(iface):
        return f"Invalid interface name: '{interface_name}'"
    return _run_ros2_cli(['interface', 'show', iface], f"definition for '{iface}'")
    

class DofbotAIAgent(Node):
    def __init__(self, node_name: str = 'dofbot_ai_agent'):
        super().__init__(node_name)

        self.declare_parameter('provider', 'ollama')
        # Reasoning-capable models such as DeepSeek-R1/Qwen3 on Ollama, OpenAI o-series/GPT-5, or Claude with extended thinking
        self.declare_parameter('model', 'nemotron-3.5-bolt:latest') #'gemma4:26b'
        self.declare_parameter('base_url', 'http://172.16.8.184:11434/')    # 'http://localhost:11434'
        self.declare_parameter('enable_thinking', True)
        self.declare_parameter('reasoning_budget', 2048)

        provider = self.get_parameter('provider').get_parameter_value().string_value
        model_name = self.get_parameter('model').get_parameter_value().string_value
        base_url = self.get_parameter('base_url').get_parameter_value().string_value
        enable_thinking = self.get_parameter('enable_thinking').get_parameter_value().bool_value
        reasoning_budget = self.get_parameter('reasoning_budget').get_parameter_value().integer_value

        self.llm = self._init_llm(
            provider=provider,
            model_name=model_name,
            base_url=base_url,
            enable_thinking=enable_thinking,
            reasoning_budget=reasoning_budget,
        )
        self.tools = [
            get_ros_distro,
            get_domain_id,
            list_topics,
            list_nodes,
            list_services,
            list_actions,
            list_dofbot_packages,
            list_package_executables,
            get_topic_info,
            get_node_info,
            get_service_type,
            show_interface_definition,
        ]

        system_prompt = (
            "You are a ROS 2 system information assistant. "
            "You can inspect the ROS 2 environment, packages, and active computation graph using these tools:\n"
            "- get_ros_distro: Get the current ROS distribution name\n"
            "- get_domain_id: Get the current ROS_DOMAIN_ID\n"
            "- list_topics: List all available ROS 2 topics\n"
            "- list_nodes: List all running ROS 2 nodes\n"
            "- list_services: List all available ROS 2 services\n"
            "- list_actions: List all available ROS 2 actions\n"
            "- list_dofbot_packages: List all installed Dofbot ROS 2 packages\n"
            "- list_package_executables(package_name): List executables inside a specific ROS 2 package\n"
            "- get_topic_info(topic_name): Get message type, publishers, and subscribers for a topic\n"
            "- get_node_info(node_name): Get publishers, subscribers, services, and actions for a node\n"
            "- get_service_type(service_name): Get the interface type of a ROS 2 service\n"
            "- show_interface_definition(interface_name): Show the fields of a msg, srv, or action interface\n\n"
            "Chain tools when needed (for example, list Dofbot packages first before inspecting executables). "
            "Return only the necessary information and results concisely."
        )

        # InMemorySaver stores multi-turn chat history keyed by thread_id (session_id)
        self.checkpointer = InMemorySaver()

        self.agent = create_agent(
            model=self.llm,
            tools=self.tools,
            system_prompt=system_prompt,
            checkpointer=self.checkpointer
        )

        self.callback_group = ReentrantCallbackGroup()

        self._action_server = ActionServer(
            self,
            AgentPrompt,
            'agent_prompt',
            execute_callback=self.execute_callback,
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback,
            callback_group=self.callback_group
        )

        # Service Server to wipe session memory on demand
        self._clear_session_srv = self.create_service(
            ClearSession,
            'clear_session',
            self.clear_session_callback,
            callback_group=self.callback_group
        )

        self.get_logger().info(
            f"Dofbot AI Agent ready ({provider}:{model_name}, thinking={enable_thinking}) | "
            f"Tools: {[t.name for t in self.tools]} | "
            f"Action: /agent_prompt | Service: /clear_session"
        )

    def _init_llm(self, provider: str, model_name: str, base_url: str, enable_thinking: bool, reasoning_budget: int):
        """Initialize an Ollama, OpenAI, or Anthropic model with optional reasoning extraction."""
        provider = provider.lower()

        if provider == 'ollama':
            # reasoning=True separates <think> blocks into reasoning_content on supported models
            return init_chat_model(
                model=model_name,
                model_provider='ollama',
                base_url=base_url,
                temperature=0,
                reasoning=enable_thinking
            )
        elif provider == 'openai':
            kwargs = {"reasoning_effort": "medium"} if enable_thinking else {}
            return init_chat_model(
                model=model_name,
                model_provider='openai',
                **kwargs
            )
        elif provider == 'anthropic':
            kwargs = {"thinking": {"type": "enabled", "budget_tokens": 2048}} if enable_thinking else {}
            return init_chat_model(
                model=model_name,
                model_provider='anthropic',
                **kwargs
            )
        elif provider == 'nvidia':
            nvidia_api_key = os.environ.get('NVIDIA_AI_API_KEY')
            if not nvidia_api_key:
                raise EnvironmentError(
                    "NVIDIA_AI_API_KEY environment variable is not set."
                )

            # ChatNVIDIA expects the base '/v1' URL and appends '/chat/completions' internally
            raw_url = 'https://integrate.api.nvidia.com/v1' # base_url.strip() or 'https://integrate.api.nvidia.com/v1'
            nvidia_base_url = raw_url.removesuffix('/chat/completions')

            effective_budget = reasoning_budget if enable_thinking else 0
            selected_model = model_name or 'nvidia/nemotron-3.5-super-vl-120b-a12'

            return ChatNVIDIA(
                model=selected_model,
                api_key=nvidia_api_key,
                base_url=nvidia_base_url,
                temperature=0.1,
                top_p=0.9,
                max_completion_tokens=8192,
                model_kwargs={"reasoning_budget": effective_budget},
            )
        else:
            raise ValueError(
                f"Unsupported provider '{provider}'. Use 'nvidia', 'ollama', 'openai', or 'anthropic'."
                )

    def clear_session_callback(self, request, response):
        """Wipe stored conversation checkpoints for the requested session_id."""
        session_id = request.session_id.strip() or "default"
        try:
            self.checkpointer.delete_thread(session_id)
            response.success = True
            response.message = f"Session '{session_id}' memory cleared."
            self.get_logger().info(response.message)
        except Exception as e:
            response.success = False
            response.message = f"Failed to clear session '{session_id}': {str(e)}"
            self.get_logger().error(response.message)
        return response    

    def goal_callback(self, goal_request):
        if not goal_request.prompt.strip():
            self.get_logger().warn("Rejected empty prompt goal.")
            return GoalResponse.REJECT
        session = goal_request.session_id.strip() or "default"
        self.get_logger().info(f"Accepted goal [session='{session}']: '{goal_request.prompt}'")
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        self.get_logger().info("Received cancel request for active prompt.")
        return CancelResponse.ACCEPT

    def _extract_thinking_and_text(self, token) -> tuple[str, str]:
        """Extract normalized reasoning/thinking chunks and final text chunks from an AIMessageChunk."""
        thinking_parts = []
        text_parts = []

        # 1. Check LangChain 1.x standardized content_blocks
        if hasattr(token, "content_blocks") and token.content_blocks:
            for block in token.content_blocks:
                b_type = block.get("type")
                if b_type in ("reasoning", "thinking"):
                    thinking_parts.append(block.get("reasoning") or block.get("thinking") or "")
                elif b_type == "text":
                    text_parts.append(block.get("text", ""))
        else:
            # 2. Fallback for raw string content + additional_kwargs['reasoning_content']
            if isinstance(token.content, str) and token.content:
                text_parts.append(token.content)
            extra_reasoning = getattr(token, "additional_kwargs", {}).get("reasoning_content")
            if extra_reasoning:
                thinking_parts.append(extra_reasoning)

        return "".join(thinking_parts), "".join(text_parts)

    def execute_callback(self, goal_handle):
        feedback_msg = AgentPrompt.Feedback()
        result = AgentPrompt.Result()

        # Fall back to 'default' if the client leaves session_id empty
        session_id = goal_handle.request.session_id.strip() or "default"
        config = {"configurable": {"thread_id": session_id}}

        feedback_msg.status = f"Processing prompt in session '{session_id}'..."
        feedback_msg.thinking = ""
        goal_handle.publish_feedback(feedback_msg)

        final_reply_chunks = []

        try:
            # stream_mode="messages" yields (token, metadata) tuples in real time
            for token, metadata in self.agent.stream(
                {"messages": [{"role": "user", "content": goal_handle.request.prompt}]},
                config=config,
                stream_mode="messages"
            ):
                if goal_handle.is_cancel_requested:
                    goal_handle.canceled()
                    result.response = "Prompt execution canceled by client."
                    result.success = False
                    return result

                node_name = metadata.get("langgraph_node", "")

                # Tool execution output node
                if node_name == "tools":
                    tool_name = getattr(token, "name", "tool")
                    feedback_msg.status = f"Executed tool: {tool_name}"
                    feedback_msg.thinking = ""
                    goal_handle.publish_feedback(feedback_msg)
                    continue

                # LLM generation node
                if node_name == "model":
                    # Announce tool call requests as status feedback
                    if getattr(token, "tool_call_chunks", None):
                        for tc in token.tool_call_chunks:
                            if tc.get("name"):
                                feedback_msg.status = f"Calling tool: {tc['name']}"
                                feedback_msg.thinking = ""
                                goal_handle.publish_feedback(feedback_msg)

                    thinking_text, answer_text = self._extract_thinking_and_text(token)

                    if thinking_text:
                        feedback_msg.status = "Thinking..."
                        feedback_msg.thinking = thinking_text
                        goal_handle.publish_feedback(feedback_msg)

                    if answer_text:
                        final_reply_chunks.append(answer_text)

            final_reply = "".join(final_reply_chunks).strip()
            goal_handle.succeed()
            result.response = final_reply
            result.success = True
            self.get_logger().info(f"Goal succeeded [session='{session_id}']: {final_reply}")
            return result

        except Exception as e:
            self.get_logger().error(f"Agent execution failed: {e}")
            goal_handle.abort()
            result.response = f"Error: {str(e)}"
            result.success = False
            return result


def init_node(args=None):
    rclpy.init(args=args)
    node = DofbotAIAgent('dofbot_ai_agent')

    executor = MultiThreadedExecutor()
    executor.add_node(node)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    init_node()
