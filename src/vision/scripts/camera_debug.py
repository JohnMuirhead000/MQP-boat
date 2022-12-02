#!/usr/bin/env python3
# Description:
#   - Basic python ROS DEBUG node receive camera data and save into file


# Import the necessary libraries
import rclpy # Python library for ROS
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
from rclpy.node import Node
import cv2 # OpenCV library
import os #used for ENV variables
 
class CamSub(Node):
    
  def __init__(self):
  
    super().__init__('camera_debug')
    self.sub = self.create_subscription(Image, 'video_frames', self.process_image,  100)
    self.iteration = 0

    print("Init: Finding Image directory")

    # Make sure to to set this every time you open the terminal
    self.PATH = os.environ.get("ROS_ImagePath") 
    
    if self.PATH is None:
      raise Exception("ERROR: Environment variable ROS_ImagePath not set: See ReadMe for details on how to set it")
    else:
      print("Saving Images to: " + str(os.environ.get("ROS_ImagePath"))) #successfully found path
   
    
  # Callback function to process the frames it receives from the Camera.py publisher
  def process_image(self, image):

    # CVBridge converts between ROS and OpenCV images
    br = CvBridge()
    
    # Convert ROS Image message to OpenCV image
    current_frame = br.imgmsg_to_cv2(image)
    
    # Write Image to file under name "an_image"
    imgName = "an_image" + str(self.iteration) + ".png"
    PATH = self.PATH + imgName

    print("Debug: Processing image -> " + imgName)

    # Write frame to file
    cv2.imwrite(PATH,current_frame)
    cv2.waitKey(30)

    # Incement the frame count
    self.iteration = self.iteration + 1

def main(args=None):
   rclpy.init(args=args)
   publisher = CamSub()
   rclpy.spin(publisher)
   publisher.destroy_node()
   rclpy.shutdown


  
if __name__ == '__main__':
  main()
