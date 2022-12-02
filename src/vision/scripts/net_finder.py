#!/usr/bin/env python3
# Basics ROS program to publish real-time streaming 
# video from your built-in webcam
# Author:
# - Addison Sears-Collins
# - https://automaticaddison.com

import rclpy # Python library for ROS
from rclpy.node import Node
from geometry_msgs.msg import Point
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library

class find_net(Node):
  def __init__(self):

    
    super().__init__('net_finder')
    self.pub = self.create_publisher(Point, 'destination_coords', 10)
    self.sub = self.create_subscription(Image, 'video_frames', self.pub_coords, 10)
    
  def pub_coords(self, msg):
    point = self.perform_ai(msg)
    self.pub.publish(point)

  # TODO: takes in an image and returns the point of the object we want
  def perform_ai(self, image):
    point = Point()

    # junk data
    point.x = float(10)
    point.y = float(10)
    point.z = float(10)

    print("returning point")
    return point

def main(args=None):
   rclpy.init(args=args)
   net_node = find_net()
   rclpy.spin(net_node)
   net_node.destroy_node()
   rclpy.shutdown

         
if __name__ == '__main__':
    main()