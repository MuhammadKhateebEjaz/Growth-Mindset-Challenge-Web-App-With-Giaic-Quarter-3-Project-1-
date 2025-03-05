#streamlit
# Imports

import streamlit as st
import pandas as pd
import os
from io import BytesIO

#set up our App


st.set_page_config(page_title="Data sweeper", layout="wide")

#custom css
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Data Sweeper")
st.write("Transfrom your filesbetween CSV and Excel fromats with build-in data cleaning and visualization!")