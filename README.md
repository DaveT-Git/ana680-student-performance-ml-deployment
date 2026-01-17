# Student Ethnicity Predictor App

Flask web application that predicts a student's race/ethnicity group (A–E) based on math, reading, and writing scores, using the Kaggle StudentsPerformance dataset.

## Important Note on Model Performance

**This project is for educational and demonstration purposes only.**

The model is a simple Random Forest classifier trained solely on three test scores (math, reading, writing). It achieves only **modest test accuracy (~34–35%)** due to substantial overlap in score distributions across ethnic groups — test scores alone provide weak predictive signal for this demographic outcome.

- This is **not** a robust or production-ready classifier.
- Accuracy is intentionally limited to reflect real-world data complexity (per project instructions: "accuracy is important, but not essential").
- Groups are anonymized (A–E) as in the original dataset.
- Results should be viewed as illustrative of basic ML deployment, not as meaningful demographic inference.
- Adding more features (e.g., gender, lunch type, parental education) would improve performance significantly, but the current version sticks to the specified scores.

This app serves as an academic exercise in building and deploying a minimal Flask API with an interactive HTML form (ANA680 project requirements).

## Features Used
- Math Score (0–100)
- Reading Score (0–100)
- Writing Score (0–100)

## Model
- Random Forest Classifier (n_estimators=100–200)
- Test Accuracy: ~0.34–0.35 (modest, as expected)

Run the application:

`python app.py`

Open: http://127.0.0.1:5000

## Deployment

**Live URL:**  
https://student-perf-predictor-djt-e3512ff2a961.herokuapp.com/

**Note:** The app is hosted on a Heroku Eco dyno, so the first load after inactivity may take 10–30 seconds while it wakes up.

### Screenshots

#### 1. Input Form (empty state)
<img width="464" height="381" alt="Screenshot 2026-01-17 at 12 57 24 PM" src="https://github.com/user-attachments/assets/1387fb20-288d-43ef-b0f3-79fb33253220" />

The main interface where users enter math, reading, and writing scores (0–100).

#### 2. Form with Prediction Result
<img width="466" height="405" alt="Screenshot 2026-01-17 at 12 58 51 PM" src="https://github.com/user-attachments/assets/c87b1cbd-8573-4b6c-9ada-af87f07a2493" />

Example after submitting scores — the predicted ethnicity group appears below the form (e.g., “Predicted Group: group C”).
