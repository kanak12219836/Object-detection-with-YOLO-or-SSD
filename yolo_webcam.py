from ultralytics import YOLO
import cv2

# Load YOLOv8 pretrained model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

# Check webcam
if not cap.isOpened():
    print("Error: Could not access webcam.")
    exit()

# Get webcam frame properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = 20  # Standard webcam recording FPS

# Save output webcam video
out = cv2.VideoWriter(
    "output/detected_webcam.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (frame_width, frame_height)
)

print("Controls:")
print("Q = Quit Webcam Detection")

while True:
    # Capture frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Perform YOLO detection
    results = model(frame, verbose=False)

    # Draw bounding boxes
    annotated_frame = results[0].plot()

    # Save detected frame
    out.write(annotated_frame)

    # Show live detection
    cv2.imshow("YOLOv8 Live Webcam Detection", annotated_frame)

    # Quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()