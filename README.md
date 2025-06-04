# 🛡️ Violence Detection App using OpenCV + CLIP

Welcome to the **Violence Detection App** — a lightweight, AI-powered system that monitors video streams and detects violent or harmful activities in real-time using **OpenAI's CLIP**, **OpenCV**, and **PyTorch**.

Ideal for surveillance, content moderation, and safety automation.

---

## 🚀 Features

- 🎥 Real-time video stream analysis using webcam or video file
- 🔍 Violence/harm detection using **zero-shot CLIP model**
- 📸 Automatic frame capture upon detection
- 📂 Easily configurable detection sensitivity via `settings.yaml`
- ⚙️ Modular and extensible architecture

---

## 🧠 How It Works

The app uses OpenAI’s CLIP model to match visual frames against text descriptions like `"a photo of violence"` or `"a photo of normal activity"`.  
It calculates the similarity between the image and text features and selects the most likely label.

A confidence threshold is used to determine whether a frame should be flagged.

✅ If the confidence is below the threshold → considered normal  
⚠️ If the confidence is **greater than or equal to the threshold** → considered **violent**

---

## 🖼️ Examples

✅ No violence detected — everything is running smoothly:  
<img src="https://github.com/user-attachments/assets/ef2e8f67-29ac-416f-99c6-7a9d3391deb0" alt="No Violence" width="500"/>

⚠️ Violence detected — immediate action recommended:  
<img src="https://github.com/user-attachments/assets/f86f2108-52a9-43fd-af2f-69fccd2385c8" alt="Violence Detected" width="500"/>

---

## ⚙️ Configuration

The app behavior is fully controlled through `settings.yaml`.

Example configuration:

```yaml
model-settings:
  model-name: ViT-B/32
  prediction-threshold: 0.24  # 📌 Adjust sensitivity here

📌 Lower values make the model more sensitive (may increase false positives)  
📌 Higher values reduce sensitivity (may miss subtle incidents)

label-settings:
  labels:
    - violence
    - normal activity
  default-label: normal activity
``yaml
---
```
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
