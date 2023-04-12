import numpy as np
import pandas as pd
import pickle
import streamlit as st
import json
import math
import base64

result = None

with open(
        r"mumbai.pickle",
        'rb') as f:
    __model = pickle.load(f)

with open(r"columns.json", 'r') as obj:
    __data_columns = json.load(obj)["data_columns"]
    __locations = __data_columns[8:]

def get_predicted_price(location, sqft, BHK, car_parking, swimming_pool):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError as e:
        loc_index = -1

    lis = np.zeros(len(__data_columns))
    lis[0] = sqft
    lis[1] = BHK
    lis[2] = car_parking
    lis[3] = swimming_pool
  

    if loc_index >= 0:
        lis[loc_index] = 1

    price = round(__model.predict([lis])[0], 2)
    strp = ' lakhs'

    if math.log10(price) >= 2:
        price = price / 100
        price = round(price, 2)
        strp = " crores"

    return str(price) + strp


def main():
    global result
    st.title("Mumbai House Price Predictor")
    html_temp = """
           <div>
           <h2>House Price Prediction ML application</h2>
           </div>
           """
    st.markdown(html_temp, unsafe_allow_html=True)
    total_sqft = st.text_input("Area")
    BHK = st.text_input("BHK")
    car_parking = st.selectbox("Parking", [0, 1])
    swimming_pool = st.selectbox("Swimming Pool", [0, 1])
    location = st.selectbox("Location", __locations)


    if st.button("Predict"):
        result = get_predicted_price(location, total_sqft, BHK, car_parking, swimming_pool)

    st.markdown("<hr>", unsafe_allow_html=True)
    if result:
        st.success(f"Estimated price for a {BHK} BHK property in {location} with a total area of {total_sqft} sqft is {result}.")
    else:
        st.warning("Please enter the details and click on 'Predict' button to get the estimated price.")


if __name__ == "__main__":
    main()
