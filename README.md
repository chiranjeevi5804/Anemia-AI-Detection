# Anemia AI — Image-based Detection Research Prototype

A Flask + YOLOv8 demo for experimental detection of four nail/tongue image classes. Rebuilt from provided UI screenshots and an existing `best.pt` model.

## Run on Windows

```cmd
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5001. Default **local demo** credentials: `admin` / `admin`. Set `DEMO_USERNAME`, `DEMO_PASSWORD`, and `SECRET_KEY` environment variables before sharing access. This demo login is not a production authentication system.

## Model

`best.pt` is an existing trained YOLO model, not trained by this rebuild. The app reads its class names from the model and displays detected bounding boxes and confidence scores. It has not been clinically validated.

## Disclaimer

This is an educational research prototype, not a medical device. An image prediction cannot confirm or rule out anemia. Consult a qualified healthcare professional and obtain appropriate blood tests.

## GitHub

The included model is approximately 137 MB, exceeding GitHub's normal 100 MB file limit. Use Git LFS or keep the model outside the repository and document how to obtain it. Never upload private patient images.
