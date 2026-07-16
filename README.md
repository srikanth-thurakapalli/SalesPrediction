# 📈 Sales Prediction System Using Machine Learning

## Overview

The **Sales Prediction System Using Machine Learning** is a Django-based web application that predicts the expected sales value for a customer order using a Machine Learning regression model. The system is trained on the **Sample Superstore** dataset and provides real-time sales predictions based on order details entered by the user.

This project demonstrates the integration of **Machine Learning**, **Data Preprocessing**, and **Django Web Development** to build an intelligent business application.

---

## Problem Statement

Businesses process thousands of customer orders every day. Predicting the expected sales value before processing an order can help improve business planning and decision-making. Since sales depend on multiple factors such as product category, customer segment, location, shipping mode, quantity, and discount, manual estimation is difficult.

This project uses Machine Learning to predict the expected sales amount from historical sales data.

---

## Objectives

* Develop a Machine Learning model to predict sales values.
* Perform data preprocessing and feature engineering.
* Build a Django web application for real-time sales prediction.
* Integrate the trained ML model with the web interface.
* Provide a simple and interactive user experience.

---

## Features

* Predict sales using historical order data.
* User-friendly web interface built with Django.
* Machine Learning model integration.
* Real-time prediction results.
* Clean and responsive interface.
* Easy to extend and deploy.

---

## Dataset

The project uses the **Sample Superstore** dataset.

### Input Features

* Category
* Sub Category
* Region
* State
* City
* Segment
* Ship Mode
* Quantity
* Discount

### Target Variable

* Sales

---

## Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Pandas
* NumPy
* Joblib

### Web Development

* Django
* HTML
* CSS
* JavaScript

### Database

* SQLite

### Development Tools

* Visual Studio Code
* Jupyter Notebook
* Git
* GitHub

---

## Machine Learning Workflow

1. Load the Sample Superstore dataset.
2. Clean and preprocess the data.
3. Encode categorical features.
4. Scale numerical features (if required).
5. Split the dataset into training and testing sets.
6. Train the regression model.
7. Save the trained pipeline and preprocessing objects.
8. Integrate the model into the Django application.
9. Predict sales based on user inputs.

---

## Project Structure

```text
Sales_Prediction_System/
│
├── dataset/
│   └── SampleSuperstore.csv
│
├── ml/
│   ├── train.py
│   ├── predict.py
│   └── pipeline.pkl
│
├── model/
│   ├── encoder.pkl
│   └── scaler.pkl
│
├── predictor/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   ├── admin.py
│   ├── tests.py
│   └── __init__.py
│
├── SalesPrediction/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── __init__.py
│
├── templates/
│   └── predict.html
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Sales_Prediction_System.git
```

### 2. Navigate to the Project Folder

```bash
cd Sales_Prediction_System
```

### 3. Run the Django Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## How the System Works

1. The user enters order details through the Django web interface.
2. Django receives the request and passes the input to the prediction module.
3. The preprocessing pipeline transforms the input into the format expected by the trained model.
4. The Machine Learning model predicts the sales value.
5. The predicted sales amount is displayed on the webpage.

---

## Machine Learning Model

* **Problem Type:** Regression
* **Target Variable:** Sales
* **Input Variables:** Category, Sub Category, Region, State, City, Segment, Ship Mode, Quantity, and Discount.

**Evaluation Metrics**

* R² Score
* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

---

## Application Screenshots

Include screenshots of:

* Home Page
* Sales Prediction Form
* Prediction Result

---

## Future Enhancements

* Interactive sales analytics dashboard.
* User authentication and role management.
* Prediction history storage.
* Cloud deployment.
* REST API integration.
* Sales trend visualization.
* Support for multiple machine learning models.

---

## Learning Outcomes

This project helped in understanding:

* Data preprocessing techniques.
* Feature encoding and transformation.
* Machine Learning regression.
* Model serialization and deployment.
* Django web development.
* Integration of Machine Learning with web applications.

---

## Author

**Srikanth**

B.Tech – Computer Science and Engineering (Artificial Intelligence & Machine Learning)

**Skills:** Python, Django, Machine Learning, SQL, HTML, CSS, JavaScript

---

## License

This project is developed for academic and learning purposes.
