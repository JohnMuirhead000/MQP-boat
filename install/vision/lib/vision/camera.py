#!/usr/bin/env python3
# Description:
#   - Basic python ROS node to get Camera Images and transmit it 

# Import the necessary libraries
import rclpy # Python library for ROS
from rclpy.node import Node
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library

class CamPub(Node):
  def __init__(self):

    
    super().__init__('camera')
    self.cap = cv2.VideoCapture(0)
    self.pub = self.create_publisher(Image, 'video_frames', 100)
    timer_period = 0.1  # 100 miliseconds
    self.timer = self.create_timer(timer_period, self.timer_callback) #timer so we dont take too many pictures. Takes picture every 100ms
    
  # Call back function, that will take a publish a frame when the timer expires
  def timer_callback(self):
     # CVBridge converts between ROS and OpenCV images
    br = CvBridge()
    ret, frame = self.cap.read()
     
    if ret == True: #if the capture was successful

        #publish the Frames to the video_frames topic
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
