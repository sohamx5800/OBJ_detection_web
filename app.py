from flask import Flask, render_template, Response, jsonify
import cv2
import numpy as np

app = Flask(__name__)

# Load the models 
net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt", "MobileNetSSD_deploy.caffemodel")

# specify the targeted obj
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor", "tvremote", "flower"]

@app.route('/')
def index():
    return render_template('index.html')

def generate_frames():
    cap = cv2.VideoCapture(1)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            frame_resized = cv2.resize(frame, (300, 300))
            blob = cv2.dnn.blobFromImage(frame_resized, 0.007843, (300, 300), 127.5)
            net.setInput(blob)
            detections = net.forward()
            object_counts = {}

            for i in range(detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                if confidence > 0.2:
                    class_id = int(detections[0, 0, i, 1])
                    box = detections[0, 0, i, 3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
                    (startX, startY, endX, endY) = box.astype("int")

                    label = CLASSES[class_id]
                    if label in object_counts:
                        object_counts[label] += 1
                    else:
                        object_counts[label] = 1

                    cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                    text = "{}: {:.2f}%".format(label, confidence * 100)
                    y = startY - 15 if startY - 15 > 15 else startY + 15
                    cv2.putText(frame, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            app.object_counts = object_counts

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/detected_objects')
def detected_objects():
    return jsonify(object_counts=app.object_counts)

if __name__ == '__main__':
    app.object_counts = {}
    app.run(debug=True)
