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
MAX_SPEED = 100
MAX_DRIVE_MOTOR = 1000
MAX_BELT_MOTOR = 1000

LEFT = 0
RIGHT = 640
BOTTOM = 0
TOP = 400


class motor_action(Node):
  def __init__(self):

    
    super().__init__('motor_action')
    self.ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
    self.ser.reset_input_buffer()
    print("Arduino set up")

    self.move_sub = self.create_subscription(Float32MultiArray, 'impeler_move', self.move_motors, 10)
    self.belt_sub = self.create_subscription(Float32, 'belt_move', self.move_belt, 10)
    
  def move_motors(self, speeds):
    left_speed = int(speeds.data[0])
    right_speed = int(speeds.data[1])

    print("the speed to send the motors, (left, right) is (" + str(left_speed) +", "  + str(right_speed) + ")")
    self.run_nav_motors(left_speed, right_speed)

    #once we have these speeds, send the propper signals to the outputs
  

  def move_belt(self, speed):
    print("the speed to send the belt is" + str(speed))
    self.run_belt_motor(int(speed.data))

    # send the propper signals to the outputs

  #TODO: Given left and right motor speeds, send signals to the Arduino to send it that speed
  def run_nav_motors(self, left, right):
    
    print("left_motor_percent = " + str(left))
    print("right_motor_percent = " + str(right))


    if len(str(left)) == 1:
      left_buf = "0"
    else:
      left_buf = ""

    if len(str(right)) == 1:
      right_buf = "0"
    else:
      right_buf = ""


    # 1 means motor controls!
    message = int(str(1) + left_buf + str(left) + right_buf +str(right))
    print("the message is " + str(message))


    # send the write bye array and then the left byte array. Always in that order!!! 
    self.ser.write(message.to_bytes(2, byteorder='big'))
    print("just sent the right array to the arduino!")
  
  def run_belt_motor(self, speed):

    if len(str(speed)) == 1:
      add_buf = "0"
    else:
      add_buf = ""

    message = int(str(2) + '0' + '0' + add_buf + str(speed))
    print("the message is " + str(message))
    self.ser.write(message.to_bytes(2, byteorder='big'))
    print("just sent the belt control to the ARDUINO")



def main(args=None):
  rclpy.init(args=args)
  motor = motor_action()
  rclpy.spin(motor)
  motor.destroy_node()
  rclpy.shutdown
         
if __name__ == '__main__':
  main()
