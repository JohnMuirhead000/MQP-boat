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

 
from ultralytics import YOLO
import sys

import time

from std_msgs.msg           import String
from blob_detector  import *



class find_net(Node):

  def __init__(self):

    
    super().__init__('net_finder')
  
    self.ball_point = Point()
    self.model = YOLO("runs/detect/train15/weights/best.pt")  # build a new model from scratch

    #print (">> Publishing image mask to topic /ball_detect/mask")
    print (">> Publishing Point to topic ball_detect/point")

   # self.pub_image = self.create_publisher(Image, 'ball_image', 10)
    self.pub_point = self.create_publisher(Point, '/ball_point', 10)

    self.bridge = CvBridge()

    print (">> Subscribed to video_frames")
    self.sub = self.create_subscription(Image, 'video_frames', self.pub_coords, 10)


    
  def pub_coords(self, msg):
    point = self.perform_ai(msg)
    print(">> Found Net at point " + str(round(self.ball_point.x, 3)) +  " , " + str(round (self.ball_point.y, 3)))
    self.pub_point.publish(point)

  # TODO: takes in an image and returns the point of the object we want
  def perform_ai(self, image):
      #--- Assuming image is 320x240
       # try:
        cv_image = self.bridge.imgmsg_to_cv2(image)
      
                    
        results = self.model.predict(source=cv_image, save=True, conf=0.40) 

        #TODO: Make this more robust. Currently Only gets first results
        boxes = results[0].boxes

        boxCoord_Array = boxes[0].xyxy.numpy()[0]
    
        print(f'bottom left: ({boxCoord_Array[0]}, {boxCoord_Array[1]}) top Right: ({boxCoord_Array[2]}, {boxCoord_Array[3]}) ')
        
                
        fps = 1.0/(time.time()-self._t0)
        self._t0 = time.time()
        return self.ball_point

      
def main(args=None):
  rclpy.init(args=args)

  net_node = find_net()
  rclpy.spin(net_node)
  net_node.destroy_node()
  rclpy.shutdown

         
if __name__ == '__main__':
    main()