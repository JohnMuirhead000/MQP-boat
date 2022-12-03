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
 
class NetFinderDebug(Node):
    
  def __init__(self):
  
    super().__init__('net_finder_debug')
    self.sub_image = self.create_subscription(Image, 'ball_image', self.process_image,  100)
    self.sub_mask = self.create_subscription(Image, 'ball_mask', self.process_mask,  100)
    
    self.mask_interation = 0
    self.image_interation = 0

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
    imgName = "debug_image_" + str(self.image_interation) + ".png"
    

    savePath = self.PATH +  "debug_images/" + imgName

    print("Debug: Processing Debug Image -> " + imgName + " @ "  + savePath)

    # Write frame to file
    cv2.imwrite(savePath,current_frame)
    cv2.waitKey(30)

    # Incement the frame count
    self.image_interation = self.image_interation + 1

    # Callback function to process the frames it receives from the Camera.py publisher
  def process_mask(self, image):

    # CVBridge converts between ROS and OpenCV images
    br = CvBridge()
    
    # Convert ROS Image message to OpenCV image
    current_frame = br.imgmsg_to_cv2(image)
    
    # Write Image to file under name "an_image"
    maskName = "debug_mask" + str(self.mask_interation) + ".png"
   
    print("Debug: Processing Mask -> " + maskName + " @ "  +self.PATH)
    savePath = self.PATH + "debug_masks/" + maskName

    # Write frame to file
    cv2.imwrite(savePath,current_frame)
    cv2.waitKey(30)

    # Incement the frame count
    self.mask_interation = self.mask_interation + 1


def main(args=None):
   rclpy.init(args=args)
   publisher = NetFinderDebug()
   rclpy.spin(publisher)
   publisher.destroy_node()
   rclpy.shutdown


  
if __name__ == '__main__':
  main()
