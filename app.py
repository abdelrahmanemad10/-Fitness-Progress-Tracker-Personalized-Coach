import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Initialize Firebase Admin SDK
cred = credentials.Certificate("firebase-credentials.json")  # Replace with your Firebase credentials path
firebase_admin.initialize_app(cred)

# Firestore Setup
db = firestore.client()

# Function to authenticate the user
def authenticate_user():
    option = st.sidebar.selectbox("Select Action", ["Login", "Sign Up"])
    if option == "Login":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            # Check credentials (Firebase logic to check the username/password)
            # If valid, return True (you can implement logic here)
            st.success("Login successful!")
            return True
    elif option == "Sign Up":
        username = st.text_input("Create Username")
        password = st.text_input("Create Password", type="password")
        if st.button("Sign Up"):
            # Save user to Firebase (you can add logic for Firebase signup here)
            st.success("Signup successful!")
            return True

# User Authentication
if authenticate_user():
    st.title("Fitness Progress Tracker & Personalized Coach")

    # Input: Log workout details
    st.header("Log Your Workout")
    exercise_type = st.selectbox("Exercise Type", ["Squat", "Bench Press", "Deadlift", "Biceps Curl", "Other"])
    weight = st.number_input("Weight (kg)", min_value=0, step=1)
    reps = st.number_input("Reps", min_value=0, step=1)

    # Store workout data in Firestore
    if st.button("Log Workout"):
        workout_data = {
            "exercise_type": exercise_type,
            "weight": weight,
            "reps": reps,
            "timestamp": firestore.SERVER_TIMESTAMP
        }
        db.collection("workouts").add(workout_data)
        st.success("Workout logged successfully!")

    # Display progress (retrieve and show workouts)
    st.header("Your Progress")
    workouts_ref = db.collection("workouts").stream()
    workout_data_list = []
    for workout in workouts_ref:
        workout_data = workout.to_dict()
        workout_data_list.append(workout_data)

    # Display workouts in a table
    if workout_data_list:
        df = pd.DataFrame(workout_data_list)
        st.dataframe(df)

        # Progress visualization (simple example: average weight lifted)
        st.subheader("Your Progress Over Time")
        avg_weight = df.groupby("exercise_type")["weight"].mean()
        st.bar_chart(avg_weight)

    # Personalized coach (AI-based or static recommendations)
    st.header("Personalized Recommendations")
    st.write("Based on your progress, here are some personalized suggestions:")
    # You can add AI-driven logic here to give recommendations, such as:
    st.write("1. Increase reps for Biceps Curl.")
    st.write("2. Try adding more weight to your Deadlift.")

# Debugging: Display Firebase data on the app
if st.button("Show All Workouts"):
    workouts_ref = db.collection("workouts").stream()
    for workout in workouts_ref:
        st.write(workout.to_dict())
