import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(
    page_title="Gym AI",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# -------------------------------
# HERO
# -------------------------------

st.markdown("""
<div class='hero'>

<h1>🏋️ Gym AI Predictor</h1>

<p>
Track • Predict • Improve
</p>

</div>
""", unsafe_allow_html=True)

# -------------------------------
# SIDEBAR
# -------------------------------

st.sidebar.image(
"https://cdn-icons-png.flaticon.com/512/2936/2936886.png",
width=120)

st.sidebar.title("⚙ User Details")

age = st.sidebar.slider("Age",18,70,25)
weight = st.sidebar.slider("Weight (kg)",40,150,70)
height = st.sidebar.slider("Height (cm)",140,210,170)

gender = st.sidebar.selectbox(
"Gender",
["Male","Female"]
)

workout = st.sidebar.slider(
"Workout Days",
1,
7,
4
)

water = st.sidebar.slider(
"Water Intake (L)",
1,
6,
3
)

sleep = st.sidebar.slider(
"Sleep Hours",
4,
10,
7
)

# -------------------------------
# METRICS
# -------------------------------

col1,col2,col3,col4=st.columns(4)

bmi=weight/((height/100)**2)

with col1:
    st.metric("BMI",round(bmi,1))

with col2:
    st.metric("Workout Days",workout)

with col3:
    st.metric("Sleep",f"{sleep} hrs")

with col4:
    st.metric("Water",f"{water} L")

st.markdown("---")

# -------------------------------
# INPUT SECTION
# -------------------------------

left,right=st.columns([2,1])

with left:

    st.markdown("## 💪 Member Information")

    calories=st.number_input(
        "Calories Intake",
        1000,
        6000,
        2500
    )

    heart_rate=st.slider(
        "Heart Rate",
        50,
        180,
        95
    )

    steps=st.slider(
        "Daily Steps",
        1000,
        30000,
        9000
    )

with right:

    fig=go.Figure(go.Indicator(
        mode="gauge+number",
        value=bmi,
        title={'text':"BMI"},
        gauge={
            'axis':{'range':[10,40]},
            'bar':{'color':"#ff4b4b"},
            'steps':[
                {'range':[10,18.5],'color':'#4dabf7'},
                {'range':[18.5,25],'color':'#51cf66'},
                {'range':[25,40],'color':'#ff922b'}
            ]
        }
    ))

    fig.update_layout(height=320)

    st.plotly_chart(fig,use_container_width=True)

st.markdown("---")

# -------------------------------
# Prediction
# -------------------------------

if st.button("🚀 Predict Performance"):

    with st.spinner("Analyzing your fitness..."):

        st.success("Prediction Complete!")

        st.markdown(f"""

<div class='prediction'>

<h2>🔥 Excellent Fitness Score</h2>

<h1>{88}%</h1>

<p>
Keep maintaining your consistency.
</p>

</div>

""",unsafe_allow_html=True)

# -------------------------------
# Charts
# -------------------------------

st.markdown("## 📊 Fitness Analytics")

df=pd.read_csv("gym_members_exercise_tracking.csv")

col1,col2=st.columns(2)

with col1:

    fig=px.histogram(
        df,
        x="Age",
        color="Gender",
        template="plotly_dark"
    )

    st.plotly_chart(fig,use_container_width=True)

with col2:

    fig = px.scatter(
    df,
    x="Age",
    y="Calories_Burned",
    color="Workout_Type",
    template="plotly_dark"
)

    st.plotly_chart(fig,use_container_width=True)

# -------------------------------
# Recommendation Cards
# -------------------------------

st.markdown("## 🔥 AI Recommendations")

c1,c2,c3=st.columns(3)

with c1:
    st.markdown("""
<div class='card'>
🏃

### Cardio

30 min Running

⭐⭐⭐⭐⭐

</div>
""",unsafe_allow_html=True)

with c2:
    st.markdown("""
<div class='card'>
🏋️

### Strength

Push Pull Legs

⭐⭐⭐⭐⭐

</div>
""",unsafe_allow_html=True)

with c3:
    st.markdown("""
<div class='card'>
🥗

### Nutrition

High Protein Diet

⭐⭐⭐⭐⭐

</div>
""",unsafe_allow_html=True)

st.markdown("---")

st.markdown(
"<center>Made with ❤️ using Streamlit</center>",
unsafe_allow_html=True
)