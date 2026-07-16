# 📊 Sales Analytics and Prediction System

## Overview

The **Sales Analytics and Prediction System** is an end-to-end Machine Learning and Data Analytics project developed using Python, Flask, SQL, and Scikit-learn. The project analyzes historical sales data, provides business insights through exploratory data analysis (EDA) and SQL queries, and predicts the deal size of a sales order using a trained Machine Learning model.

The application allows users to enter order details through a web interface and receive an ML-based prediction while also demonstrating data preprocessing, feature engineering, model training, and deployment.

---

## Problem Statement

Businesses generate large volumes of sales data every day. Analyzing this data manually is time-consuming and makes it difficult to identify trends and support decision-making.

This project aims to:

* Analyze historical sales data.
* Identify sales trends and customer insights.
* Train a Machine Learning model using historical records.
* Predict the deal size of a new sales order.
* Provide a simple web interface for making predictions.

---

## Features

* Data cleaning and preprocessing using Pandas.
* Exploratory Data Analysis (EDA).
* SQL-based business analysis.
* Machine Learning model training using Random Forest Classifier.
* Prediction of Sales Deal Size (Small, Medium, Large).
* User-friendly Flask web application.
* Responsive HTML/CSS interface.
* Ready for cloud deployment.

---

## Dataset

The project uses a historical sales dataset containing information such as:

* Order Number
* Quantity Ordered
* Price Each
* Sales
* Order Date
* Product Line
* MSRP
* Country
* Territory
* Customer Details
* Deal Size
* Order Status

---

## Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn
* Joblib

### Web Development

* Flask
* HTML
* CSS
* JavaScript

### Database

* MySQL

### Data Analysis

* SQL
* Matplotlib
* Seaborn

---

## Machine Learning Workflow

1. Data Cleaning
2. Exploratory Data Analysis
3. Feature Selection
4. One-Hot Encoding
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Model Serialization using Joblib
9. Flask Integration
10. Web Deployment

---

## Project Structure

```text
Sales_Deal_Size_Prediction/
│
├── dataset/
│   └── clean_sales_data.csv
│
├── model/
│   ├── train_model.py
│   ├── dealsize_model.pkl
│   ├── target_encoder.pkl
│   └── feature_columns.pkl
│
├── static/
│   └── css/
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## How to Run

### Clone the Repository

```bash
git clone <repository-url>
```

### Train the Model

```bash
python model/train_model.py
```

### Run the Flask Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Model Used

* Random Forest Classifier

The model is trained using selected features from the sales dataset to classify the deal size into:

* Small
* Medium
* Large

---

## Future Enhancements

* Interactive analytics dashboard
* Sales forecasting
* Customer segmentation
* Product recommendation system
* Deployment on Render
* User authentication
* Export prediction reports

---

## Learning Outcomes

Through this project, the following concepts were implemented:

* Data Cleaning
* Exploratory Data Analysis
* SQL Analysis
* Feature Engineering
* Machine Learning Classification
* Model Evaluation
* Flask Web Development
* Model Deployment

---

## Author

**Srikanth**

B.Tech – Computer Science and Engineering (AI & ML)

Passionate about Machine Learning, Data Analytics, and Full Stack Development.
