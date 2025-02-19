import streamlit as st
import time

# Set page configuration
st.set_page_config(page_title="Ramadan Gym Planner", page_icon="🌙", layout="wide")

# Custom CSS for improved UI
st.markdown(
    """
    <style>
    .stApp {
        background-color: #121212;
        color: #FFD700;
        font-family: 'Arial', sans-serif;
    }
    .stTitle {
        text-align: center;
        font-size: 2.5em;
        font-weight: bold;
        color: #FFA500;
    }
    .stHeader {
        color: #FFD700;
        font-size: 1.8em;
        margin-bottom: 10px;
    }
    .stSubheader {
        color: #FFD700;
        font-size: 1.4em;
        margin-bottom: 10px;
    }
    .stVideo {
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .section {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0px 0px 10px rgba(255, 215, 0, 0.2);
    }
    .sidebar .sidebar-content {
        background-color: #1E1E1E;
        color: #FFD700;
    }
    .stButton>button {
        background-color: #FFA500;
        color: #121212;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 20px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Loading animation
def loading_animation():
    with st.spinner("Loading your personalized Ramadan fitness plan..."):
        time.sleep(2)

# Main function
def main():
    loading_animation()
    
    # Sidebar for navigation
    with st.sidebar:
        st.markdown("## 🌙 Navigation")
        page = st.radio("Go to", ["🏋️ Workout Plan", "⚖️ Weight Tracker", "🍽️ Nutrition Plan"])
    
    # Main content
    st.markdown("<h1 class='stTitle'>🌙🏋️ Ramadan Gym Planner</h1>", unsafe_allow_html=True)
    st.write("Stay fit and maintain muscle mass during Ramadan with a structured workout plan!")
    
    if page == "⚖️ Weight Tracker":
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.markdown("<h2 class='stHeader'>⚖️ Weight Tracker</h2>", unsafe_allow_html=True)
        weight = st.number_input("Enter your current weight (kg):", min_value=30, max_value=200, value=70)
        st.write(f"Your recorded weight: **{weight} kg**")
        st.markdown("</div>", unsafe_allow_html=True)
    
    elif page == "🏋️ Workout Plan":
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.markdown("<h2 class='stHeader'>🗓️ Choose Your Workout Days</h2>", unsafe_allow_html=True)
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        selected_days = st.multiselect("Select the days you plan to work out:", days, default=["Monday", "Wednesday", "Saturday"])
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.markdown("<h2 class='stHeader'>🏋️ Filter by Workout Type</h2>", unsafe_allow_html=True)
        workout_types = ["All", "Push (Chest, Shoulders, Triceps)", "Pull (Back, Biceps, Traps)", "Legs & Core"]
        selected_type = st.selectbox("Select workout type:", workout_types, index=0)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.markdown("<h2 class='stHeader'>💪 Workout Plan</h2>", unsafe_allow_html=True)
        if selected_days:
            for day in selected_days:
                st.markdown(f"<h3 class='stSubheader'>📅 {day}</h3>", unsafe_allow_html=True)
                if day in ["Monday", "Thursday"] and (selected_type == "All" or selected_type == "Push (Chest, Shoulders, Triceps)"):
                    st.write("**Push Day (Chest - Shoulders - Triceps)**")
                    st.write("- Bench Press: 4x8-12")
                    st.video("https://www.youtube.com/watch?v=rT7DgCr-3pg")
                    st.write("- Incline Dumbbell Press: 3x10-12")
                    st.video("https://www.youtube.com/watch?v=8iPEnn-ltC8")
                    st.write("- Lateral Raises: 3x12-15")
                    st.video("https://www.youtube.com/watch?v=kDqklk1ZESo")
                elif day in ["Tuesday", "Saturday"] and (selected_type == "All" or selected_type == "Pull (Back, Biceps, Traps)"):
                    st.write("**Pull Day (Back - Biceps - Traps)**")
                    st.write("- Lat Pulldown: 4x8-12")
                    st.video("https://www.youtube.com/watch?v=CAwf7n6Luuc")
                    st.write("- Dumbbell Rows: 3x10-12")
                    st.video("https://www.youtube.com/watch?v=pYcpY20QaE8")
                elif day in ["Wednesday", "Sunday"] and (selected_type == "All" or selected_type == "Legs & Core"):
                    st.write("**Legs & Core Day**")
                    st.write("- Squats: 4x8-12")
                    st.video("https://www.youtube.com/watch?v=ultWZbUMPL8")
                    st.write("- Leg Extension: 3x12-15")
                    st.video("https://www.youtube.com/watch?v=yMzTlKjYPK8")
                else:
                    st.write("Active Rest / Cardio")
                    st.write("- Walking 30 minutes")
                    st.write("- Stretching / Yoga")
        else:
            st.write("⚠️ Please select at least one workout day.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    elif page == "🍽️ Nutrition Plan":
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.markdown("<h2 class='stHeader'>🍽️ Bulking Nutrition Plan for Ramadan</h2>", unsafe_allow_html=True)
        st.write("**Iftar:** Dates, water, high-protein meal with rice and vegetables.")
        st.write("**Post-Iftar Meal:** Protein-rich meal (chicken, beef, or fish) with complex carbs.")
        st.write("**Pre-Workout Snack:** Oats, peanut butter, and honey.")
        st.write("**Post-Workout Meal:** Protein shake, fruits, and a balanced dinner.")
        st.write("**Suhoor:** Slow-digesting protein (Greek yogurt, casein), oats, and healthy fats.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.success("💡 Stay consistent and make the most of Ramadan while keeping your gains!")

if __name__ == "__main__":
    main()
