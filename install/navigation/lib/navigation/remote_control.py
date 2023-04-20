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

#MAX_SPEED 100
THRUSTER_SPEED = 2
MOTOR_SPEED = 2

class remote_control(Node):
    def __init__(self): 
        super().__init__('remote_control')
        self.pub_move = self.create_publisher(Float32MultiArray, 'impeler_move', 10)
        self.pub_belt = self.create_publisher(Float32, 'belt_move', 10)
        while True:

            last_command = input()
            #send values to thruster
            if last_command == 'w':
                self.send_val(THRUSTER_SPEED, THRUSTER_SPEED)
            elif last_command  == 'a':
                self.send_val(0, THRUSTER_SPEED)
            elif last_command == 'd':
                self.send_val(THRUSTER_SPEED, 0)
            
            #Turn on Belt
            elif last_command == 't':
                start_time = time.time()
                while (time.time() - start_time) < 10:
                    self.send_val(0, 0)
                    # Do something in the loop for 10 seconds
                    self.send_to_motor(MOTOR_SPEED)
                    time.sleep(1)

                self.send_to_motor(0) #stop belt
            else:
                self.send_val(0, 0)  
                self.send_to_motor(0)  



    # send to thruster
    def send_val(self, left, right):

        data = [float(left), float(right)]
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
        print("about to PUB")
        self.pub_move.publish(float32MultiArray)

    def send_to_motor(self, val):
        
        float32 = Float32()
        float32.data = float(val)
        print("sending motor " + str(float32))
        self.pub_belt.publish(float32)


  
    
def main(args=None):
   rclpy.init(args=args)
   controller = remote_control()
   rclpy.spin(controller)
   publisher.destroy_node()
   rclpy.shutdown

         
if __name__ == '__main__':
    main()
