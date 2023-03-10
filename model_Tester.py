import rclpy  # Python library for ROS
from rclpy.node import Node
from sensor_msgs.msg import Image  # Image is the message type
from cv_bridge import CvBridge  # Package to convert between ROS and OpenCV Images
import cv2  # OpenCV library
from ultralytics import YOLO
import os
import random

import supervision
from supervision import Detections, BoxAnnotator, ColorPalette

# Paths
MODEL_PATH = 'runs/detect/train4/weights/best.pt'
TEST_IMAGES_PATH = 'Model_Data/test/images'
ANNOTATED_IMAGE_PATH = "Annotated_Images/"
ANNOTATED_VIDEO_PATH = "Annotated_Video/"

TEST_VIDEO_PATH = "Annotated_Video/Pool_VIdeo_ShorterOne_RAW.mov"
TEST_VIDEO_SAVE_PATH = "annotated_Video.mp4"
RANDOM_TEST_PATH = "Model_Data/test/Random Tests"

VALIDATE = False
PREDICT = True
USE_VIDEO = True # True: Use Video or Camera, False: Uses images
USE_CAMERA = False # True: uses webcam, False uses video

# Constants
CONFIDENCE_INTERVAL = 0.45
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

# Load the custom model
model = YOLO(MODEL_PATH)

# Dict maping class_id to class_name
CLASS_NAMES_DICT = model.model.names

# Class_ids of interest - net... TODO: Add walls, other obstacles
CLASS_ID = [0]


def process_Images():
    # Store images in list
    images = []
    for filename in os.listdir(TEST_IMAGES_PATH):
        img = cv2.imread(os.path.join(TEST_IMAGES_PATH, filename))
        if img is not None:
            images.append(img)

    # Interate through each image and perform object detection
    image_number = 0
    for image in images:
        results = model.predict(source=image,
                                save=False, conf=CONFIDENCE_INTERVAL)

        # Convert results from Tensor to Numpy array
        detection_array = results[0].numpy()

        # For each detection in image, draw bounding box and save
        if (len(detection_array) != 0):
            for i in range(len(results[0])):
                box = results[0].boxes[i]               # Get box
                class_id = (int)(box.cls.numpy()[0])    # Class id
                confidence = box.conf.numpy()[0]       # Confidence interval
                bound_box = box.xyxy.numpy()[0]         # The bounding box xy

                # Draw bounding boxes
                cv2.rectangle(image, (int(bound_box[0]), int(bound_box[1])), (int(
                    bound_box[2]), int(bound_box[3])), BOX_COLORS[class_id], 3)

                # Display class name and confidence Interval
                cv2.putText(
                    image,
                    CLASS_LIST[class_id] + " - " +
                    str((int)(confidence*100)) + "%",
                    (int(bound_box[0]), int(bound_box[1]) - 10),
                    FONT, FONT_SIZE, FONT_COLOR, FONT_THICKNESS)

                filename = ANNOTATED_IMAGE_PATH + \
                    "image_" + str(image_number) + ".png"
                print(filename)
                cv2.imwrite(filename, image)

        image_number = image_number + 1


def process_Camera():
    process_Video(True)


def process_Video(isCamera):

    if (not isCamera):
        cap = cv2.VideoCapture(TEST_VIDEO_PATH)
    else:
        cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open video")
        exit()

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    frame_size = (frame_width,frame_height)
    fps = 10
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    
    print("Frame Size = " + str(frame_size))
    # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
    out = cv2.VideoWriter(TEST_VIDEO_SAVE_PATH, fourcc, fps, frame_size)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Resize the frame | small frame optimise the run
        frame = cv2.resize(frame, (frame_width, frame_height))
       

        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        

        # Predict on image
        results = model.predict(
            source=[frame], conf=CONFIDENCE_INTERVAL, save=False)

        # Convert tensor array to numpy
        detection_array = results[0].numpy()

        # For each detection in image, draw bounding box and save
        if (len(detection_array) != 0):
            for i in range(len(results[0])):
                box = results[0].boxes[i]               # Get box
                class_id = (int)(box.cls.numpy()[0])    # Class id
                confidence = box.conf.numpy()[0]       # Confidence interval
                bound_box = box.xyxy.numpy()[0]         # The bounding box xy

                # Draw bounding boxes
                cv2.rectangle(frame, (int(bound_box[0]), int(bound_box[1])), (int(
                    bound_box[2]), int(bound_box[3])), BOX_COLORS[class_id], 3)

                # Display class name and confidence Interval
                cv2.putText(
                    frame,
                    CLASS_LIST[class_id] + " - " +
                    str((int)(confidence*100)) + "%",
                    (int(bound_box[0]), int(bound_box[1]) - 10),
                    FONT, FONT_SIZE, FONT_COLOR, FONT_THICKNESS)


        #         # Write the frame into the file 'output.avi'
        cv2.imshow("Annotated Frame",frame)

         # Terminate run when "Q" pressed
        if cv2.waitKey(1) == ord('q'):
            break

        out.write(frame)
       

    # Clean Up
    cap.release()
    out.release()

    # Closes all the frames
    cv2.destroyAllWindows()
    cv2.waitKey(1) 



def main():
    if (VALIDATE):
        # Validate model
        # evaluate model performance on the validation set
        val = model.val(conf=CONFIDENCE_INTERVAL, save=True)


    if (PREDICT):
        print("Running Predictions and drawing Bounding Boxes")

        if (USE_VIDEO):
            print("Processing Video: USE_CAMERA = " + str(USE_CAMERA))
            print("Saving results to " + ANNOTATED_VIDEO_PATH)
            print("_________________________________________________________\n")
            process_Video(USE_CAMERA)
            
        else:
            print("Processing Images: " + TEST_IMAGES_PATH)
            print("Saving results to " + ANNOTATED_IMAGE_PATH)
            print("_________________________________________________________\n")
            process_Images()

        
        

if __name__ == "__main__":
    main()


# Helpful tips

#  Model.predict Parameters:
#   - source = "0"  -> Default webcam
#   - source = "test/images"    -> images from test folder: test_net.jpg, test_NoNet.png, test/images
#
#   - conf= 0.40    -> confidence interval to consider
#   - save=True     -> Save the results
#
#   https://docs.ultralytics.com/cfg/