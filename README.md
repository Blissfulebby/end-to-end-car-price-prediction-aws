<p align="center">
  <img src="images/banner.png" alt="End-to-End Used Car Price Prediction" width="100%">
</p>

# 🚗 End-to-End Used Car Price Prediction on AWS

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikitlearn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit&logoColor=white)
![AWS EC2](https://img.shields.io/badge/AWS-EC2-FF9900?logo=amazonaws&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-181717?logo=github&logoColor=white)

## 📌 Project Overview

This project is an end-to-end Machine Learning application that predicts the selling price of used cars based on vehicle characteristics. It demonstrates the complete machine learning workflow—from data preprocessing and exploratory data analysis (EDA) to model training, evaluation, deployment with Streamlit, and cloud hosting on AWS EC2.

The project was built to showcase practical Data Science and Machine Learning skills using Python and Scikit-learn.

---

## 🎯 Business Problem

Pricing used vehicles accurately is essential for dealerships, online marketplaces, and private sellers. Manual pricing is often subjective and inconsistent.

This application predicts the estimated selling price of a used vehicle based on key vehicle attributes, helping users make data-driven pricing decisions.

---

# 🛠️ Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib |
| Machine Learning | Scikit-learn |
| Model | Random Forest Regressor |
| Web Application | Streamlit |
| Cloud Platform | AWS EC2 |
| Model Persistence | Joblib |
| Version Control | Git & GitHub |

---

# 📂 Dataset

The dataset contains information about used vehicles including:

- Brand
- Model
- Vehicle Age
- Kilometers Driven
- Mileage
- Maximum Power
- Number of Seats
- Selling Price (Target Variable)

---

# 🔍 Features Used for Model Training

- Brand
- Model
- Vehicle Age
- Kilometers Driven
- Mileage
- Maximum Power
- Seats

Target Variable:

- Selling Price (₦)

---

# ⚙️ Machine Learning Workflow

✔ Data Cleaning

✔ Exploratory Data Analysis (EDA)

✔ Feature Engineering

✔ Train/Test Split

✔ Model Training

✔ Model Evaluation

✔ Model Serialization using Joblib

✔ Streamlit Web Application

✔ AWS EC2 Deployment

---

# 🤖 Models Evaluated

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

After evaluation, the **Random Forest Regressor** was selected as the final model because it delivered the best predictive performance.

---

# 📊 Exploratory Data Analysis

## Feature Importance

<p align="center">
<img src="images/feature_importance.png" width="800">
</p>

---

## Correlation Heatmap

<p align="center">
<img src="images/correlation_heatmap.png" width="800">
</p>

---

## Outlier Detection

<p align="center">
<img src="images/outlier_boxplots.png" width="800">
</p>

---

# 💻 Streamlit Web Application

The application allows users to enter vehicle information and instantly receive a predicted selling price.

<p align="center">
<img src="images/streamlit_app.png" width="900">
</p>

---

# ☁️ AWS EC2 Deployment

The Streamlit application was successfully deployed on **Amazon Web Services (AWS EC2)** during development.

Deployment included:

- Launching an EC2 instance
- Installing project dependencies
- Running the Streamlit application
- Hosting the application through a public IP address

> **Note:** The live deployment is currently unavailable because the AWS Free Tier account has expired. The complete source code remains available in this repository and can be redeployed.

---

# 📁 Project Structure

```text
end-to-end-car-price-prediction-aws/
│
├── images/
│   ├── banner.png
│   ├── streamlit_app.png
│   ├── feature_importance.png
│   ├── correlation_heatmap.png
│   └── outlier_boxplots.png
│
├── car_data_v2.csv
├── car_price.pkl
├── car_price_app.py
├── train_app.py
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Blissfulebby/end-to-end-car-price-prediction-aws.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run car_price_app.py
```

---

# 📈 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Machine Learning
- Model Evaluation
- Random Forest Regression
- Streamlit
- AWS EC2 Deployment
- Git & GitHub
- Python Programming

---

# 👩🏽‍💻 Author

**Agatha Onwudiwe**

**Data Scientist | Data Analyst**

📧 Email: agatha.onwudiwe@gmail.com

💼 LinkedIn: https://www.linkedin.com/in/agatha-onwudiwe-86b87215b

🌐 Portfolio: https://blissfulebby.github.io/AggiePortfolio

GitHub: https://github.com/Blissfulebby


- Python
- SQL
- Power BI
- Machine Learning
- AWS
- Streamlit

---

## ⭐ If you found this project helpful, please consider giving it a star!
