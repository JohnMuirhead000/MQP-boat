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
import os #used for ENV variables
 
class CamSub(Node):
    
  def __init__(self):
    self.iteration = 0
    super().__init__('camera_debug')
    self.sub = self.create_subscription(Image, 'video_frames', self.process_image,  100)
    print("building the debugger")
    #print("Saving Images to " + os.environ.get("ROS_ImagePath"))
   
    #make sure to to set this every time you open the terminal
    self.PATH = os.environ.get("ROS_ImagePath")
    
  def process_image(self, image):
  # Used to convert between ROS and OpenCV images
    br = CvBridge()
    
    # Convert ROS Image message to OpenCV image
    current_frame = br.imgmsg_to_cv2(image)
    
    # Display image
    PATH = self.PATH + "an_image" + str(self.iteration) + ".png"
    cv2.imwrite(PATH,current_frame)

    cv2.waitKey(30)
    print ("processed image")
    self.iteration = self.iteration + 1

def main(args=None):
   rclpy.init(args=args)
   publisher = CamSub()
   rclpy.spin(publisher)
   publisher.destroy_node()
   rclpy.shutdown


  
if __name__ == '__main__':
  main()
