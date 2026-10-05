# Diabetes Progression Predictor

## Project Overview
This project develops a machine learning-based Diabetes Progression Predictor using the diabetes dataset available through scikit-learn.

The workflow includes data loading, exploratory data analysis, visualization, feature scaling, machine learning model development, evaluation, model selection, and deployment using Streamlit.

## Dataset
The project uses the built-in Diabetes dataset from scikit-learn.

- Samples: 442
- Input features: 10
- Target: Diabetes disease progression score

## Machine Learning Models
Two regression models were developed and compared:

1. Linear Regression
2. Random Forest Regressor

## Evaluation Metrics
Models were evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

## Workflow
1. Dataset loading
2. Dataset exploration
3. Missing-value analysis
4. Exploratory data visualization
5. Correlation analysis
6. Train-test split
7. Feature scaling
8. Model training
9. Model evaluation
10. Best model selection
11. Model serialization using Joblib
12. Streamlit application development

## Application
The Streamlit application accepts the ten input features and predicts the diabetes progression score using the trained machine learning model.

## Disclaimer
This project is intended for educational and research purposes only and is not a medical diagnostic tool.
