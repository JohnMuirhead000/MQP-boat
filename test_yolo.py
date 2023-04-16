from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library 
from ultralytics import YOLO

model = YOLO("src/vision/scripts/runs/detect/trainV2/weights/best.pt")  # build a new model from scratch
 
model.export(format="onnx",opset=12) 

