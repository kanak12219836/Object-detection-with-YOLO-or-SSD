# Real-Time Object Detection using YOLOv8

## Overview

This project is a Computer Vision application that performs real-time object detection using YOLOv8. It detects and classifies multiple objects in **static images**, **pre-recorded videos**, and **live webcam feeds** using bounding boxes and labels.

Built with **Python**, **Ultralytics YOLOv8**, and **OpenCV**, this project demonstrates practical implementation of AI-powered object detection for surveillance, traffic analysis, and automation systems.

---

## Features

* **Image Detection** – Detect objects from static images
* **Video Detection** – Perform object detection frame-by-frame on videos
* **Live Webcam Detection** – Real-time object detection using webcam
* **Pretrained YOLOv8 Model** – Uses YOLOv8 Nano (`yolov8n.pt`)
* **Bounding Boxes & Labels** – Displays object classes clearly

---

## Technologies Used

* Python
* Ultralytics YOLOv8
* OpenCV
* COCO Dataset (Pretrained Model)

---

## Project Structure

```bash
Object_Detection_YOLO/
│
├── images/
│   └── car.jpg
│
├── videos/
│   └── traffic-video.mp4
│
├── output/
│
├── yolo_image.py
├── yolo_video.py
├── yolo_webcam.py
└── README.md
```

---

## Installation

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-link>
cd Object_Detection_YOLO
```

### Step 2: Install Required Libraries

```bash
pip install ultralytics opencv-python
```

---

## Usage

### Image Detection

```bash
python yolo_image.py
```

### Video Detection

```bash
python yolo_video.py
```

### Live Webcam Detection

```bash
python yolo_webcam.py
```

---

## How It Works

1. Loads pretrained YOLOv8 model
2. Accepts input source (image, video, webcam)
3. Processes frames using object detection
4. Identifies objects with labels
5. Displays bounding boxes around detected objects

---

## YOLOv8 Advantages

* High-speed real-time detection
* Better accuracy
* Efficient for multiple object classes
* Easy integration with Python
* Suitable for surveillance and automation

---

## Applications

* Traffic Monitoring
* Security Surveillance
* Smart City Systems
* Autonomous Vehicles
* Retail Analytics

---

## Sample Output

* Detects cars, people, trucks, and more
* Works on images, recorded videos, and live feeds

---

## Future Improvements

* Custom dataset training
* Face detection integration
* Object tracking
* License plate detection
* GUI dashboard

---

## Learning Outcomes

Through this project, I gained hands-on experience in:

* Computer Vision
* YOLOv8 Implementation
* OpenCV Integration
* Real-Time AI Systems
* Object Localization

---

## Author

**Kanak Sharma**

---

## License

This project is for educational and learning purposes.
