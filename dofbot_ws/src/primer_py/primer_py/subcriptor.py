#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class SubNode(Node):
    def __init__(self):
        super().__init__('subcriber_node')
        self.subcriber_ = self.create_subscription(Int32, 
                    'publisher_topic',self.callback_function, 10)
        self.get_logger().info('Nodo publicador activo')

    def callback_function(self, msg):
        self.get_logger().info(f'Mensaje recibo {msg.data}')
        
def main(args=None):
    rclpy.init(args=args)
    node = SubNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()