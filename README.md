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

| Model   | size (pixels) | mAP<sup>val</sup> 50-95 | params (M) |
|---------|---------------|-------------------------|------------|
| YOLOv8n | 640           | 37.3                    | 3.2        |
| YOLOv8s | 640           | 44.9                    | 11.2       |
| YOLOv8m | 640           | 50.2                    | 25.9       |
| YOLOv8l | 640           | 52.9                    | 43.7       |
| YOLOv8x | 640           | 53.9                    | 68.2       |

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