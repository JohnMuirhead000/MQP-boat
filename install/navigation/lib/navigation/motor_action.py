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
import serial

class motor_action(Node):
  def __init__(self):

    
    super().__init__('motor_action')
    self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    self.ser.reset_input_buffer()
    self.move_sub = self.create_subscription(Float32MultiArray, 'impeler_move', self.move_motors, 10)
    self.belt_sub = self.create_subscription(Float32, 'belt_move', self.move_belt, 10)
    
  def move_motors(self, speeds):
    left_speed = speeds.data[0]
    right_speed = speeds.data[1]
    print("the speed to send the motors, (left, right) is (" + str(left_speed) +", "  + str(right_speed) + ")")
    self.run_nav_motors(left_speed, right_speed)

    #once we have these speeds, send the propper signals to the outputs
  

  def move_belt(self, speed):
    print("the speed to send the belt is" + str(speed))
    self.run_belt_motor(speed)

    # send the propper signals to the outputs

  #TODO: Given left and right motor speeds, send signals to the Arduino to send it that speed
  def run_nav_motors(self, left, right):
    print("Need to implement 'run_nav_motors'")
    self.ser.write(b"L"+str(left) + " R" + str(right))
  
  #TODO: Given belt motor speed, send signals to the Arduino to send it that speed
  def run_belt_motor(self, speed):
    print("Need to implement 'run_belt_motor'")
    self.ser.write(b"B"+str(speed))
  




def main(args=None):
   rclpy.init(args=args)
   motor = motor_action()
   rclpy.spin(motor)
   motor.destroy_node()
   rclpy.shutdown

         
if __name__ == '__main__':
  main()
