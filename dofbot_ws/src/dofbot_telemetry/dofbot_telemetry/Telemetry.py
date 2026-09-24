#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from dofbot_interfaces.msg import Telemetry

class TelemetryNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.__telem_pub = self.create_publisher(Telemetry,'telemtry',10)
        self._telem_timer = self.create_timer(1.0, self._on_telem_clk)
        self.get_logger().info(f"[{node_name}] inicializado")

    def _on_telem_clk(self):
        telemetry_msg = Telemetry()
        #telemetry_msg.status = 'ACTIVE'
        #telemetry_msg.pos_x = 0.0
        #telemetry_msg.pos_y = 0.0
        #telemetry_msg.pos_z = 0.0

        telemetry_msg.status = "Active"
        telemetry_msg.arm_pose.position.x = 0.0
        telemetry_msg.arm_pose.position.y = 0.0
        telemetry_msg.arm_pose.position.z = 0.0

        telemetry_msg.arm_pose.orientation.w = 1.0
        telemetry_msg.arm_pose.orientation.x = -1.0
        telemetry_msg.arm_pose.orientation.y = -1.0
        telemetry_msg.arm_pose.orientation.z = -1.0

        self.__telem_pub.publish(telemetry_msg)

def init_node(args=None):
    rclpy.init(args=args)
    telemetry_node = TelemetryNode("telem_node")
    rclpy.spin(telemetry_node)
    rclpy.shutdown()

if __name__ == '__main__':
    init_node()