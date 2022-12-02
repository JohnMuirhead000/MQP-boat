#!/usr/bin/env python3
# Basics ROS program to publish real-time streaming 
# video from your built-in webcam
# Author:
# - Addison Sears-Collins
# - https://automaticaddison.com

import rclpy # Python library for ROS
from rclpy.node import Node
from geometry_msgs.msg import Point
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import MultiArrayDimension
from std_msgs.msg import MultiArrayLayout

class motor_action(Node):
  def __init__(self):

    
    super().__init__('motor_action')
    self.move_sub = self.create_subscription(Float32MultiArray, 'impeler_move', self.move_motors, 10)
    self.belt_sub = self.create_subscription(Float32, 'belt_move', self.move_belt, 10)
    
  def move_motors(self, speeds):
    left_speed = speeds.data[0]
    right_speed = speeds.data[1]
    print("the speed to send the motors, (left, right) is (" + str(left_speed) +", "  + str(right_speed) + ")")

    #once we have these speeds, send the propper signals to the outputs
  

  def move_belt(self, speed):
    print("the speed to send the belt is" + str(speed))

    # send the propper signals to the outputs




def main(args=None):
   rclpy.init(args=args)
   motor = motor_action()
   rclpy.spin(motor)
   motor.destroy_node()
   rclpy.shutdown

         
if __name__ == '__main__':
  main()
