#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import os
# Utilizamos LangChain para interatuar entre el LLM y las herrameintas
# necesarias para el agente
from langchain.tools import BaseTool, tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

class DofbotAIAgent(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.get_logger().info("Dofbot AI Agent Node initialized...")

        # Herramientas
        self.get_ros_distro_tool = tool(self.get_ros_distro)
        self.get_domain_id_tool = tool(self.get_domain_id)
        # Definimos un prompt
        self.prompt = ChatPromptTemplate({
            ("system", """You are a ROS 2 system information assistant.
            You can check ROS 2 system status using these commands:
            - get_ros_distro(): Get the current ROS distribution name
            - get_domain_id(): Get the current ROS_DOMAIN_ID
            
            Return only the necessary information and results. e.g
            Human: What ROS distribution am I using?
            AI: Current ROS distribution: humble
            Human: What is my ROS domain ID?
            AI: Current ROS domain ID: 0
            """),
            MessagesPlaceholder('chat_history', optional=True),
            ("human", "{input}"),
            MessagesPlaceholder("agent_scratchpad"),
        })
        

    def get_ros_distro(self) -> str:
        """Obtiene la version de ROS utilizada"""
        ros_distro = os.environ.get('ROS_DISTRO')
        try:
            if (ros_distro):
                return f"Distribución actual de ROS: {ros_distro}"
            else:
                return f"La variable de entorno ROS_DISTRO no existe"
        except Exception as e:
            return f"Error getting ROS distribution: {str(e)}"        

    def get_domain_id(self) -> str:
        """Obtiene ROS2 Domain ID"""
        try:
            # Si no existe ROS_DOMAIN_ID, el valor por default es 0
            domain_id = os.environ.get('ROS_DOMAIN_ID', '0') 
            return f"El ID del dominio actual de ROS2 es: {domain_id}"
        except Exception as e:
            return f"Error getting ROS Domain ID: {str(e)}"        


def main():
    print('Hi from dofbot_agent.')


if __name__ == '__main__':
    main()
