#!/usr/bin/env python3

import os
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Utilizamos LangChain para interatuar entre el LLM y las herrameintas
# necesarias para el agente
# from langchain.tools import BaseTool, tool
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import tool
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

# 1. Define tools as standalone functions using the @tool decorator
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


class DofbotAIAgent(Node):
    def __init__(self, node_name):
        super().__init__(node_name)

        # 2. Declare ROS 2 parameters to switch LLM providers at runtime
        self.declare_parameter('provider', 'ollama')   # 'ollama', 'openai', 'anthropic'
        self.declare_parameter('model', 'gemma4:26b')    # e.g., 'gemma4:26b', 'gpt-4o-mini', 'claude-sonnet-4-5'
        self.declare_parameter('base_url', 'http://172.16.8.184:11434/')    # 'http://localhost:11434'        
        provider = self.get_parameter('provider').get_parameter_value().string_value
        model_name = self.get_parameter('model').get_parameter_value().string_value
        base_url = self.get_parameter('base_url').get_parameter_value().string_value

        # 3. Initialize the chat model using LangChain 1.5's unified factory
        self.llm = self._init_llm(provider, model_name, base_url)
        self.tools = [get_ros_distro, get_domain_id]

        system_prompt = (
            "You are a ROS 2 system information assistant. "
            "You can check ROS 2 system status using these tools:\n"
            "- get_ros_distro: Get the current ROS distribution name\n"
            "- get_domain_id: Get the current ROS_DOMAIN_ID\n\n"
            "Return only the necessary information and results. e.g.\n"
            "Human: What ROS distribution am I using?\n"
            "AI: Current ROS distribution: humble\n"
            "Human: What is my ROS domain ID?\n"
            "AI: Current ROS domain ID: 0"
        )

        # 4. Create the agent graph (replaces legacy AgentExecutor)
        self.agent = create_agent(
            model=self.llm,
            tools=self.tools,
            system_prompt=system_prompt
        )

        # 5. ROS 2 Topic interface for sending prompts and receiving replies
        self.sub = self.create_subscription(String, '/agent/prompt', self.prompt_callback, 10)
        self.pub = self.create_publisher(String, '/agent/response', 10)

        self.get_logger().info(
            f"Dofbot AI Agent initialized ({provider}:{model_name}). Listening on /agent/prompt..."
        )

    def _init_llm(self, provider: str, model_name: str, base_url: str):
        """Initialize an Ollama, OpenAI (ChatGPT), or Anthropic (Claude) model."""
        provider = provider.lower()
        if provider == 'ollama':
            # Model must support native tool calling (e.g., llama3.2, llama3.1, qwen2.5)
            return init_chat_model(
                model=model_name,
                model_provider='ollama',
                base_url=base_url,
                temperature=0
            )
        elif provider == 'openai':
            # Reads OPENAI_API_KEY from environment
            return init_chat_model(
                model=model_name,
                model_provider='openai',
                temperature=0
            )
        elif provider == 'anthropic':
            # Reads ANTHROPIC_API_KEY from environment
            return init_chat_model(
                model=model_name,
                model_provider='anthropic',
                temperature=0
            )
        else:
            raise ValueError(f"Unsupported provider '{provider}'. Use 'ollama', 'openai', or 'anthropic'.")

    def query_agent(self, user_input: str) -> str:
        """Run the LangChain 1.5 agent loop and return the final assistant text."""
        try:
            result = self.agent.invoke({
                "messages": [{"role": "user", "content": user_input}]
            })
            # In LangChain 1.5+, messages may return content as a string or structured blocks
            final_msg = result["messages"][-1]
            return final_msg.text if hasattr(final_msg, "text") else str(final_msg.content)
        except Exception as e:
            self.get_logger().error(f"Agent execution failed: {e}")
            return f"Error: {str(e)}"

    def prompt_callback(self, msg: String):
        """Process incoming String messages on /agent/prompt and publish to /agent/response."""
        self.get_logger().info(f"Received query: {msg.data}")
        reply = self.query_agent(msg.data)
        self.get_logger().info(f"Agent reply: {reply}")

        response_msg = String()
        response_msg.data = reply
        self.pub.publish(response_msg)

def init_node(args=None):
    rclpy.init(args=args)
    node = DofbotAIAgent('dofbot_ai_agent')
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    init_node()
