import os
import uuid
from pathlib import Path
from functools import wraps
import cv2
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from ultralytics import YOLO
from werkzeug.utils import secure_filename

BASE = Path(__file__).resolve().parent
UPLOADS = BASE / 'static' / 'uploads'
UPLOADS.mkdir(parents=True, exist_ok=True)
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'local-demo-change-before-deployment')
app.config['MAX_CONTENT_LENGTH'] = 12 * 1024 * 1024
MODEL = None
CLASSES = ['Anemic Nail', 'Anemic Tongue', 'Non-Anemic Nail', 'Non-Anemic Tongue']

def get_model():
    global MODEL
    if MODEL is None:
        MODEL = YOLO(str(BASE / 'best.pt'))
    return MODEL

def protected(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        if not session.get('authenticated'):
            return redirect(url_for('login'))
        return fn(*args, **kwargs)
    return wrapped

@app.route('/', methods=['GET', 'POST'])
def login():
    if session.get('authenticated'):
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        if username == os.environ.get('DEMO_USERNAME', 'admin') and password == os.environ.get('DEMO_PASSWORD', 'admin'):
            session.clear()
            session['authenticated'] = True
            return redirect(url_for('home'))
        flash('Incorrect username or password.', 'error')
    return render_template('login.html')

@app.route('/home')
@protected
def home():
    return render_template('home.html', active='home')

@app.route('/about')
@protected
def about():
    return render_template('about.html', active='about')

@app.route('/prediction', methods=['GET', 'POST'])
@protected
def prediction():
    if request.method == 'GET':
        return render_template('prediction.html', active='prediction', result=None)
    file = request.files.get('file')
    if not file or not file.filename:
        flash('Please choose an image.', 'error')
        return redirect(url_for('prediction'))
    if Path(file.filename).suffix.lower() not in {'.jpg', '.jpeg', '.png', '.bmp', '.webp'}:
        flash('Upload a JPG, PNG, BMP, or WEBP image.', 'error')
        return redirect(url_for('prediction'))
    name = uuid.uuid4().hex
    input_path = UPLOADS / (name + Path(secure_filename(file.filename)).suffix.lower())
    file.save(input_path)
    img = cv2.imread(str(input_path))
    if img is None:
        input_path.unlink(missing_ok=True)
        flash('This file could not be decoded as an image.', 'error')
        return redirect(url_for('prediction'))
    try:
        prediction = get_model().predict(source=img, conf=0.15, verbose=False)[0]
        names = prediction.names
        items = []
        for box in prediction.boxes:
            idx = int(box.cls[0].item())
            items.append({'name': str(names[idx]), 'confidence': round(float(box.conf[0].item()) * 100, 1)})
        items.sort(key=lambda x: x['confidence'], reverse=True)
        output_path = UPLOADS / (name + '_result.jpg')
        cv2.imwrite(str(output_path), prediction.plot())
        result = {'image': 'uploads/' + output_path.name, 'items': items, 'top': items[0] if items else None}
        return render_template('prediction.html', active='prediction', result=result)
    except Exception:
        app.logger.exception('Prediction failed')
        flash('Prediction failed. Check the server terminal for details.', 'error')
        return redirect(url_for('prediction'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.errorhandler(413)
def too_large(error):
    flash('Image is too large (maximum 12 MB).', 'error')
    return redirect(url_for('prediction'))

if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT', '5001')), debug=False)
