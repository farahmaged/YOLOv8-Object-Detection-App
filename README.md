# Overview

**YOLOv8 Object Detection App** is designed to offer an intuitive interface for real-time object detection using **YOLOv8** model. The application supports a range of input sources, including images, videos, and webcam streams. Users can easily customize the detection process by adjusting parameters such as confidence thresholds and model selection. Built using the **Streamlit** frontend, the app integrates seamlessly with the **YOLOv8** backend for efficient and accurate object detection and classification.

## Usage Instructions

### 1. Set Up the Environment:

Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

# 2. Download Pre-trained YOLOv8 Detection Weights

Create a directory named `weights` and create a subdirectory named `detection`, then save the downloaded YOLOv8 object detection weights inside this directory.  
The weight files can be downloaded from the table below:

| Model | size (pixels) | mAP<sup>val</sup> 50-95 | Speed CPU ONNX (ms) | Speed A100 TensorRT (ms) | params (M) | FLOPs (B) |
|-------|---------------|-------------------------|----------------------|---------------------------|------------|-----------|
| [YOLOv8n](https://huggingface.co/ultralytics/yolov8/resolve/main/yolov8n.pt) | 640 | 37.3 | 80.4 | 0.99 | 3.2 | 8.7 |
| [YOLOv8s](https://huggingface.co/ultralytics/yolov8/resolve/main/yolov8s.pt) | 640 | 44.9 | 128.4 | 1.20 | 11.2 | 28.6 |
| [YOLOv8m](https://huggingface.co/ultralytics/yolov8/resolve/main/yolov8m.pt) | 640 | 50.2 | 234.7 | 1.83 | 25.9 | 78.9 |
| [YOLOv8l](https://huggingface.co/ultralytics/yolov8/resolve/main/yolov8l.pt) | 640 | 52.9 | 375.2 | 2.39 | 43.7 | 165.2 |
| [YOLOv8x](https://huggingface.co/ultralytics/yolov8/resolve/main/yolov8x.pt) | 640 | 53.9 | 479.1 | 3.53 | 68.2 | 257.8 |

### 3. Run the Application:

Launch the Streamlit application with the following command:

```bash
streamlit run app.py
```

### 4. Access the Application:

Open your web browser and navigate to http://localhost:8501/ to interact with the YOLOv8 object detection app.

### 5. Choose Input Source:

- **Image Upload:** Upload an image for object detection.
- **Video Stream:** Provide a video file for object detection.
- **Webcam Stream:** Connect your webcam for real-time object detection.

### 6. Adjust Detection Parameters:

Fine-tune detection settings, such as the confidence threshold and model selection, to achieve the desired detection performance.

### 7. View Detection Results:

Once processed, the app will display detected objects with corresponding labels, bounding boxes, and confidence scores.

## Key Features

- **Multi-Source Input:** Supports a wide range of input sources, including images, videos, and real-time webcam feeds.
  
- **Real-Time Object Detection:** Leverages the latest YOLOv8 model for high-speed, accurate object detection.
  
- **Customizable Detection Settings:** Offers flexibility to adjust key parameters, including the confidence threshold and model selection, for optimal results.
  
- **Interactive UI:** Developed using [Streamlit](https://streamlit.io/), providing an easy-to-use, responsive interface for end users.
  
- **Bounding Box Annotations:** Displays detected objects with bounding boxes, labels, and confidence scores for clear visualization.
  
- **Efficient and Scalable:** Optimized for local machine performance and can be easily scaled for larger applications as needed.
