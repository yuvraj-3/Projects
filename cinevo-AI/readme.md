# 🧠 CINEVO-AI: YOLOv8 Object Detection Web App

![Banner](cinevo-AI/logo.jpg)

**CINEVO-AI** is a powerful, user-friendly web application built with **Streamlit** and **YOLOv8** by Ultralytics.  
It allows users to detect objects in **images**, **videos**, and **live webcam feeds**—including support for **external webcams** and **IP-based phone cameras**.  
The app supports **GPU acceleration** (if available) and features a beautiful UI with a custom background, sidebar logo, contact links, and download options.

---

## 🚀 Features

- 🖼️ Image-based object detection  
- 🎥 Video-based object detection with frame-by-frame processing  
- 🔴 Real-time webcam detection (laptop, USB webcam, or IP stream)  
- 💻 GPU support via PyTorch CUDA (if available)  
- 📥 Download results (images/videos) after detection  
- 🌄 Custom background image with CSS  
- 🎨 Circular sidebar logo with social links  
- 📱 Mobile IP camera stream detection support  
- 🧠 Powered by **YOLOv8**

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
Example requirements.txt:
nginx
Copy
Edit
streamlit
torch
ultralytics
Pillow
opencv-python
numpy
🛠️ Project Structure
bash
Copy
Edit
cinevo-AI/
│
├── app copy.py               # Main Streamlit app
├── yolov8n.pt                # YOLOv8 model (auto-downloaded if not present)
├── photo-ai.jpeg             # Background image
├── cinevo ai.jpg             # Sidebar circular logo
├── requirements.txt          # Dependencies
└── outputs/                  # Folder to store output videos
▶️ Run the App
bash
Copy
Edit
streamlit run "app copy.py"
Then open your browser at http://localhost:8501

📷 Usage Guide
1. Image Detection
Upload a JPG/PNG image

Click Detect

Download the processed image

2. Video Detection
Upload a video file (MP4/AVI/MOV)

Click Detect Objects in Video

Wait for processing and download the output video

3. Live Webcam Detection
Choose from:

💻 Laptop webcam (default)

🧩 External USB webcam (change index if needed)

📱 Phone IP camera (e.g. http://192.168.0.101:8080/video)

Start and stop detection from the app UI.

💡 Use Android apps like DroidCam or IP Webcam to stream your phone camera over Wi-Fi.

🤝 Credits
🔍 YOLOv8 by Ultralytics

🎨 Sidebar & UI design by:

Shivam Verma

Yuvraj Kumar

📧 Contact
Yuvraj Kumar
📬 yuvrajkumarsingh303@gmail.com
📎 GitHub: github.com/yuvraj-3