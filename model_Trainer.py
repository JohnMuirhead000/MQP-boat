from ultralytics import YOLO

CONFIDENCE_INTERVAL = 0.45
SAVE_RESULTS = True
EPOCHS = 150

# Build a new model from scratch
model = YOLO("yolov8n.yaml") 

#model = YOLO("yolov8n.pt")  # load a pretrained model


# Train the model
results = model.train(data="data.yaml", epochs=EPOCHS)  # train the model

val = model.val(conf=CONFIDENCE_INTERVAL, save=SAVE_RESULTS)  # evaluate model performance on the validation set
