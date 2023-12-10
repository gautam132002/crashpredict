import streamlit as st
import streamlit_shadcn_ui as ui
import pandas as pd
import fetch
import hash_multiplier
import train
import train_rnn


def get_model_prediction_crashCNN():

    with st.spinner():
        hash_multiplier.main()
        prediction = train.predict_next_event()

        st.title(prediction)


def get_model_prediction_crashRNN():

    with st.spinner():
        prediction = train_rnn.predict_rnn()

        st.title(prediction)
        

def laod_game_data():

    with st.spinner():
        x = fetch.main()

        payout = x.get("payout", " ")
        target = x.get("ticket", " ")
        startedAt = x.get("startedAt", " ")
        numberOfBets = x.get("numberOfBets", " ")
        serverSeed = x.get("serverSeed", " ")
        game_id = x.get("id", " ")
        endTime = x.get("endTime", " ")


        cols = st.columns(3)
        with cols[0]:
            ui.metric_card(title="Total Payout", content=f"{payout}", description="Payout of last game", key="card1")
        with cols[1]:
            ui.metric_card(title="Game Multiplier", content=target/100, description="Crash multiplier of last Game", key="card2")
        with cols[2]:
            ui.metric_card(title="No. of Bets", content= numberOfBets, description="Bettig data of last game", key="card3")

        ui.badges(badge_list=[("game-hash", "outline"),(f"{serverSeed}", "default")], class_name="flex gap-2", key="badges1")
        


st.sidebar.title("Select Model")
selected_model = st.sidebar.selectbox("Choose a model", ["Crash CNN", "Crash RNN"])


st.title("Crash Predictor")
# st.subheader(f"Selected Model: {selected_model}")
ui.badges(badge_list=[(f"{selected_model}", "destructive")])

if ui.button("Predict Next Event", key="clk_btn"):

    st.subheader("Last Game Data")
    laod_game_data()

    st.subheader("Predicted Multiplier of Next Game")
    if selected_model == "Crash CNN":
        get_model_prediction_crashCNN()
    if selected_model == "Crash RNN":
        get_model_prediction_crashRNN()

    
else:
    st.subheader("Last Game Data")
    laod_game_data()

    st.subheader("Predicted Multiplier of Next Game")
    if selected_model == "Crash CNN":
        get_model_prediction_crashCNN()
    if selected_model == "Crash RNN":
        get_model_prediction_crashRNN()


    
    



        












