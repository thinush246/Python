import cv2
import urllib.request
import numpy as np
import os

# ========= Configuration =========
# Your ESP32-CAM snapshot URL
url = 'http://192.168.8.144/cam-hi.jpg'

# Path where YOLO files are stored
base_path = r"c:\Users\Admin\OneDrive\Desktop\Python\ESP"

weightsPath = os.path.join(base_path, "yolov4-tiny.weights")
configPath  = os.path.join(base_path, "yolov4-tiny.cfg")
namesPath   = os.path.join(base_path, "coco.names")

# ========= Load YOLO =========
print("Loading YOLOv4-tiny...")
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

layer_names = net.getLayerNames()
# Fix for OpenCV 4.x (flatten output layer indexes)
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]

with open(namesPath, "r") as f:
    classes = [line.strip() for line in f.readlines()]

print("YOLOv4-tiny loaded successfully!")

# ========= Windows =========
cv2.namedWindow("Live", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Detection", cv2.WINDOW_AUTOSIZE)

# ========= Main Loop =========
while True:
    try:
        # Fetch frame from ESP32-CAM
        img_resp = urllib.request.urlopen(url)
        imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        frame = cv2.imdecode(imgnp, -1)

        if frame is None:
            continue

        # Show raw feed
        cv2.imshow("Live", frame)

        # Prepare input for YOLO
        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Process detections
        class_ids = []
        confidences = []
        boxes = []
        h, w = frame.shape[:2]

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * w)
                    center_y = int(detection[1] * h)
                    width = int(detection[2] * w)
                    height = int(detection[3] * h)
                    x = int(center_x - width / 2)
                    y = int(center_y - height / 2)
                    boxes.append([x, y, width, height])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Non-max suppression
        indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        detection_frame = frame.copy()
        for i in indices.flatten():   # flatten here too
            x, y, w_box, h_box = boxes[i]
            label = str(classes[class_ids[i]])
            conf = confidences[i]
            cv2.rectangle(detection_frame, (x, y), (x + w_box, y + h_box), (0, 255, 0), 2)
            cv2.putText(detection_frame, f"{label} {conf:.2f}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Show detection window
        cv2.imshow("Detection", detection_frame)

    except Exception as e:
        print("Error:", e)
        continue

    # Exit on 'q'
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()