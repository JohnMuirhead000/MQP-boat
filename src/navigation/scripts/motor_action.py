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
import struct
from struct import pack, unpack
import serial
import time
import sys

#Arduino stuff
BAUD_RATE = 9600
COM_PORT = '/dev/ttyACM0'


class motor_action(Node):
  def __init__(self):

    
    super().__init__('motor_action')
    self.ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
    self.ser.reset_input_buffer()
    print("Arduino set up")
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
    right_array = bytearray(struct.pack("f", right)) 
    left_array = bytearray(struct.pack("f", left))

    # send the write bye array and then the left byte array. Always in that order!!! 
    self.ser.write(right_array)
    self.ser.write(left_array)

    arduino_out = self.ser.readline()
    print("arduino_out = " + str(arduino_out))
  
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
