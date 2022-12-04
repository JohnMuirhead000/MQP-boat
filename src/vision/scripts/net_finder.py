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
 
import sys

import time

from std_msgs.msg           import String
from sensor_msgs.msg        import Image
from geometry_msgs.msg      import Point
from cv_bridge              import CvBridge, CvBridgeError
from blob_detector  import *



class find_net(Node):

  def __init__(self, thr_min, thr_max, blur=15, blob_params=None, detection_window=None):

    
    super().__init__('net_finder')
    #self.pub = self.create_publisher(Point, 'destination_coords', 10)
    #self.sub = self.create_subscription(Image, 'video_frames', self.pub_coords, 10)

    self.set_threshold(thr_min, thr_max)
    self.set_blur(blur)
    self.set_blob_params(blob_params)
    self.detection_window = detection_window
    
    self._t0 = time.time()
    
    self.ball_point = Point()

    print (">> Publishing image to topic ball_detect/image")
    print (">> Publishing image mask to topic /ball_detect/mask")
    print (">> Publishing Point to topic ball_detect/pont")

    self.pub_image = self.create_publisher(Image, 'ball_image', 10)
    self.pub_mask = self.create_publisher(Image, '/ball_mask', 10)
    self.pub_point = self.create_publisher(Point, '/ball_point', 10)

    self.bridge = CvBridge()

    print (">> Subscribed to video_frames")
    self.sub = self.create_subscription(Image, 'video_frames', self.pub_coords, 10)


    
  def pub_coords(self, msg):
    point = self.perform_ai(msg)
    print(">> Found ball at point " + str(round(self.ball_point.x, 3)) +  " , " + str(round (self.ball_point.y, 3)))
    self.pub_point.publish(point)

  # TODO: takes in an image and returns the point of the object we want
  def perform_ai(self, image):
      #--- Assuming image is 320x240
       # try:
        cv_image = self.bridge.imgmsg_to_cv2(image)
        #except CvBridgeError as e:
           # print(e)

        (rows,cols,channels) = cv_image.shape
        if cols > 60 and rows > 60 :
            #--- Detect blobs
            keypoints, mask   = blob_detect(cv_image, self._threshold[0], self._threshold[1], self._blur,
                                            blob_params=self._blob_params, search_window=self.detection_window )
            #--- Draw search window and blobs
            cv_image    = blur_outside(cv_image, 10, self.detection_window)

            cv_image    = draw_window(cv_image, self.detection_window, line=1)
            cv_image    = draw_frame(cv_image)
            
            cv_image    = draw_keypoints(cv_image, keypoints) 
            
            try:
                self.pub_image.publish(self.bridge.cv2_to_imgmsg(cv_image))
                self.pub_mask.publish(self.bridge.cv2_to_imgmsg(mask))
            except CvBridgeError as e:
                print(e)            

            for i, keyPoint in enumerate(keypoints):
                #--- Here you can implement some tracking algorithm to filter multiple detections
                #--- We are simply getting the first result
                x = keyPoint.pt[0]
                y = keyPoint.pt[1]
                s = keyPoint.size
                #print ("kp %d: s = %3d   x = %3d  y= %3d"%(i, s, x, y))
                
                #--- Find x and y position in camera adimensional frame
                x, y = get_blob_relative_position(cv_image, keyPoint)
                
                self.ball_point.x = x
                self.ball_point.y = y
                break 
                
                
                    
            fps = 1.0/(time.time()-self._t0)
            self._t0 = time.time()
            return self.ball_point



  
  def set_threshold(self, thr_min, thr_max):
      self._threshold = [thr_min, thr_max]
      
  def set_blur(self, blur):
      self._blur = blur
    
  def set_blob_params(self, blob_params):
      self._blob_params = blob_params
      
def main(args=None):
  rclpy.init(args=args)

  ball_HSV_min = (19,26,82)
  ball_HSV_max = (46, 209, 255) 

  blur     = 5
  min_size = 10
  max_size = 40
  
  #--- detection window respect to camera frame in [x_min, y_min, x_max, y_max] adimensional (0 to 1)
  x_min   = 0.1
  x_max   = 0.9
  y_min   = 0.4
  y_max   = 0.9
  
  detection_window = [x_min, y_min, x_max, y_max]
  
  params = cv2.SimpleBlobDetector_Params()
        
  # Change thresholds
  params.minThreshold = 0
  params.maxThreshold = 100
    
  # Filter by Area.
  params.filterByArea = True
  params.minArea = 20
  params.maxArea = 20000
    
  # Filter by Circularity
  params.filterByCircularity = True
  params.minCircularity = 0.1
    
  # Filter by Convexity
  params.filterByConvexity = True
  params.minConvexity = 0.2
    
  # Filter by Inertia
  params.filterByInertia = True
  params.minInertiaRatio = 0.7   


  net_node = find_net(ball_HSV_min, ball_HSV_max, blur, params, detection_window)
  rclpy.spin(net_node)
  net_node.destroy_node()
  rclpy.shutdown

         
if __name__ == '__main__':
    main()