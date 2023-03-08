import rclpy # Python library for ROS
from rclpy.node import Node
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library
from ultralytics import YOLO

CONFIDENCE_INTERVAL = 0.45
SAVE_RESULTS = True


# Build a new model from scratch
model = YOLO("yolov8n.yaml") 

#model = YOLO("yolov8n.pt")  # load a pretrained model


# Train the model
results = model.train(data="data.yaml", epochs=100)  # train the model

val = model.val(conf=CONFIDENCE_INTERVAL, save=SAVE_RESULTS)  # evaluate model performance on the validation set
