#!/usr/bin/env python3

import rclpy
from rclpy.node import Node 
from dofbot_interfaces.msg import Telemetry

class TelemetrySubscriptor(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.__telem_sub = self.create_subscription(
            Telemetry,
            'telemtry',
            self._on_telemy_clbk,
            10
        )
        self.get_logger().info(f"Nodo {node_name} inicializado...")

    def _on_telemy_clbk(self, tel_msg:Telemetry):
        #msg_str = f"Recibi-> [{tel_msg.status}] pos: [x={tel_msg.pos_x}, y={tel_msg.pos_y}, z={tel_msg.pos_z}]"
        msg_str = f"Recibi-> [{tel_msg.status}] pos: [x={tel_msg.arm_pose.position.x}, y={tel_msg.arm_pose.position.y}, z={tel_msg.arm_pose.position.z}]"
        self.get_logger().info(msg_str)

def init_node(args=None):
    rclpy.init(args=args)
    tel_node_sub = TelemetrySubscriptor('tel_node_sub')
    rclpy.spin(tel_node_sub)
    rclpy.shutdown()

if __name__ == "__main__":
    init_node()
