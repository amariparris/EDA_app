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

    def save_uploaded_file(uploadedfile):
        with open(os.path.join('data','Main.csv'),'wb') as f:
            f.write(uploadedfile.getbuffer())
            
    #make df global variable
    global df
    df = None
    #save file
    if uploaded_file is not None:
        save_uploaded_file(uploaded_file)
