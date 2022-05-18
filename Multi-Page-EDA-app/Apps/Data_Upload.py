import streamlit as st 
import pandas as pd
import os

def app():
    # File uploader page 
    st.header('Data Upload')

    st.write('This is the `Data Uploader` tab of the Data Explorer app.')

    st.write('Please upload a dataset to explore')

    #add data uploader 
    uploaded_file = st.file_uploader(label = 'Upload CSV or Excel', type = ['csv', 'xlsx'], accept_multiple_files=False)

    #make df global variable
    global df
    df = None
    #create dataframe
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e: 
            df = pd.read_excel(uploaded_file)
    try:
        df.to_csv('data/main_data.csv', index=False)
    except Exception as e: 
        pass