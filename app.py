import streamlit as st
import time

st.set_page_config(page_title="Ramadan Gym Planner", page_icon="🌙", layout="wide")

def loading_animation():
    with st.spinner("Loading your personalized Ramadan fitness plan..."):
        time.sleep(2)

def main():
    loading_animation()
    
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
        }
        .stVideo {
            border-radius: 10px;
        }
        .section {
            background-color: #1E1E1E;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0px 0px 10px rgba(255, 215, 0, 0.2);
        }
        </style>
        """, unsafe_allow_html=True
    )
    
    st.markdown("<h1 class='stTitle'>🌙🏋️ Ramadan Gym Planner</h1>", unsafe_allow_html=True)
    st.write("Stay fit and maintain muscle mass during Ramadan with a structured workout plan!")
    
    # Select workout days
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("🗓️ Choose Your Workout Days")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    selected_days = st.multiselect("Select the days you plan to work out:", days, default=["Monday", "Wednesday", "Saturday"])
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Workout Plan
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("💪 Workout Plan")
    if selected_days:
        for day in selected_days:
            st.subheader(f"📅 {day}")
            if day in ["Monday", "Thursday"]:
                st.write("**Push Day (Chest - Shoulders - Triceps)**")
                st.write("- Bench Press: 4x8-12")
                st.video("https://www.youtube.com/watch?v=rT7DgCr-3pg")
                st.write("- Incline Dumbbell Press: 3x10-12")
                st.video("https://www.youtube.com/watch?v=8iPEnn-ltC8")
                st.write("- Lateral Raises: 3x12-15")
                st.video("https://www.youtube.com/watch?v=kDqklk1ZESo")
                st.write("- Shoulder Press: 3x8-12")
                st.video("https://www.youtube.com/watch?v=qEwKCR5JCog")
                st.write("- Triceps Cable Pushdown: 3x12-15")
                st.video("https://www.youtube.com/watch?v=vB5OHsJ3EME")
            elif day in ["Tuesday", "Saturday"]:
                st.write("**Pull Day (Back - Biceps - Traps)**")
                st.write("- Lat Pulldown: 4x8-12")
                st.video("https://www.youtube.com/watch?v=CAwf7n6Luuc")
                st.write("- Dumbbell Rows: 3x10-12")
                st.video("https://www.youtube.com/watch?v=pYcpY20QaE8")
                st.write("- Seated Row: 3x12-15")
                st.video("https://www.youtube.com/watch?v=GZbfZ033f74")
                st.write("- Barbell Biceps Curl: 3x10-12")
                st.video("https://www.youtube.com/watch?v=kwG2ipFRgfo")
                st.write("- Dumbbell Shrugs: 3x12-15")
                st.video("https://www.youtube.com/watch?v=V0BhRkGhxH8")
            elif day in ["Wednesday", "Sunday"]:
                st.write("**Legs & Core Day**")
                st.write("- Squats: 4x8-12")
                st.video("https://www.youtube.com/watch?v=ultWZbUMPL8")
                st.write("- Leg Extension: 3x12-15")
                st.video("https://www.youtube.com/watch?v=yMzTlKjYPK8")
                st.write("- Leg Curl: 3x12-15")
                st.video("https://www.youtube.com/watch?v=1Tq3QdYUuHs")
                st.write("- Calf Raises: 3x12-15")
                st.video("https://www.youtube.com/watch?v=-M4-G8p8fmc")
                st.write("- Plank + Core Work: 3 sets")
                st.video("https://www.youtube.com/watch?v=pSHjTRCQxIw")
            else:
                st.write("Active Rest / Cardio")
                st.write("- Walking 30 minutes")
                st.write("- Stretching / Yoga")
    else:
        st.write("⚠️ Please select at least one workout day.")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Nutrition Tips
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("🍽️ Nutrition Tips for Ramadan")
    st.write("- **Suhoor:** Eat slow-digesting protein (yogurt, nuts, oats) to stay full longer.")
    st.write("- **Iftar:** Break fast with dates and water, then have a balanced meal with protein, carbs, and healthy fats.")
    st.write("- **Hydration:** Drink 2-3 liters of water between Iftar and Suhoor.")
    st.write("- **Supplements:** Consider BCAAs during workouts and creatine post-workout.")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.success("💡 Stay consistent and make the most of Ramadan while keeping your gains!")

if __name__ == "__main__":
    main()
