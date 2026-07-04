# Flood Prediction System

A Machine Learning-based web application that predicts the likelihood of floods using historical weather and rainfall data. The application leverages an XGBoost model integrated with a Flask web framework to provide real-time flood predictions through a simple and responsive web interface.

---

# Project Links

| Resource | Link |
|----------|------|
| **Live Demo** | https://flood-prediction-system-3fv8.onrender.com |
| **GitHub Repository** | https://github.com/doprajnasai/Rising-Waters |

---

# Project Overview

Floods are among the most devastating natural disasters, causing severe damage to human life, agriculture, and infrastructure. Early prediction enables authorities and communities to take preventive measures and minimize potential losses.

This project analyzes weather and rainfall parameters using Machine Learning to predict whether flooding is likely to occur. The system follows the complete Machine Learning lifecycle, including data preprocessing, model training, evaluation, deployment, and user interaction through a Flask web application.

---

# Features

- Weather parameter input through an intuitive web interface
- Flood likelihood prediction using Machine Learning
- Real-time prediction results
- Input validation for all weather parameters
- Responsive and user-friendly interface
- XGBoost-based prediction model
- Flask backend integration
- Cloud deployment on Render

---

# Machine Learning

The following Machine Learning algorithms were trained and evaluated:

- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- XGBoost

After performance evaluation, **XGBoost** was selected as the final deployed model because it achieved the best prediction accuracy.

---

# Technology Stack

| Layer | Technologies |
|-------|--------------|
| Programming Language | Python |
| Web Framework | Flask |
| Machine Learning | XGBoost, Scikit-learn |
| Data Processing | Pandas, NumPy |
| Model Storage | Joblib |
| Frontend | HTML5, CSS3, Jinja2 |
| Development Tools | Jupyter Notebook, VS Code |
| Version Control | Git, GitHub |
| Deployment | Render |

---

# Project Structure

```text
Flood-Prediction-System/
│
├── app.py
├── Procfile
├── requirements.txt
├── README.md
├── .gitignore
│
├── dataset/
│   └── flood_dataset.xlsx
│
├── notebooks/
│   └── Flood_Prediction.ipynb
│
├── saved_models/
│   ├── flood_model.joblib
│   └── scaler.joblib
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       └── flood.jpg
│
├── templates/
    ├── index.html
    └── predict.html
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/doprajnasai/Flood-Prediction-System.git
```

## Navigate to the Project Directory

```bash
cd Flood-Prediction-System
```

## Create a Virtual Environment

```bash
python -m venv venv
```

## Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

## Open in Browser

```text
http://127.0.0.1:5000
```

---

# Input Features

The prediction model uses the following weather parameters:

1. Temperature
2. Humidity
3. Cloud Cover
4. Annual Rainfall
5. Jan-Feb Rainfall
6. Mar-May Rainfall
7. Jun-Sep Rainfall
8. Oct-Dec Rainfall
9. Average June Rainfall
10. Subdivision Rainfall

---

# Prediction Output

The system predicts one of the following outcomes:

- Flood Likely
- No Flood Likely

---

# Future Improvements

- Live Weather API Integration
- Location-Based Flood Prediction
- Interactive GIS Flood Maps
- Rainfall Trend Visualization
- Mobile Application
- Deep Learning-Based Prediction Models
- Email and SMS Alert System

---

# Deployment

The application is deployed on **Render** and is publicly accessible.

**Live Application**

https://flood-prediction-system-3fv8.onrender.com

---

# Authors

- Doprajna Sai Vadlamudi
- Madugundu Surendra
- Debosmita Mukhopadhyay
- Vedha Sri Tallam

---

# License

This project is developed for educational and academic purposes.
