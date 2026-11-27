#!/usr/bin/env python3

import sys
import shutil
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from dofbot_interfaces.action import AgentPrompt
from dofbot_interfaces.srv import ClearSession


class DofbotAgentClient(Node):
    def __init__(self, session_id: str = 'user_1'):
        super().__init__('dofbot_agent_client')
        self.session_id = session_id
        self._action_client = ActionClient(self, AgentPrompt, 'agent_prompt')
        self._clear_client = self.create_client(ClearSession, 'clear_session')

        # Track streaming state for single-line thinking output
        self._thinking_buffer = ""
        self._is_thinking = False

    def wait_for_servers(self):
        self.get_logger().info("Waiting for /agent_prompt action and /clear_session service...")
        self._action_client.wait_for_server()
        self._clear_client.wait_for_service()

    def _print_single_line_thinking(self, token: str):
        """Append thinking tokens and render the tail cleanly on a single terminal line."""
        # Flatten newlines so the terminal never wraps onto a new line
        clean_token = token.replace('\r', ' ').replace('\n', ' ')
        self._thinking_buffer += clean_token
        self._is_thinking = True

        term_width = shutil.get_terminal_size((80, 20)).columns
        prefix = "\033[90m[Thinking] "
        suffix = "\033[0m"
        max_text_len = max(10, term_width - 13)

        # Keep the most recent characters that fit within the terminal width
        visible_text = self._thinking_buffer[-max_text_len:]
        sys.stdout.write(f"\r\033[2K{prefix}{visible_text}{suffix}")
        sys.stdout.flush()

    def _finish_thinking_line(self):
        """Clear the temporary thinking line once reasoning finishes."""
        if self._is_thinking:
            sys.stdout.write("\r\033[2K")
            sys.stdout.flush()
            self._thinking_buffer = ""
            self._is_thinking = False

    def feedback_callback(self, feedback_msg):
        fb = feedback_msg.feedback
        if fb.thinking:
            self._print_single_line_thinking(fb.thinking)
        elif fb.status and fb.status != "Thinking...":
            self._finish_thinking_line()
            print(f"\033[36m[Status]\033[0m {fb.status}")

    def send_prompt(self, prompt: str):
        self._thinking_buffer = ""
        self._is_thinking = False

        goal_msg = AgentPrompt.Goal()
        goal_msg.prompt = prompt
        goal_msg.session_id = self.session_id

        send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        rclpy.spin_until_future_complete(self, send_goal_future)
        goal_handle = send_goal_future.result()

        if not goal_handle.accepted:
            print("\033[31m[Error]\033[0m Goal rejected by server.")
            return

        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)
        self._finish_thinking_line()

        result = result_future.result().result
        if result.success:
            print(f"\033[32mAI:\033[0m {result.response}\n")
        else:
            print(f"\033[31m[Failed]\033[0m {result.response}\n")

    def clear_session(self):
        req = ClearSession.Request()
        req.session_id = self.session_id
        future = self._clear_client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        res = future.result()
        color = "\033[32m" if res.success else "\033[31m"
        print(f"{color}[Session]\033[0m {res.message}\n")


def init_node(args=None):
    rclpy.init(args=args)
    session_id = sys.argv[1] if len(sys.argv) > 1 else "user_1"
    client = DofbotAgentClient(session_id=session_id)
    client.wait_for_servers()

    # run as: ros2 run <your_package> dofbot_agent_client session_alpha
    print(f"\nConnected to Dofbot AI Agent (session_id='{session_id}').")
    print("Commands: '/clear' to wipe session memory, 'exit' or Ctrl+C to quit.\n")

    try:
        while rclpy.ok():
            user_input = input("You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("exit", "quit"):
                break
            if user_input.lower() == "/clear":
                client.clear_session()
                continue

            client.send_prompt(user_input)
    except (KeyboardInterrupt, EOFError):
        print()
    finally:
        client.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    init_node()
