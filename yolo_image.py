from ultralytics import YOLO
import cv2

# Load YOLOv8 pretrained model
model = YOLO("yolov8n.pt")

# Image path
image_path = "images/car.jpg"

# Perform detection
results = model(image_path)

# Display and save result
for result in results:
    annotated_image = result.plot()

    # Save detected image
    cv2.imwrite("output/detected_car.jpg", annotated_image)

    # Show detected image
    cv2.imshow("YOLOv8 Object Detection", annotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()