import pandas as pd
import streamlit as st
import pickle
import xgboost
from xgboost import XGBRegressor

# Load data
airlines_encoded = pd.read_excel('airlines_encoded.xlsx')
source_encoded = pd.read_excel('source_encoded.xlsx')
destination_encoded = pd.read_excel('destination_encoded.xlsx')

with open('XGBR_Flight_Prices_Predictor.pkl', 'rb') as file:
    model = pickle.load(file)

def predict():
    # Taking inputs
    Airline = st.text_input("Enter Airline Name:")
    Source = st.text_input("Enter Source Location:")
    Destination = st.text_input("Enter Destination Location:")
    Total_Stops = st.number_input("Enter Total Number of Stops:", min_value=0, step=1)
    Day_of_journey = st.number_input("Enter Day of Journey:", min_value=1, max_value=31, step=1)
    Month_of_journey = st.number_input("Enter Month of Journey:", min_value=1, max_value=12, step=1)
    Departure_Hour = st.number_input("Enter Departure Hour:", min_value=0, max_value=23, step=1)
    Departure_Min = st.number_input("Enter Departure Minute:", min_value=0, max_value=59, step=1)
    Duration_hrs = st.number_input("Enter Duration in Hours:", min_value=0, step=1)
    Duration_mins = st.number_input("Enter Duration in Minutes:", min_value=0, max_value=59, step=1)
    
    if st.button("Predict Price"):
        try:
            Airline = airlines_encoded[airlines_encoded["Airline"]==Airline]["Encoding"].values[0]
            Source = source_encoded[source_encoded["Source"]==Source]["Encoding"].values[0]
            Destination = destination_encoded[destination_encoded["Destination"]==Destination]["Encoding"].values[0]

            pred = model.predict([[Airline, Source, Destination,
                                Total_Stops, Day_of_journey,
                                Month_of_journey, Departure_Hour,
                                Departure_Min, Duration_hrs,
                                Duration_mins]])
            st.write(f"Predicted Price: {pred[0]}")
        except (IndexError, KeyError):
            st.write("An Error Occured")

def main():
    st.title("Flight Prices Prediction")
    predict()

if __name__ == '__main__':
    main()