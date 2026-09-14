#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class SubcriberNode(Node):
    def __init__(self):
        super().__init__('subcriber_node')
        self.create_subscription(Int32,'publisher_topic',
                                  self.listener_callback, 10)

        self.get_logger().info("El nodo subcritor esta activo")


    def listener_callback(self, msg):

        self.get_logger().info(f'El mensaje recibido es: "{msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = SubcriberNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
