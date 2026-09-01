# 🏠 House Price Prediction using AWS & Machine Learning

## 📌 Project Overview

This project is a Machine Learning based House Price Prediction application.

The user enters house details such as area, number of bedrooms, bathrooms, stories, parking, and other features through a web interface. The request is sent to an AWS API, processed by AWS Lambda, and the trained Machine Learning model hosted on Amazon SageMaker predicts the house price.

The predicted price is then displayed on the frontend.

---

## 🚀 Features

- House price prediction using Machine Learning
- Interactive web frontend
- REST API using Amazon API Gateway
- Serverless backend using AWS Lambda
- ML model deployed on Amazon SageMaker
- Data storage using Amazon S3
- ETL/data processing using AWS Lambda
- CORS configured for frontend API communication
- Real-time prediction through the deployed endpoint

---

## 🛠️ Technologies Used

### Programming
- Python
- HTML
- CSS
- JavaScript

### Machine Learning
- Pandas
- NumPy
- Scikit-learn
- XGBoost

### AWS Services
- Amazon S3
- AWS Lambda
- Amazon SageMaker
- Amazon API Gateway
- AWS IAM

---

## 🏗️ Architecture

```text
                 ┌─────────────────┐
                 │    Frontend     │
                 │ HTML/CSS/JS     │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │  API Gateway    │
                 │   POST /predict │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │  AWS Lambda     │
                 │ Backend/API     │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Amazon          │
                 │ SageMaker       │
                 │ Endpoint        │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ XGBoost Model   │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Predicted Price │
                 └─────────────────┘

📊 Input Features
The model uses the following house features:
Feature
Description
Area
Area of the house
Bedrooms
Number of bedrooms
Bathrooms
Number of bathrooms
Stories
Number of stories
Parking
Number of parking spaces
Main Road
Whether the house is connected to the main road
Guest Room
Whether a guest room is available
Basement
Whether the house has a basement
Hot Water Heating
Whether hot water heating is available
Air Conditioning
Whether air conditioning is available
Furnishing Status
Furnishing condition of the house

🔄 Project Workflow
1. Data Storage
The dataset is stored in Amazon S3.
2. Data Processing
AWS Lambda is used for processing/ETL operations and preparing the data for Machine Learning.
3. Model Training
The processed dataset is used to train an XGBoost Machine Learning model.
4. Model Deployment
The trained model is deployed as an Amazon SageMaker endpoint.
5. Backend
AWS Lambda receives prediction requests from API Gateway and invokes the SageMaker endpoint.
6. API
Amazon API Gateway exposes the /predict POST endpoint.
7. Frontend
The frontend collects house information and sends it to the API.
8. Prediction
The model returns the predicted house price, which is displayed on the webpage.

🧪 Example Prediction
Example input:
Area: 7420
Bedrooms: 4
Bathrooms: 2
Stories: 3
Parking: 2
Main Road: Yes
Guest Room: No
Basement: No
Hot Water Heating: No
Air Conditioning: Yes
Furnishing Status: Furnished

Example output:
Predicted Price: ₹1,08,14,315


📁 Project Structure
house-price-prediction-aws/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── lambda/
│   └── backend code
│
├── README.md
└── .gitignore


⚙️ API Request Example
The frontend sends a POST request to:
/predict


Example JSON:
{
  "area": 7420,
  "bedrooms": 4,
  "bathrooms": 2,
  "stories": 3,
  "parking": 2,
  "mainroad": 1,
  "guestroom": 0,
  "basement": 0,
  "hotwaterheating": 0,
  "airconditioning": 1,
  "furnishingstatus": 2
}
Example response:
{
  "success": true,
  "predicted_price": 10814315
}


🔐 Security
AWS IAM is used to control permissions between AWS services.
Sensitive information such as:
AWS Access Keys
Secret Access Keys
.env files
Private keys
should never be committed to GitHub.


📈 Future Improvements
Improve model accuracy through hyperparameter tuning
Add more housing features
Add authentication
Add prediction history
Add database storage
Add model monitoring
Add CI/CD pipeline
Use HTTPS with a custom domain
Add charts and analytics to the frontend

👨‍💻 Author
Aditya Rao

Skills demonstrated
Python
Machine Learning
XGBoost
AWS
Amazon SageMaker
AWS Lambda
API Gateway
Amazon S3
HTML
CSS
JavaScript

⭐ Project Summary

This project demonstrates how a Machine Learning model can be integrated with AWS cloud services and a web application to create an end-to-end cloud-based prediction system.
