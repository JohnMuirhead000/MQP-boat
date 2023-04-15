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
import time
import msvcrt

#MAX_SPEED 100

class remote_control(Node):
  def __init__(self):
    
    super().__init__('remote_control')
    self.pub_move = self.create_publisher(Float32MultiArray, 'impeler_move', 10)
    self.pub_belt = self.create_publisher(Float32, 'belt_move', 10)

    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            print(key)
            break
    #while True:
        # if keyboard.is_pressed('a') and keyboard.is_pressed('d'):
        #     self.send_val(10, 10)
        # elif keyboard.is_pressed('a'):
        #     self.send_val(10, 0)
        # elif keyboard.is_pressed('d'):
        #     self.send_val(0, 10)
        # else:
        #     self.send_val(0, 0)

        # if keyboard.is_pressed('t'):
        #     start_time = time.time()
        #     while (time.time() - start_time) < 10:
        #         self.send_val(0, 0)
        #         # Do something in the loop for 10 seconds
        #         self.send_to_motor()
    
    def send_val(self, left, right):
        print("write to the motor subscriber")
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

    def send_to_motor(self):
        print("power the motor with 10% ")
        float32 = Float32()
        float32.data = float(10)
        self.pub_belt.publish(float32)


  
    
def main(args=None):
   rclpy.init(args=args)
   controller = remote_control()
   rclpy.spin(controller)
   publisher.destroy_node()
   rclpy.shutdown

         
if __name__ == '__main__':
    main()