import streamlit as st
import numpy as np
import joblib

# --------------------------------------------------
# Load trained model
# --------------------------------------------------

model = joblib.load("linear_regressor.pkl")


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="IPL Score Predictor",
    page_icon="🏏",
    layout="centered"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🏏 IPL Score Predictor")
st.write("Predict the final IPL score using current match statistics.")


# --------------------------------------------------
# Teams
# --------------------------------------------------

teams = [
    "Chennai Super Kings",
    "Delhi Daredevils",
    "Kings XI Punjab",
    "Kolkata Knight Riders",
    "Mumbai Indians",
    "Rajasthan Royals",
    "Royal Challengers Bangalore",
    "Sunrisers Hyderabad"
]


# --------------------------------------------------
# Team encoding
# --------------------------------------------------

def encode_team(team):

    if team == "Chennai Super Kings":
        return [1, 0, 0, 0, 0, 0, 0, 0]

    elif team == "Delhi Daredevils":
        return [0, 1, 0, 0, 0, 0, 0, 0]

    elif team == "Kings XI Punjab":
        return [0, 0, 1, 0, 0, 0, 0, 0]

    elif team == "Kolkata Knight Riders":
        return [0, 0, 0, 1, 0, 0, 0, 0]

    elif team == "Mumbai Indians":
        return [0, 0, 0, 0, 1, 0, 0, 0]

    elif team == "Rajasthan Royals":
        return [0, 0, 0, 0, 0, 1, 0, 0]

    elif team == "Royal Challengers Bangalore":
        return [0, 0, 0, 0, 0, 0, 1, 0]

    elif team == "Sunrisers Hyderabad":
        return [0, 0, 0, 0, 0, 0, 0, 1]


# --------------------------------------------------
# Prediction function
# --------------------------------------------------

def predict_score(
    batting_team,
    bowling_team,
    overs,
    runs,
    wickets,
    runs_in_prev_5,
    wickets_in_prev_5
):

    temp_array = []

    # Batting team
    temp_array += encode_team(batting_team)

    # Bowling team
    temp_array += encode_team(bowling_team)

    # Match statistics
    temp_array += [
        overs,
        runs,
        wickets,
        runs_in_prev_5,
        wickets_in_prev_5
    ]

    # Convert to numpy array
    temp_array = np.array([temp_array])

    # Prediction
    prediction = model.predict(temp_array)[0]

    return int(prediction)


# --------------------------------------------------
# UI
# --------------------------------------------------

st.subheader("🏏 Match Details")

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox(
        "Batting Team",
        teams
    )

with col2:
    bowling_team = st.selectbox(
        "Bowling Team",
        teams,
        index=4
    )


st.subheader("📊 Current Match Statistics")

col1, col2 = st.columns(2)

with col1:
    overs = st.number_input(
        "Overs Completed",
        min_value=0.0,
        max_value=20.0,
        value=5.0,
        step=0.1
    )

with col2:
    runs = st.number_input(
        "Current Runs",
        min_value=0,
        max_value=300,
        value=50,
        step=1
    )

col1, col2 = st.columns(2)

with col1:
    wickets = st.number_input(
        "Wickets Fallen",
        min_value=0,
        max_value=10,
        value=0,
        step=1
    )

with col2:
    runs_in_prev_5 = st.number_input(
        "Runs in Previous 5 Overs",
        min_value=0,
        max_value=100,
        value=40,
        step=1
    )

wickets_in_prev_5 = st.number_input(
    "Wickets in Previous 5 Overs",
    min_value=0,
    max_value=10,
    value=0,
    step=1
)


# --------------------------------------------------
# Prediction button
# --------------------------------------------------

st.write("")

if st.button("🔮 Predict Final Score", use_container_width=True):

    if batting_team == bowling_team:

        st.error("Batting Team and Bowling Team cannot be the same.")

    elif wickets > 10:

        st.error("Wickets cannot be greater than 10.")

    elif overs == 20 and runs == 0:

        st.warning("Please enter valid current match statistics.")

    else:

        prediction = predict_score(
            batting_team,
            bowling_team,
            overs,
            runs,
            wickets,
            runs_in_prev_5,
            wickets_in_prev_5
        )

        st.success("Prediction generated successfully!")

        st.metric(
            label="🏏 Predicted Final Score",
            value=f"{prediction} Runs"
        )

        st.info(
            f"{batting_team} is predicted to score approximately "
            f"{prediction} runs."
        )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption("IPL Score Prediction using Machine Learning")