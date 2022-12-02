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

class CamPub(Node):
  def __init__(self):

    
    super().__init__('camera')
    self.sub = self.create_subscription(Point, 'destination_coords', self.get_speeds, 10)
    self.pub_move = self.create_publisher(Float32MultiArray, 'impeler_move', 10)
    self.pub_belt = self.create_publisher(Float32, 'belt_move', 10)
  


    
  def get_speeds(self, point):

    print("time to process the point ("+ str(point.x) + ", " + str(point.y) + ", " + str(point.z) + ")")

    left, right = self.find_speed(point)

    #jumk data Float32MultiArray; probably better to replace with custom message type
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

    #Junk Float32 to detrmine if we should move the belt motor
    belt_speed = Float32()

    #calculation done here
    belt_speed.data = 0.5

    # publish belt stuff
    self.pub_belt.publish(belt_speed)

  #TODO; function takes in a point and rturns left anf right speed to get to trash
  def find_speed(self, point):
    #Junk data
    return float(12), float(14)



  
    


    





def main(args=None):
   rclpy.init(args=args)
   publisher = CamPub()
   rclpy.spin(publisher)
   publisher.destroy_node()
   rclpy.shutdown

         
if __name__ == '__main__':
    main()