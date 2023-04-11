#!/usr/bin/env python3
# Description:
#   - Basic python ROS node to get Camera Images and transmit it 

# Import the necessary libraries
import rclpy # Python library for ROS
from rclpy.node import Node
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library
import os


class CameraSpoofer(Node):
  def __init__(self):
    super().__init__('camera_Spoofer')

    # Make sure to to set this every time you open the terminal
    self.PATH = os.environ.get("ROS_VideoPath") 
    
    if self.PATH is None:
      raise Exception("ERROR: Environment variable ROS_VideoPath not set: See ReadMe for details on how to set it")
    else:
      print("Loading Video from: " + str(os.environ.get("ROS_VideoPath"))) #successfully found path


    # Load video and publish
    self.cap = cv2.VideoCapture(self.PATH)

    self.pub = self.create_publisher(Image, 'video_frames', 100)
    timer_period = 0.1  # 100 miliseconds
    self.timer = self.create_timer(timer_period, self.timer_callback) #timer so we dont take too many pictures. Takes picture every 100ms
    
  # Call back function, that will take a publish a frame when the timer expires
  def timer_callback(self):

    # CVBridge converts between ROS and OpenCV images
    br = CvBridge()
    ret, frame = self.cap.read()
     
    if ret == True: #if the capture was successful

        # Resize the frame | small frame optimise the run
        frame_width = int(self.cap.get(3))
        frame_height = int(self.cap.get(4))
        frame = cv2.resize(frame, (frame_width, frame_height))

        #publish the Frames to the video_frames topic
        print("Publishing image from Video")
        self.pub.publish(br.cv2_to_imgmsg(frame))

    else:
         print("Can't receive frame (stream end?)")
            
        
def main(args=None):
   rclpy.init(args=args)
   publisher = CameraSpoofer()
   rclpy.spin(publisher)
   publisher.destroy_node()
   rclpy.shutdown
   
    

         
if __name__ == '__main__':
    main()
