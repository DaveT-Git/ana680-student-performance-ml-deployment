# Student Ethnicity Predictor App

Flask web application that predicts a student's race/ethnicity group (A–E) based on math, reading, and writing scores, using the Kaggle StudentsPerformance dataset.

## Important Note on Model Performance

**This project is for educational and demonstration purposes only.**

The model is a simple Random Forest classifier trained solely on three test scores (math, reading, writing). It achieves only **modest test accuracy (~34–35%)** due to substantial overlap in score distributions across ethnic groups — test scores alone provide weak predictive signal for this demographic outcome.

- This is **not** a robust or production-ready classifier.
- Accuracy is intentionally limited to reflect real-world data complexity (per project instructions: "accuracy is important, but not essential").
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

Run the application locally:

```bash
python app.py
