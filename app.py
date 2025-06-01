from flask import Flask, render_template, Response
import cv2
import numpy as np
from model import Model

app = Flask(__name__)
model = Model()

# List of video files
video_files = [
    'video1.mp4',
    'video2.mp4',
    'video3.mp4',
    'video4.mp4'
    # Add more video files here
]

# Define violence labels
violence_labels = {'fight on a street', 'street violence', 'violence in office', 'fire in office'}


def generate_frames(video_path):
    """Generate frames from the given video source."""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Unable to open video source: {video_path}")

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # Process the frame
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        prediction = model.predict(image=image)
        label_text = prediction['label']

        # Display the label only if it's a violence-related label
        if label_text in violence_labels:
            cv2.putText(frame, f'Predicted: {label_text}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,
                        cv2.LINE_AA)
        else:
            cv2.putText(frame, 'No Violence Detected', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2,
                        cv2.LINE_AA)

        # Convert frame to JPEG
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Yield frame as byte stream
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    """Render the main page with video streams."""
    return render_template('index.html', video_files=enumerate(video_files))


@app.route('/video_feed/<int:index>')
def video_feed(index):
    """Serve video frames for the given video index."""
    try:
        if 0 <= index < len(video_files):
            video_path = video_files[index]
            return Response(generate_frames(video_path),
                            mimetype='multipart/x-mixed-replace; boundary=frame')
        else:
            return "Video index out of range", 404
    except ValueError as e:
        return str(e), 404


if __name__ == '__main__':
    app.run(debug=True)
