from ultralytics import YOLO
model = YOLO("src/vision/scripts/runs/detect/trainV2/weights/best.pt")
model.predict(source=0, show=True)