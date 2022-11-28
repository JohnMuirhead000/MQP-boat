#!/usr/bin/env python3
# Description:
# - Subscribes to real-time streaming video from your built-in webcam.
#
# Author:
# - Addison Sears-Collins
# - https://automaticaddison.com
 
# Import the necessary libraries
import rclpy # Python library for ROS
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
from rclpy.node import Node
import cv2 # OpenCV library
 
# def callback(data):
 
#   # Used to convert between ROS and OpenCV images
#   br = CvBridge()
   
#   # Convert ROS Image message to OpenCV image
#   current_frame = br.imgmsg_to_cv2(data)
   
#   # Display image
#   cv2.imwrite("~/images")
   
#   cv2.waitKey(0)
      
# def receive_message():
 
#   # Tells rospy the name of the node.
#   # Anonymous = True makes sure the node has a unique name. Random
#   # numbers are added to the end of the name. 
#   rclpy.init()
   
#   # Node is subscribing to the video_frames topic
#   rclpy.create_subscription'video_frames', Image, callback)
 
#   # spin() simply keeps python from exiting until this node is stopped
#   rclpy.spin()
 
#   # Close down the video stream when done
#   cv2.destroyAllWindows()


class CamSub(Node):
    
  def __init__(self):

    super().__init__('camera_debug')
    self.sub = self.create_subscription(Image, 'video_frames', self.process_image,  10)
    print("building the debugger")

    
  def process_image(self, image):
  # Used to convert between ROS and OpenCV images
    br = CvBridge()
    
    # Convert ROS Image message to OpenCV image
    current_frame = br.imgmsg_to_cv2(image)
    
    # Display image
    cv2.imwrite("~/images")
    cv2.waitKey(0)
    print ("processed image")

def main(args=None):
   rclpy.init(args=args)
   publisher = CamSub()
   rclpy.spin(publisher)
   publisher.destroy_node()
   rclpy.shutdown


  
if __name__ == '__main__':
  main()