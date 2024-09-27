# Zameen.com House Price Prediction Streamlit App

![streamlit_app](https://github.com/user-attachments/assets/68fd4de6-02b5-414b-adc9-0d5043e08c06)

## **a. Introduction**
This project aims to predict housing prices using a dataset scraped from Zameen.com, one of Pakistan’s most popular real estate platforms. The dataset includes important features like:

- Area (in square feet)
- Number of bedrooms
- Number of bathrooms
- Listed price of the properties
  
## **b. Objective**
The main goal is to build a machine learning model that can accurately predict housing prices based on these features.

## **c. Key Steps in the Workflow**

#### 1. Data Cleaning
Rows with missing values are removed to maintain data quality.<br />
Outliers are detected and addressed to prevent skewed predictions.

#### 2. Feature Engineering
The number of bedrooms and bathrooms are combined to create a single feature, improving model performance by reducing redundancy.

#### 3. Exploratory Data Analysis
Correlations between features are examined to identify any multicollinearity, ensuring that features don’t distort model training.

#### 4. Modeling
The dataset is split into training and testing sets. A log transformation is applied on the target variable (price in rupees)<br />
A pipeline is designed, including standardization of data.

#### 6. Model Optimization
Grid search is employed to fine-tune hyperparameters and find the best values for maximizing the model's predictive performance.

## d. Tools and Libraries Used
[Libraries used (with versions)](https://github.com/Maheer24/Zameen-com-House-Price-Prediction-Streamlit/blob/main/requirements.txt)

## e. The Streamlit App
To make the model accessible and user-friendly, a [Streamlit app](https://maheer24-zameen-com-house-price-prediction-streamlit-app-xxvb6v.streamlit.app/) has been built. Users can input property details (like area, number of bedrooms, and bathrooms) and get an estimated price for the property in real-time.

#### **How to Run the App?**

- Clone the repository.<br />
- Install the required dependencies listed in requirements.txt.

- Run the Streamlit app using the command:
`streamlit run streamlit_app.py`
