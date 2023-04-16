#!/usr/bin/env python3
# Basics ROS program to publish real-time streaming 
# video from your built-in webcam
# Author:
# - Addison Sears-Collins
# - https://automaticaddison.com
 
# Import the necessary libraries
import rclpy # Python library for ROS
from rclpy.node import Node
from geometry_msgs.msg import Point
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import MultiArrayDimension
from std_msgs.msg import MultiArrayLayout

#MAX_SPEED 100

class test_motor_action(Node):
  def __init__(self):
    
    super().__init__('test_motor_action')
    self.pub_move = self.create_publisher(Float32MultiArray, 'impeler_move', 10)
    self.pub_belt = self.create_publisher(Float32, 'belt_move', 10)

    while True:
      left = float(input("left motor test val =  "))
      right = float(input("right motor test val =  "))
      belt = float(input("motor percent val =  "))
      data = [left, right]

      multiArrayLayout = MultiArrayLayout()

      multiArrayDimension  = MultiArrayDimension()
      multiArrayDimension.label = "jump label"
      multiArrayDimension.size = 2
      multiArrayDimension.stride = 0
      list = [multiArrayDimension]

      multiArrayLayout.data_offset = 0
      multiArrayLayout.dim = list

      float32MultiArray = Float32MultiArray()
      float32MultiArray.data = data
      float32MultiArray.layout = multiArrayLayout

      #publiish motor stuff
      self.pub_move.publish(float32MultiArray)

      #make the array for the propellers
      float32 = Float32()
      float32.data = float(belt)

      self.pub_belt.publish(float32)


  
    
def main(args=None):
   rclpy.init(args=args)
   motor_test = test_motor_action()
   rclpy.spin(motor_test)
   publisher.destroy_node()
   rclpy.shutdown

         
if __name__ == '__main__':
    main()