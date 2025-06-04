# 🔥 Violence Detection App Using OpenCV & CLIP

Detect violence in real-time video streams effortlessly with this smart surveillance system! 🚨👁️‍🗨️

---

## 🚀 Features

- **Real-time multi-video streaming** with live violence detection  
- Uses **OpenAI’s CLIP model** for zero-shot image classification 🎯  
- Customizable violence labels (e.g., fights, street violence, fires)  
- Visual alerts on video frames — green text for violence, blue for safe  
- **Adjustable sensitivity** via `prediction-threshold` in `settings.yaml` ⚙️  
- Responsive, scroll-free CCTV-style dashboard with elastic 16:9 video grids 📺  

---

## ⚙️ How It Works

1. Grab video frames and preprocess them for the model.  
2. Convert violence-related labels to CLIP text features.  
3. Compare each frame’s image features with label features to predict violence.  
4. Show alerts on the video stream based on confidence and threshold.  

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
