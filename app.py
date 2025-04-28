from pathlib import Path
import streamlit as st
import config
from utils import load_model, infer_uploaded_image, infer_uploaded_video, infer_uploaded_webcam

st.set_page_config(
    page_title="YOLOv8 Interactive Object Detection App",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("YOLOv8 Interactive Object Detection App")

st.sidebar.header("Deep Learning Model Config")

model_type = st.sidebar.selectbox(
    "Select Model",
    config.DETECTION_MODEL_LIST
)

confidence = float(st.sidebar.slider(
    "Select Model Confidence", 30, 100, 50)) / 100

model_path = ""
if model_type:
    model_path = Path(config.DETECTION_MODEL_DIR, str(model_type))
else:
    st.error("Please select model in sidebar")

try:
    model = load_model(model_path)
except Exception as e:
    st.error(f"Unable to load model. Please check the specified path: {model_path}")

st.sidebar.header("Image/Video Config")

source_selectbox = st.sidebar.selectbox(
    "Select Source",
    config.SOURCES_LIST
)

source_img = None
if source_selectbox == config.SOURCES_LIST[0]:
    infer_uploaded_image(confidence, model)
elif source_selectbox == config.SOURCES_LIST[1]:
    infer_uploaded_video(confidence, model)
elif source_selectbox == config.SOURCES_LIST[2]:
    infer_uploaded_webcam(confidence, model)
