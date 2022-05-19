import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import os

def app():

    st.title('Preview Data')

    st.write('This is the `Data Filter` tool of the Data Explorer app.')

    st.write('filter through the dataset and examine columns and rows of your choosing')
    
    if 'main_data.csv' not in os.listdir('data'):
        st.markdown("Please upload data through `Upload Data` page.")
    else:
        try:
            df = pd.read_csv('data/Main.csv')
        except Exception as e:
             df = pd.read_excel('data/Main.csv')

    # Show Dataset
    try:
        number = st.number_input('Select Number of Rows to View', value = 5)
        st.write(df.head(number).astype(str))
    except Exception as e: 
        if uploaded_file is None:
            st.write('No dataset has been uploaded. Please upload a file in the sidebar tab')

    # Select Columns 
    all_columns = df.columns.tolist()       
    selected_columns = st.multiselect('Select Columns to View', all_columns)
    new_df = df[selected_columns]
    st.dataframe(new_df.astype(str))
    
    # Show Values 
    columns = df.columns.tolist()
    selected_column = st.selectbox('Select Column', columns)
    if st.button('Value Count'):
        st.write(df[selected_column].value_counts())

    # Show Summary Values for numerical columns 
    st.subheader('Summary')
    summary_columns = df.columns.tolist()
    summary_df_columns = st.multiselect(label = 'Please select only numerical columns', options=summary_columns)
    summary_df = df[summary_df_columns]
    summary_df = summary_df.apply(pd.to_numeric)
    try:
        st.write(summary_df.describe())
    except Exception as e: 
        pass

    st.set_option('deprecation.showPyplotGlobalUse', False)

