# Real-Time Object Detection Web App

This project is a Flask-based web application that performs real-time object detection using a webcam. The app utilizes the pre-trained MobileNetSSD model for object detection and displays the video feed along with bounding boxes around detected objects. Additionally, the app counts and lists the detected objects on the webpage.

## Features:
- **Real-Time Object Detection**: Captures video feed from the webcam and performs object detection in real-time.
- **Object Counting**: Counts the number of detected objects and displays the count on the webpage.
- **User-Friendly Interface**: Modern and responsive design with separate sections for the video feed and detected objects.
- **Technology Stack**: Utilizes Flask for the backend, OpenCV for video processing, and HTML/CSS/JavaScript for the frontend.

## Project Structure:
- `app.py`: Main Flask application.
- `static/`: Folder containing static files (CSS and JavaScript).
  - `styles.css`: Styling for the webpage.
  - `script.js`: JavaScript for updating detected objects.
- `templates/`: Folder containing HTML templates.
  - `index.html`: Main HTML template.
- `MobileNetSSD_deploy.prototxt.txt`: Configuration file for the MobileNetSSD model.
- `MobileNetSSD_deploy.caffemodel`: Pre-trained MobileNetSSD model.
- `haarcascade_eye.xml`: Haar cascade for eye detection.
- `haarcascade_frontalface_default.xml`: Haar cascade for face detection.

## How to Run:
1. Clone the repository:
   ```bash
   git clone https://github.com/sohamx5800/OBJ_detection_web.git
   cd OBJ_detection_web
