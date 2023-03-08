#!/usr/bin/env python3
# Basics ROS program to publish real-time streaming
# video from your built-in webcam
# Author: Shane Stevens - WPI '23 - smstevens@wpi.edu

import rclpy  # Python library for ROS
from rclpy.node import Node
from geometry_msgs.msg import Point
from sensor_msgs.msg import Image  # Image is the message type
from cv_bridge import CvBridge  # Package to convert between ROS and OpenCV Images
import cv2  # OpenCV library
import time
from std_msgs.msg import String
from blob_detector import *
from ultralytics import YOLO
import sys


class find_net(Node):

    def __init__(self):
        super().__init__('net_finder')

        self.net_point = Point()

        # Load the Custom YOLO Model
        self.model = YOLO("runs/detect/train4/weights/best.pt")

        print(">> Publishing Point to topic net_detect/point")
        print(">> Publishing Image to topic net_detect/image")
        self.pub_point = self.create_publisher(Point, 'net_detect/point', 10)
        self.pub_image = self.create_publisher(Image, 'net_detect/image', 10)

        print(">> Subscribed to video_frames")
        self.sub_frames = self.create_subscription(
            Image, 'video_frames', self.sub_Frames, 10)

        # Used to convert between ROS and OpenCV images
        self.bridge = CvBridge()


    # Subscribes to video_frames topic and passes frames to perform-ai
    #   Input: Frame from Camera
    #   Output: Point (x,y) indicating the location of the net in the frame

    def sub_Frames(self, msg):
        # Get point net is found at (x,y)
        point = self.find_Net(msg)

        print(">> Found Net at point " + str(round(self.net_point.x, 3)
                                             ) + " , " + str(round(self.net_point.y, 3)))
        # Publish the point
        self.pub_point.publish(point)


    # Recieves image and performs Object Recognition
    #   Input: Frame from Camera
    #   Output: Point (x,y) indicating the location of the net in the frame

    def find_Net(self, image):

        # Convert ROS image to OpenCV image
        cv_image = self.bridge.imgmsg_to_cv2(image)

        # Look for Net in frame
        results = self.model.predict(source=cv_image, save=True, conf=0.40)

        # TODO: Make this more robust. Currently Only gets first results
        boxes = results[0].boxes
        boxCoord_Array = boxes[0].xyxy.numpy()[0]

        print(
            f'Bottom left: ({boxCoord_Array[0]}, {boxCoord_Array[1]}) Top Right: ({boxCoord_Array[2]}, {boxCoord_Array[3]}) ')

       # Unused
       # fps = 1.0/(time.time()-self._t0)
       # self._t0 = time.time()

        return self.ball_point


# Generally Not used: only if net_finder is being run as the main script
def main(args=None):

    print(">> Net_Finder running as Main")

    # Initialize the rclpy library
    rclpy.init(args=args)

    # Create Node
    net_node = find_net()

    # Spin the node so the callback function is called.
    rclpy.spin(net_node)

    # Clean up
    net_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
