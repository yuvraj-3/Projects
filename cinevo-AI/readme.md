
# 🧠 CINEVO-AI: YOLOv8 Object Detection Web App

![Banner](logo.jpg)

**CINEVO-AI** is a powerful, user-friendly web application built with **Streamlit** and **YOLOv8** by Ultralytics. It allows users to detect objects in **images**, **videos**, and **live webcam feeds**—including support for **external webcams** and **IP-based phone cameras**. It uses GPU acceleration (if available) and includes a beautiful UI with custom background, sidebar logo, contact links, and download options.

---

## 🚀 Features

- 🖼️ Image-based object detection  
- 🎥 Video-based object detection with frame-by-frame processing  
- 🔴 Real-time webcam detection (laptop, USB webcam, or IP stream)  
- 💻 GPU support via PyTorch CUDA (if available)  
- 📥 Download results (images/videos) after detection  
- 🌄 Background image with custom CSS  
- 🎨 Circular sidebar logo with social links  
- 📱 Mobile IP camera stream detection support  
- 🧠 Powered by [YOLOv8](https://github.com/ultralytics/ultralytics)

---

## 📦 Requirements

Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:
```txt
streamlit
torch
ultralytics
Pillow
opencv-python
numpy
```

---

## 🛠️ Project Structure

```
CINEVO-AI/
│
├── .venv/                         # Virtual environment (optional, usually in .gitignore)
├── app/
│   ├── app.py                     # Main Streamlit app
│   └── app2.py                    # Additional app logic or helper script
├── outputs/
│   ├── detected_image.jpg         # Example output image
│   └── detected_output.mp4        # Example output video
├── results/                       # Results or logs directory (empty by default)
├── uploads/
│   ├── back.jpg                   # Uploaded example image
│   ├── bus.jpg
│   ├── download (1).jpeg
│   ├── zidane.jpg
│   └── ...                        # Other uploads
├── 3.jpg                          # Additional project image
├── back.jpg                       # Additional project image
├── logo.jpg                       # Sidebar logo
├── yolov5s.pt                     # YOLOv5 model checkpoint
├── yolov8n.pt                     # YOLOv8 model checkpoint
├── readme.md                      # Project documentation
└── requirements.txt               # Python dependencies list
```

---

## ▶️ Run the App

```bash
streamlit run app copy.py
```

Then open your browser at: [http://localhost:8501](http://localhost:8501)

---

## 📷 Usage Guide

### 1. **Detect in Image**
- Upload an image (`jpg/png`)
- Click **Detect**
- Download the result

### 2. **Detect in Video**
- Upload a video file (`mp4/avi/mov`)
- Click **Detect Objects in Video**
- Wait for processing and download the result

### 3. **Live Webcam Detection**
- Choose from:
  - Laptop Webcam (default)
  - External Webcam (change index if needed)
  - Phone Camera (via IP stream like `http://192.168.0.101:8080/video`)
- Start and stop live detection

> 💡 Tip: Use apps like **DroidCam** or **IP Webcam** on Android to stream phone camera

---

## 🤝 Credits

- 🔍 [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- 🎨 Sidebar & UI by:  
  - [Shivam Verma](https://www.linkedin.com/in/shivam-verma-17683130a/)  
  - [Yuvraj Kumar](https://www.linkedin.com/in/yuvraj-kumar-78a669323/)

> GitHub:  
> - [Shivam](https://github.com/Shivam5571)  
> - [Yuvraj](https://github.com/yuvraj-3)

📧 Contact:  
- yuvrajkumarsingh303@gmail.com

---
