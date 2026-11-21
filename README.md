# Anemia AI Detection Using YOLOv8

### Non-Invasive Anemia Screening Using Deep Learning and Computer Vision

Anemia AI Detection is a web-based machine learning application designed to explore non-invasive anemia screening through the analysis of fingernail and tongue images. The system uses a trained YOLOv8 object detection model to identify visual patterns associated with anemic and non-anemic appearances.

The application integrates **Python, Flask, YOLOv8, OpenCV, HTML, CSS, and JavaScript** to provide an interactive interface for image uploads, model inference, visual annotations, and confidence-score display.

> **Disclaimer:** This project is intended for research and educational purposes only. It is not a clinically validated diagnostic tool and cannot replace blood tests or professional medical evaluation.

---

## Project Overview

Traditional anemia diagnosis typically involves blood tests such as a Complete Blood Count (CBC) to evaluate hemoglobin levels and other blood parameters.

This project investigates an image-based approach that uses computer vision to analyze visible characteristics of fingernails and the tongue.

The system allows users to upload an image, processes it using a trained YOLOv8 model, and displays the detected class along with an annotated image and model confidence score.

### Project Objectives

- Develop a web-based application for experimental anemia screening.
- Apply deep learning techniques to fingernail and tongue image analysis.
- Use YOLOv8 for object detection and classification.
- Identify four predefined detection classes.
- Display annotated predictions and model confidence scores.
- Provide a responsive and user-friendly interface.
- Explore the potential of computer vision in non-invasive health-screening research.

---

## Key Features

### 1. User Authentication

- Login interface for accessing the application.
- Session-based access to protected pages.
- Logout functionality.

The current login system is intended for local demonstration and should be replaced with secure authentication before deployment.

### 2. Interactive Dashboard

- Modern dark-themed user interface.
- Project introduction and overview.
- Navigation between Home, About, and Prediction pages.
- Information about the detection workflow.

### 3. AI-Based Image Analysis

- Upload fingernail or tongue images.
- Process images using the trained YOLOv8 model.
- Detect regions associated with the model's predefined classes.
- Display annotated images with bounding boxes.

### 4. Prediction Results

- Display the detected class.
- Show model confidence scores.
- Present annotated detection images.
- Support multiple detected regions when available.
- Provide feedback when no detection is found.

### 5. Research Information

- Overview of the system architecture.
- Explanation of the detection process.
- Description of the four detection classes.
- Educational information about the project.

---

## Detection Classes

The YOLOv8 model is configured to identify four classes:

| Class | Description |
|---|---|
| Anemic Nail | Fingernail appearance classified by the model as associated with anemia |
| Non-Anemic Nail | Fingernail appearance classified by the model as non-anemic |
| Anemic Tongue | Tongue appearance classified by the model as associated with anemia |
| Non-Anemic Tongue | Tongue appearance classified by the model as non-anemic |

**Important:** These labels represent model classifications, not confirmed medical conditions. A confidence score indicates the model's confidence in a detection, not the probability that a person has anemia.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming and model integration |
| Flask | Web application framework |
| YOLOv8 | Deep learning object detection |
| Ultralytics | YOLO model loading and inference |
| PyTorch | Deep learning framework used by YOLO |
| OpenCV | Image processing and annotations |
| NumPy | Numerical and image-array operations |
| HTML5 | Webpage structure |
| CSS3 | Responsive user interface styling |
| JavaScript | Frontend interactions |
| Jinja2 | Dynamic HTML template rendering |

---

## System Architecture

The application follows a Flask-based web architecture integrated with a trained YOLOv8 model.

**Processing Workflow:**

1. User accesses the web application.
2. User logs in to the dashboard.
3. User navigates to the Prediction page.
4. User uploads a fingernail or tongue image.
5. Flask receives and validates the uploaded file.
6. The image is processed by the YOLOv8 model.
7. The model generates detections and confidence scores.
8. The application creates an annotated result image.
9. The prediction result is displayed on the webpage.

---

## Project Structure

```text
Anemia-AI-Detection/
│
├── app.py
├── run.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── best.pt
│
├── templates/
│   ├── login.html
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   └── prediction.html
│
└── static/
    ├── style.css
    └── uploads/
```

**Note:** `best.pt` is downloaded separately from GitHub Releases. The `uploads` directory is used locally for uploaded images and generated prediction results; these files are not included in the repository.

---

## Download the Trained YOLOv8 Model

The trained YOLOv8 model is stored separately because its size exceeds GitHub's standard repository upload limit.

**Model filename:** `best.pt`

**Model size:** Approximately 130 MB

**Release version:** `v1.0.0`

### Download Link

[Download YOLOv8 Trained Model — GitHub Release v1.0.0](https://github.com/chiranjeevi5804/Anemia-AI-Detection/releases/tag/v1.0.0)

### Model Setup

1. Open the release link.
2. Expand the **Assets** section.
3. Download `best.pt`.
4. Place the file in the root directory of the downloaded project, alongside `app.py`.

The application requires this model file to perform predictions.

---

## Installation and Setup

### Prerequisites

Ensure that the following are installed:

- Python 3.10 or later with compatible dependencies.
- pip (Python package manager).
- A modern web browser.
- Git (optional, for cloning the repository).

### Step 1: Clone the Repository

```bash
git clone https://github.com/chiranjeevi5804/Anemia-AI-Detection.git
```

Navigate to the project folder:

```bash
cd Anemia-AI-Detection
```

Alternatively, download the source code as a ZIP file from GitHub and extract it.

### Step 2: Create a Virtual Environment

On Windows:

```cmd
py -m venv .venv
```

Activate it:

```cmd
.venv\Scripts\activate
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

Installation may take several minutes because YOLOv8 uses PyTorch and other machine learning dependencies.

### Step 4: Download the Model

Download `best.pt` from the GitHub Release linked above.

Place it in the project root:

```text
Anemia-AI-Detection/
├── app.py
├── best.pt
└── requirements.txt
```

### Step 5: Run the Application

```bash
python app.py
```

Once the Flask server starts, open:

http://127.0.0.1:5001

### Step 6: Access the Dashboard

For local demonstration, use the login credentials configured in the application.

**Security note:** Do not use demonstration credentials or hardcoded secret keys in a publicly deployed application.

---

## How to Use

### 1. Login

Open the application and sign in using the locally configured demonstration account.

### 2. Explore the Dashboard

The Home page provides information about the project, detection workflow, and related research.

### 3. Open the Prediction Page

Navigate to **Prediction** using the top navigation bar.

### 4. Upload an Image

Choose a clear image of a fingernail or tongue.

Supported formats include:

- JPG / JPEG
- PNG
- BMP
- WEBP

### 5. Analyze the Image

Click **Analyze Image**.

The application sends the image to the YOLOv8 model for inference.

### 6. View the Results

The application displays:

- Annotated image.
- Predicted detection class.
- Model confidence score.
- Additional detected regions, when present.

A prediction should not be interpreted as a medical diagnosis.

---

## Model Workflow

### Image Acquisition

Fingernail and tongue images are used as inputs for the detection model.

### Data Preparation

The training workflow involves organizing image datasets and their corresponding annotations into a format compatible with YOLOv8.

### Model Training

YOLOv8 learns visual features from labeled training examples.

The trained model weights are saved as `best.pt`.

### Model Inference

During prediction, the trained model processes the uploaded image and generates detection outputs.

### Result Visualization

The application displays bounding boxes, class labels, and confidence scores associated with the model's predictions.

---

## User Interface

The application includes four main interface components.

### Login Page

A dark-themed login interface for accessing the application.

### Home Page

A project dashboard containing the system introduction, workflow, and research information.

### About Page

An overview of the system, its architecture, detection process, and supported classes.

### Prediction Page

An interactive image-upload interface displaying model predictions and annotated results.

---

## Testing

The application can be tested using sample fingernail and tongue images.

Recommended functional tests include:

1. Verify that the login page opens.
2. Verify navigation between Home, About, and Prediction.
3. Upload a valid image.
4. Confirm that the YOLOv8 model processes the image.
5. Verify that the annotated result is displayed.
6. Check that class labels and confidence scores appear.
7. Test unsupported file formats.
8. Verify that the application handles images with no detections.

**Note:** Functional testing does not establish clinical accuracy. Clinical validation would require appropriately collected medical data, reference diagnoses, and rigorous evaluation.

---

## Limitations

- The system is an experimental research prototype.
- Predictions depend on image quality, lighting, camera conditions, and training data.
- Visual appearance alone cannot reliably confirm or exclude anemia.
- Model confidence scores are not calibrated clinical probabilities.
- The system does not measure hemoglobin concentration.
- The application requires further evaluation before any real-world clinical use.
- The current demonstration authentication is not intended for production use.

---

## Future Enhancements

Potential future improvements include:

- Expanding the training dataset with more diverse, clinically verified images.
- Evaluating model performance on independent test datasets.
- Improving robustness to different lighting conditions and image qualities.
- Implementing secure user authentication.
- Adding a prediction history dashboard with appropriate privacy safeguards.
- Developing an optional mobile interface.
- Improving model interpretability.
- Conducting clinical validation in collaboration with healthcare professionals.

---

## GitHub Release

**Version:** `v1.0.0`

**Status:** Pre-release — Experimental Research Prototype

**Included asset:** `best.pt` (trained YOLOv8 model)

[View Release and Download Model](https://github.com/chiranjeevi5804/Anemia-AI-Detection/releases/tag/v1.0.0)

---

## License

No license has been specified for this repository. All rights are reserved unless a license is added.

---

## Medical Disclaimer

This application is developed for academic, research, and educational purposes.

The output generated by the machine learning model must not be used as a substitute for professional medical advice, diagnosis, or treatment.

Anemia requires appropriate clinical evaluation, including laboratory testing when indicated.

**Anemia AI Detection — Exploring Computer Vision and Deep Learning for Non-Invasive Health-Screening Research.**
