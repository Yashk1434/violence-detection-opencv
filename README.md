# 🛡️ Violence Detection App using OpenCV

Welcome to the **Violence Detection App** — an AI-powered system designed to monitor video streams and detect violent or harmful activities in real-time using computer vision and deep learning. Built with **OpenCV**, this tool is ideal for surveillance, safety enforcement, and smart monitoring applications.

---

## 🚀 Features

- 🎥 Real-time video feed analysis
- 🔍 Detection of violent/harmful activities
- 📸 Screenshots captured upon detection
- ⚙️ Configurable detection sensitivity
- 🧩 Easy to set up and integrate

---

## 🧠 How It Works

Each frame from a video stream is analyzed using a trained deep learning model. Based on the prediction confidence, the app determines whether violence is occurring. When violence is detected, it can trigger alerts, logging, or automated actions.

---

## 🖼️ Examples

✅ No violence detected — everything is running smoothly:  
<img src="https://github.com/user-attachments/assets/ef2e8f67-29ac-416f-99c6-7a9d3391deb0" alt="No Violence" width="500"/>

⚠️ Violence detected — immediate action recommended:  
<img src="https://github.com/user-attachments/assets/f86f2108-52a9-43fd-af2f-69fccd2385c8" alt="Violence Detected" width="500"/>


---

## ⚙️ Configuration

All app settings can be found in the `settings.yaml` file.

To adjust the sensitivity of the violence detection system, modify the `prediction-threshold` value:

``yaml
📌 Lower values make the model more sensitive (may increase false positives)  
📌 Higher values reduce sensitivity (may miss subtle incidents)

---

## 🛠️ Requirements

- Python 3.7 or higher  
- OpenCV (`cv2`)  
- PyYAML  
- NumPy  
- TensorFlow or PyTorch (based on the model used)

Install all dependencies using:

```bash
pip install -r requirements.txt
```
---

## ▶️ Running the App

To run the application:

```bash
python app.py
```
