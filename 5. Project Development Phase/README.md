# 🌊 Flood Prediction System

A Machine Learning based web application that predicts the possibility of floods using historical weather and rainfall data.

---

##  Project Overview

Floods are among the most devastating natural disasters. Early prediction can help authorities and citizens take preventive measures.

This project uses Machine Learning to analyze weather parameters and predict whether flooding is likely to occur.

The application is built using **Python**, **Flask**, and **XGBoost** and provides a simple web interface where users can enter weather information and receive an instant prediction.

---

#  Features

- 🌡 Temperature Prediction Input
- 💧 Humidity Input
- ☁ Cloud Cover Input
- 🌧 Rainfall Analysis
- 🤖 Machine Learning Prediction
- ⚡ Instant Results
- 🎨 Professional Flask Web Interface
- 📱 Responsive Design

---

# Machine Learning

The following Machine Learning algorithms were implemented and compared:

- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- XGBoost (Best Performing Model)

The final deployed model is **XGBoost**.

---

# Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Joblib
- HTML
- CSS
- JavaScript (Basic)

---

# Project Structure

```text
Flood-Prediction-System/
│
├── app.py
├── requirements.txt
├── README.md
├── dataset/
├── notebooks/
├── saved_models/
├── static/
│   ├── css/
│   └── images/
└── templates/
```

---

# ⚙ Installation

Clone the repository

```bash
git clone <repository-link>
```

Move into the project folder

```bash
cd Flood-Prediction-System
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install required libraries

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

Open the browser

```text
http://127.0.0.1:5000
```

---

# Input Features

The model uses the following 10 features:

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

The application predicts one of the following:

- Flood Likely
- No Flood Likely

---


# Future Improvements

- Live Weather API Integration
- Interactive Maps
- Rainfall Visualization
- Location-based Prediction
- Deep Learning Models
- Mobile Application

---

# Developer

**Name:** Doprajna Sai Vadlamudi

B.Tech CSE

SRM University AP

---

# License

This project is developed for educational purposes.

---

# Authors

Doprajna Sai Vadlamudi
Madugundu Surendra
Debosmita Mukhopadhyay
Vedha Sri Tallam