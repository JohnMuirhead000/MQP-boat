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
import random
from std_msgs.msg           import String
from blob_detector  import *



# Constants
CONFIDENCE_INTERVAL = 0.25
FRAME_HEIGHT = 640
FRAME_WIDTH = 480

CLASS_LIST = ["net", "person", "wall", "divider"]

# The colors of each class's bounding box
BOX_COLORS = []
for i in range(len(CLASS_LIST)):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    BOX_COLORS.append((b, g, r))

FONT = cv2.FONT_HERSHEY_TRIPLEX
FONT_COLOR = (255, 255, 255)  # White
FONT_SIZE = 1.1             # Float
FONT_THICKNESS = 2          # Int




class find_net(Node):

  def __init__(self):

    
    super().__init__('net_finder')
  
    self.net_point = Point()
    self.model = YOLO("src/vision/scripts/runs/detect/trainV2/weights/best.pt")  # build a new model from scratch

    
    print (">> Publishing Point to topic /net_detect/point")
    print (">> Publishing annotated images to topic /net_detect/image")

    self.pub_image = self.create_publisher(Image, '/net_detect/image', 10)
    self.pub_point = self.create_publisher(Point, '/net_detect/point', 10)

    self.bridge = CvBridge()

    print (">> Subscribed to video_frames")
    self.sub = self.create_subscription(Image, 'video_frames', self.pub_coords, 10)


    
  def pub_coords(self, msg):
    point = self.detect_net(msg)
    if (point is not None): 
      self.pub_point.publish(point)
    else:
       print("Point is NONE")

  # TODO: takes in an image and returns the point of the object we want
  def detect_net(self, image):
        self.net_point = Point()
     
        cv_image = self.bridge.imgmsg_to_cv2(image)
      
        # Run object detection prediction
        results = self.model.predict(source=cv_image, save=False, conf=CONFIDENCE_INTERVAL) 
  
        # Convert the tensor array to numpy array
        detection_array = results[0].numpy()

        # For each detection in image, draw bounding box and publish imag
        if (len(detection_array) != 0):
            for i in range(len(results[0])):
                box = results[0].boxes[i]               # Get box
                class_id = (int)(box.cls.numpy()[0])    # Class id
                confidence = box.conf.numpy()[0]       # Confidence interval
                bound_box = box.xyxy.numpy()[0]         # The bounding box xy
                detected_class=  CLASS_LIST[class_id]



                # Draw bounding boxes
                cv2.rectangle(cv_image, (int(bound_box[0]), int(bound_box[1])), (int(
                    bound_box[2]), int(bound_box[3])), BOX_COLORS[class_id], 3)

                # Display class name and confidence Interval
                cv2.putText(
                    cv_image,
                    CLASS_LIST[class_id] + " - " +
                    str((int)(confidence*100)) + "%",
                    (int(bound_box[0]), int(bound_box[1]) - 10),
                    FONT, FONT_SIZE, FONT_COLOR, FONT_THICKNESS)

              
                #print(f'Found {detected_class} conf {confidence}  at bottom left: ({bound_box[0]}, {bound_box[1]}) top Right: ({bound_box[2]}, {bound_box[3]}) ')
                
                # Find the center of the object
                x = (bound_box[0] + bound_box[2])/2
                y = (bound_box[1] + bound_box[3])/2

                self.net_point.x = x
                self.net_point.y = y
                
            # After all detections made, export image... but only send 1 of the net locations... For now!!! TODO!!
            self.pub_image.publish(self.bridge.cv2_to_imgmsg(cv_image))
            return  self.net_point
        else:
            #print(f'No Nets found')
            self.net_point.x = float(0)
            self.net_point.y = float(0)
            # -1 on z indicates no net
            self.net_point.z = float(-1)
            return self.net_point



        return None

      
def main(args=None):
  rclpy.init(args=args)

  net_node = find_net()
  rclpy.spin(net_node)
  net_node.destroy_node()
  rclpy.shutdown

         
if __name__ == '__main__':
    main()

