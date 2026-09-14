#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class MyNodo(Node):
    def __init__(self):
        super().__init__('primer_node')
        self.count_ = 2
        self.publisher_  = self.create_publisher(Int32,'publisher_topic',10)
        self.timer_ = self.create_timer(1.0, self.callback_function)
        self.get_logger().info('Nodo publicador activo')


    def callback_function(self):
        message = Int32()
        message.data = self.count_
        self.publisher_.publish(message)

def main(args= None):
    rclpy.init(args=args)
    node = MyNodo()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()