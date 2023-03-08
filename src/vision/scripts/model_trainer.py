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

val = model.val(conf=0.45, save=True)  # evaluate model performance on the validation set

#results = model.predict(source= "0",show=True)  # predict on an webcam...

#https://docs.ultralytics.com/cfg/

# test_net.jp test_NoNet.png test/images
results = model.predict(source="test/images", save=True,conf=0.40) 

print("Result: " )
print (results)



boxes = results[0].boxes

print("Result boxes " )
print (boxes)
boxCoord_Array = boxes[0].xyxy.numpy()[0]

print("Coord result: " )
#print(boxCoord_Array[0])
print(f'bottom left: ({boxCoord_Array[0]}, {boxCoord_Array[1]}) top Right: ({boxCoord_Array[2]}, {boxCoord_Array[3]}) ')

print ("orig size")
print(results[0].orig_shape)
k=input("press close to exit") 








