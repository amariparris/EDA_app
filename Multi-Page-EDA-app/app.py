import streamlit as st
from multiapp import MultiApp
from Apps import Data_Explorer, viz, Data_Upload


app = MultiApp()
st.markdown("""
# Data Explorer App

Welcome to the Data Explorer app! A multi-page app built using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar]. 
This app will function as a tool for filtering and visualizing data relationships.
""")

# Add all your application pages here
app.add_app("Data Upload", Data_Upload.app)
app.add_app("Preview Data", Data_Explorer.app)
app.add_app("Visualization", viz.app)
app.run()

