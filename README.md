# 🔥 Violence Detection App Using OpenCV & CLIP Model

Detect violence in real-time video streams with this smart surveillance system! 🚨👁️‍🗨️

---

## 🚀 Features

- **Real-time multi-video streaming** with live violence detection  
- Powered by **CLIP (Contrastive Language–Image Pretraining) model** for zero-shot image classification 🎯  
- Customizable violence labels (e.g., fights, street violence, fires)  
- Visual alerts on video frames — green text for violence, blue for safe  
- **Adjustable sensitivity** via `prediction-threshold` in `settings.yaml` ⚙️  
- Responsive, scroll-free CCTV-style dashboard with elastic 16:9 video grids 📺  

---

## ⚙️ How It Works

1. Grabs video frames and preprocesses them for the CLIP model.  
2. Converts violence-related labels into text feature embeddings using CLIP.  
3. Compares each frame’s image features with label features to predict violence.  
4. Shows alerts on the video stream based on confidence and threshold.  

---

## 🔧 Configuration

Modify `settings.yaml` to fine-tune your app:

```yaml
model-settings:
  model-name: "ViT-B/32"  # CLIP model variant
  prediction-threshold: 0.24  # Lower = more sensitive, Higher = fewer false alarms

label-settings:
  labels:
    - fight on a street
    - street violence
    - violence in office
    - fire in office
  default-label: "No Violence Detected"
