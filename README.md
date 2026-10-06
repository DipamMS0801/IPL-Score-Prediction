# 🏏 IPL Score Prediction

A Machine Learning-based web application that predicts the final score of an IPL team based on current match statistics. The model is integrated with a Streamlit interface and deployed online for interactive predictions.

## 🚀 Live Demo

👉 **Live Application:**  
https://ipl-scoreprediction.streamlit.app

---

## 📌 Project Overview

In a cricket match, the first inning final score depends on several factors such as the current score, overs completed, wickets fallen, and recent scoring performance.

This project uses historical IPL match data to build a Machine Learning model that predicts the approximate final score of a batting team based on the current state of the match.

The trained model is integrated into a Streamlit web application where users can enter match information and receive an estimated final score.

---

## 🎯 Objectives

- Analyze historical IPL match data.
- Perform data preprocessing and exploratory data analysis.
- Train a Machine Learning regression model.
- Predict the final score of an IPL innings.
- Build an interactive web interface using Streamlit.
- Deploy the application online for public access.

---

## 🧠 Machine Learning Approach

The project uses **Linear Regression, Decision Tree, Random Forest**  to predict the final score.

The prediction is based on the following input features:

- Batting Team
- Bowling Team
- Overs Completed
- Current Runs
- Current Wickets
- Runs Scored in Previous 5 Overs
- Wickets Lost in Previous 5 Overs

The categorical team variables are converted into numerical one-hot encoded features before being passed to the model.

### Prediction Flow

```text
Match Information
       ↓
Data Preprocessing
       ↓
One-Hot Encoding
       ↓
Linear Regression Model
       ↓
Predicted Final Score