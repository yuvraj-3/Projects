import streamlit as st
import torch
from PIL import Image
import cv2
import os
import tempfile
import numpy as np
import base64

# ------------------- Background Setup -------------------
def get_base64_image(path):
    with open(path, "rb") as img_file:
        data = img_file.read()
    return base64.b64encode(data).decode()

image_path = "back.jpg"  # Make sure this file is in the same directory
base64_img = get_base64_image(image_path)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{base64_img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------- Sidebar with Logo -------------------
@st.cache_resource
def display_logo(logo_path, title):
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as logo_file:
            encoded_logo = base64.b64encode(logo_file.read()).decode()

        st.sidebar.markdown(
            f"""
            <div style="display: flex; align-items: center;">
                <img src="data:image/png;base64,{encoded_logo}" style="border-radius: 50%; width: 60px; height: 60px; margin-right: 10px;">
                <h3 style="margin: 0;">{title}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

logo_path = "logo.jpg"
display_logo(logo_path, "CINEVO-AI")
st.sidebar.markdown("<hr style='margin: 20px 0;'>", unsafe_allow_html=True)
st.sidebar.header("💼 Connect With Us:")
st.sidebar.markdown("[🐱 GitHub](https://github.com/yuvraj-3), [🐱 GitHub-2](https://github.com/Shivam5571)")
st.sidebar.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/yuvraj-kumar-78a669323/)")
st.sidebar.markdown("📧 Email: yuvrajkumarsingh303@gmail.com")
st.sidebar.markdown("<hr style='margin: 20px 0;'>", unsafe_allow_html=True)

# ------------------- Load YOLOv5 Model -------------------
@st.cache_resource
def load_model():
    return torch.hub.load('yolov5', 'yolov5s', source='local')

model = load_model()

st.title("🎬 CINEVO-AI")

option = st.selectbox("What would you like to detect?", ( "Objects in Image", "Objects in Video", "Live Detection (Webcam)"))

# ------------------- Image Detection -------------------
if option == "Objects in Image":
    uploaded_file = st.file_uploader("📷 Upload an Image", type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='🖼 Uploaded Image', use_container_width=True)

        if st.button("🚀 Detect Objects"):
            temp_path = os.path.join("uploads", uploaded_file.name)
            os.makedirs("uploads", exist_ok=True)
            image.save(temp_path)

            results = model(temp_path)
            results.render()

            result_image = Image.fromarray(results.ims[0])
            st.image(result_image, caption="🎯 Detection Result", use_container_width=True)

            result_path = os.path.join("outputs", "detected_image.jpg")
            os.makedirs("outputs", exist_ok=True)
            result_image.save(result_path)

            with open(result_path, "rb") as f:
                st.download_button(
                    label="⬇️ Download Processed Image",
                    data=f,
                    file_name="detected_image.jpg",
                    mime="image/jpeg"
                )

# ------------------- Video Detection -------------------
elif option == "Objects in Video":
    uploaded_video = st.file_uploader("🎥 Upload a Video", type=['mp4', 'mov', 'avi'])
    if uploaded_video is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())
        video_path = tfile.name

        st.video(video_path)

        if st.button("🚀 Detect Objects in Video"):
            st.info("Processing video... please wait ⏳")

            cap = cv2.VideoCapture(video_path)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)

            output_dir = "outputs"
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, "detected_output.mp4")

            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

            frame_count = 0
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                results = model(frame)
                results.render()
                annotated_frame = results.ims[0]
                out.write(annotated_frame)
                frame_count += 1

            cap.release()
            out.release()

            st.success(f"✅ Done! Processed {frame_count} frames.")
            with open(output_path, "rb") as f:
                st.download_button(
                    label="⬇️ Download Processed Video",
                    data=f,
                    file_name="detected_output.mp4",
                    mime="video/mp4"
                )

# ------------------- Live Webcam Detection -------------------

elif option == "Live Detection (Webcam)":
    st.warning(" Works only locally. Cloud Streamlit can't access your webcam.")

    start = st.button("🎥 Start Live Detection")

    if start:
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            st.error("❌ Cannot access webcam.")
        else:
            stframe = st.empty()
            stop_button = st.button(" Stop Detection")

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                results = model(frame)
                results.render()
                detected_frame = results.ims[0]
                stframe.image(detected_frame, channels="BGR", use_container_width=True)

                # Break loop if Stop Detection is pressed
                if stop_button:
                    st.success("🛑 Detection stopped.")
                    break

            cap.release()
