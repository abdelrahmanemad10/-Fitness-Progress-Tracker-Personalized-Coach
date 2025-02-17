import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Check if Firebase is already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase-credentials.json")  # Replace with your actual JSON key file
    firebase_admin.initialize_app(cred)

# Firestore Setup
db = firestore.client()

# Streamlit App
st.title("Fitness Progress Tracker & Personalized Coach")

# User Authentication Placeholder
st.sidebar.subheader("User Authentication")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")
login_button = st.sidebar.button("Login")

# If login button is clicked (Authentication Logic Needed)
if login_button:
    st.sidebar.success(f"Logged in as {username}")

# User Dashboard
st.header("Track Your Progress")

# User Data Input
st.subheader("Enter Workout Data")
exercise = st.text_input("Exercise Name")
weight = st.number_input("Weight Used (kg)", min_value=0.0, step=0.5)
sets = st.number_input("Number of Sets", min_value=1, step=1)
reps = st.number_input("Reps per Set", min_value=1, step=1)
submit_button = st.button("Save Workout")

if submit_button:
    workout_data = {
        "exercise": exercise,
        "weight": weight,
        "sets": sets,
        "reps": reps
    }
    db.collection("workouts").add(workout_data)
    st.success("Workout data saved successfully!")

# Retrieve and Display Data
st.subheader("Workout History")
workouts = db.collection("workouts").stream()
for workout in workouts:
    data = workout.to_dict()
    st.write(f"**{data['exercise']}** - {data['weight']} kg, {data['sets']} sets x {data['reps']} reps")
