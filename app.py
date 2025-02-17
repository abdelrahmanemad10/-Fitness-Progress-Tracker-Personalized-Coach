import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# App Title
st.title('Fitness Progress Tracker & Personalized Coach')

# Sidebar for navigation
st.sidebar.header('User Info')
user_goal = st.sidebar.selectbox("Select Your Goal", ["Build Muscle", "Lose Fat", "Increase Strength"])
workout_type = st.sidebar.selectbox("Select Workout Type", ["Home Gym", "Gym Equipment"])

# Workout Log
st.header('Log Your Workout')
exercise_name = st.text_input("Enter Exercise Name")
sets = st.number_input("Number of Sets", min_value=1, max_value=10, value=3)
reps = st.number_input("Number of Reps per Set", min_value=1, max_value=20, value=8)
weight = st.number_input("Weight Used (kg)", min_value=1, max_value=100, value=20)

# Log the data into a DataFrame
if st.button("Log Workout"):
    workout_data = pd.DataFrame([[exercise_name, sets, reps, weight]], columns=["Exercise", "Sets", "Reps", "Weight"])
    st.write(workout_data)

# AI Insights & Suggestions
st.header('AI Insights & Workout Suggestions')
st.write("Here, you will get suggestions based on your progress.")
# Example: Show personalized suggestions
if user_goal == "Build Muscle":
    st.write("Focus on compound exercises like squats, deadlifts, and bench press.")

# Visualize Progress (for demonstration, we use random data)
st.header('Progress Visualization')
data = pd.DataFrame(np.random.randn(100, 2), columns=['Week', 'Strength'])
sns.lineplot(data=data, x="Week", y="Strength")
st.pyplot()

# Display Progress Graph
st.header('Progress Graph')
st.line_chart(data['Strength'])

# AI Model to Recommend Plan (Simple Example with Linear Regression)
st.header('AI-Powered Personalized Plan')
X = np.array([[1, 2], [2, 4], [3, 6], [4, 8], [5, 10]])  # Sample Data: Week vs Strength
y = np.array([1, 2, 3, 4, 5])  # Simple Strength Progression

model = LinearRegression().fit(X, y)
predicted_strength = model.predict([[6, 12]])  # Example: Week 6, Workout Progress

st.write(f"Predicted strength for week 6: {predicted_strength[0]:.2f}")

