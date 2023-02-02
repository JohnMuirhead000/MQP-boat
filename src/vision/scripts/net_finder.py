import rclpy # Python library for ROS
from rclpy.node import Node
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library

from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
#model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
results = model.train(data="data.yaml", epochs=3)  # train the model
results = model.val()  # evaluate model performance on the validation set
results = model("test_net.jpg")  # predict on an image
success = model.export(format="onnx")  # export the model to ONNX format



