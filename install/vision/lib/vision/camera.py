#!/usr/bin/env python3
# Basics ROS program to publish real-time streaming 
# video from your built-in webcam
# Author:
# - Addison Sears-Collins
# - https://automaticaddison.com
 
# Import the necessary libraries
import rclpy # Python library for ROS
from rclpy.node import Node
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library

class CamPub(Node):
  def __init__(self):

    
    super().__init__('camera')
    self.pub = self.create_publisher(Image, 'video_frames', 10)
    timer_period = 0.5  # seconds
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0

    
  def timer_callback(self):
    cap = cv2.VideoCapture(2)
     # Used to convert between ROS and OpenCV images
    br = CvBridge()
    counter = 0
    while counter < 50:
      ret, frame = cap.read()
      counter = counter + 1
    if ret == True:
        # Print debugging information to the terminal
        # Publish the image.
        # The 'cv2_to_imgmsg' method converts an OpenCV
        # image to a ROS image message
        print("sending over image")
        self.pub.publish(br.cv2_to_imgmsg(frame))

def main(args=None):
   rclpy.init(args=args)
   publisher = CamPub()
   rclpy.spin(publisher)
   publisher.destroy_node()
   rclpy.shutdown

         
if __name__ == '__main__':
    main()
