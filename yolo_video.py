from ultralytics import YOLO
import cv2

# Load YOLOv8 pretrained model
model = YOLO("yolov8n.pt")

# Load input video
cap = cv2.VideoCapture("videos/traffic-video.mp4")

# Check video
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Save output video
out = cv2.VideoWriter(
    "output/detected_traffic.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (frame_width, frame_height)
)

paused = False
annotated_frame = None

print("Controls:")
print("SPACE = Pause/Resume")
print("Q = Quit")

while cap.isOpened():

    if not paused:
        ret, frame = cap.read()

        if not ret:
            print("Video completed.")
            paused = True
        else:
            # YOLO detection
            results = model(frame, verbose=False)

            # Annotated frame
            annotated_frame = results[0].plot()

            # Save frame
            out.write(annotated_frame)

    # Show frame
    if annotated_frame is not None:
        cv2.imshow("YOLOv8 Video Detection", annotated_frame)

    key = cv2.waitKey(30) & 0xFF

    # Quit
    if key == ord('q'):
        break

    # Pause / Resume
    elif key == 32:
        paused = not paused

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()