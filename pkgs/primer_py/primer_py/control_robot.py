#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
import time

class ControlNode(Node):
    def __init__(self):
            super().__init__('control_robot_node')
            self.cmd_vel_pub_ = self.create_publisher(
                 Twist,'/cmd_vel',10)
            self.joint_0_pub_ = self.create_publisher(
                 Float64,'/joint0/cmd_pos',10)
            self.joint_1_pub_ = self.create_publisher(
                 Float64,'/joint1/cmd_pos',10)
            self.get_logger().info("Nodo control iniciado")
            self.timer_ = self.create_timer(
                 1.0,self.callback_control )


    def callback_control(self):
       # Definicion de mesajes
       movil_msg_control = Twist()
       joint0_msg_control = Float64()
       joint1_msg_control = Float64()


        # Primera acción
       # Velocidad lineal 
       movil_msg_control.linear.x = 0.1
       movil_msg_control.linear.y = 0.0
       movil_msg_control.linear.z = 0.0
        # velocidad angular
       movil_msg_control.angular.x = 0.0
       movil_msg_control.angular.y = 0.0
       movil_msg_control.angular.z = 0.05
       # postura del brazo
       joint0_msg_control.data = float(0.0)
       joint1_msg_control.data = float(1.57)

       self.cmd_vel_pub_.publish(movil_msg_control)
       self.joint_0_pub_.publish(joint0_msg_control)
       self.joint_1_pub_.publish(joint1_msg_control)
       # timer 1
       time.sleep(1.5)
       self.get_logger().info("Primera acción terminada")

       
        # Segunda acción
       # Velocidad lineal 
       movil_msg_control.linear.x = 0.0
       movil_msg_control.linear.y = 0.0
       movil_msg_control.linear.z = 0.0
        # velocidad angular
       movil_msg_control.angular.x = 0.0
       movil_msg_control.angular.y = 0.0
       movil_msg_control.angular.z = 0.0
       # postura del brazo
       joint0_msg_control.data = float(1.57)
       joint1_msg_control.data = float(1.57)
       # publicacion
       self.cmd_vel_pub_.publish(movil_msg_control)
       self.joint_0_pub_.publish(joint0_msg_control)
       self.joint_1_pub_.publish(joint1_msg_control)
       self.get_logger().info("Segunda acción terminada")
       # timer 2
       time.sleep(1.5)
       
     
def main(args=None):
     rclpy.init(args=args)
     node = ControlNode()
     rclpy.spin(node)
     rclpy.shutdown()

if __name__=='__main__':
     main()




            






