import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the insurance data
insurance_data = pd.read_csv("C:\\Users\\varun\Downloads\\insurance.csv")

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(insurance_data[['age', 'bmi', 'children']], insurance_data['charges'])

# Set the page title
st.title("Health Insurance Cost Prediction")

# Create input fields
age = st.slider("Age", min_value=0, max_value=100, value=30)
Sex = st.selectbox('Select sex', ('Male', 'Female'))
st.write('Selected sex:', Sex)
bmi = st.number_input("BMI", min_value=10, max_value=50, value=25)
children = st.slider("Children", min_value=0, max_value=10, value=0)
Region = st.selectbox('Select region', ('Southwest', 'Southeast', 'Nortwest', 'Northeast'))
st.write('Selected Region:', Region)

# Predict the cost
predicted_cost = model.predict([[age, bmi, children]])

# Display the predicted cost
st.subheader("Prediction Result")
st.write(f"The predicted cost is: ${predicted_cost[0]:.2f}")