import rclpy # Python library for ROS
from rclpy.node import Node
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library

from ultralytics import YOLO

# Load a model  
#model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("runs/detect/train4/weights/best.pt")  # build a new model from scratch
#model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
#results = model.train(data="data.yaml", epochs=100)  # train the model

#val = model.val()  # evaluate model performance on the validation set

results = model.predict(source= "0",show=True)  # predict on an webcam...

#results = model.predict(source="test/images", show=True) 


k=input("press close to exit") 


