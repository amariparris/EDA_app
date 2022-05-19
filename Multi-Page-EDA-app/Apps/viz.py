import streamlit as st
import pandas as pd
import numpy as np
from numpy import mean
from numpy import std
from numpy import cov
from scipy.stats import pearsonr
import sklearn
import os
import matplotlib.pyplot as pyplot
import matplotlib as plt
import seaborn as sns

def app():

    st.title('Visualization')

    st.write('This is the `Visualization` tool of the Data Explorer app.')

    st.write('Construct standard graphs for variables of your choice')
    
    if 'main_data.csv' not in os.listdir('data'):
        st.markdown("Please upload data through `Upload Data` page.")
     else:
        try:
            df = pd.read_csv('data/Main.csv')
        except Exception as e:
             df = pd.read_excel('data/Main.csv')
    
    # Plotting and Visualization
    all_columns_names = df.columns.tolist()

    st.header('Standard Plots')
    selected_columns_names = st.multiselect('Select Columns to Plot', all_columns_names)
    type_of_plot = st.selectbox('Choose Plot Type', ['area', 'bar', 'box', 'corr', 'hist', 'kde', 'line', 'pie'])
    plot_type_dict = {'area':'area plot', 'bar':'bar plot', 'box':'box plot', 'corr':'correlation plot', 'hist':'histogram', 'kde':'kde plot', 'line':'line plot', 'pie':'pie plot'}
    
    if st.button('Create Plot'):
        st.success('Create {} for {}'.format(plot_type_dict[type_of_plot], selected_columns_names))

        # Plot on streamlit
        if type_of_plot == 'area': 
            custom_data = df[selected_columns_names]
            custom_data = custom_data.apply(pd.to_numeric)
            st.area_chart(custom_data)

        elif type_of_plot == 'bar': 
            custom_data = df[selected_columns_names]
            custom_data = custom_data.apply(pd.to_numeric)
            st.bar_chart(custom_data)

        elif type_of_plot == 'line': 
            custom_data = df[selected_columns_names]
            custom_data = custom_data.apply(pd.to_numeric)
            st.line_chart(custom_data)

        #Plot using Matplotlib
        elif type_of_plot == 'box':
            custom_data = df[selected_columns_names]
            custom_data = custom_data.apply(pd.to_numeric)
            custom_plot = custom_data.plot(kind= type_of_plot)
            st.write(custom_plot)
            st.pyplot()

        elif type_of_plot == 'hist': 
            custom_data = df[selected_columns_names]
            custom_data = custom_data.apply(pd.to_numeric)
            custom_plot = custom_data.plot(kind= type_of_plot)
            st.write(custom_plot)
            st.pyplot()
            
        elif type_of_plot == 'corr': 
            custom_data = df[selected_columns_names]
            custom_data = custom_data.apply(pd.to_numeric)
            st.write(sns.heatmap(custom_data.corr(), annot=True))
            st.pyplot()
        
        elif type_of_plot == 'pie':
            custom_data = df[selected_columns_names]
            st.write(custom_data[selected_columns_names].value_counts().plot.pie(autopct='%1.1f%%'))
            pyplot.ylabel(selected_columns_names)
            st.pyplot()

        elif type_of_plot == 'kde': 
            custom_data = df[selected_columns_names]
            custom_data = custom_data.apply(pd.to_numeric)
            custom_plot = custom_data.plot(kind= type_of_plot)
            st.write(custom_plot)
            st.pyplot()

    st.header('Scatter Plots')

    type_of_scatter_plot = st.selectbox('Choose Plot Type', ['normal','Color-coded', 'Regression', 'Multiple Regression'])
    
    X_value = st.selectbox('X-axis', selected_columns_names)
    Y_value = st.selectbox('Y-axis', selected_columns_names)

    if type_of_scatter_plot == 'Color-coded' or type_of_scatter_plot == 'Multiple Regression': 
            Hue = st.selectbox('Choose Categorical Variable', all_columns_names) 
    
    if st.button('Create Scatter Plot'):
        st.success('Create {} Plot for {}'.format(type_of_scatter_plot, selected_columns_names))
        
        # Plot on streamlit
        if type_of_scatter_plot == 'normal': 
            custom_data = df[selected_columns_names]
            custom_data = custom_data.apply(pd.to_numeric)
            custom_plot = sns.scatterplot(x=custom_data[X_value], y=custom_data[Y_value])
            st.write(custom_plot)
            st.pyplot()

        elif type_of_scatter_plot == 'Color-coded':
            custom_data = df[selected_columns_names]
            custom_data = custom_data.apply(pd.to_numeric)
            custom_plot = sns.scatterplot(x=custom_data[X_value], y=custom_data[Y_value], hue=Hue)
            st.write(custom_plot)
            st.pyplot()

        elif type_of_scatter_plot == 'Regression': 
            custom_data = df[selected_columns_names]
            custom_data = custom_data.apply(pd.to_numeric)
            custom_plot = sns.regplot(x=custom_data[X_value], y=custom_data[Y_value])
            st.write(custom_plot)
            st.pyplot()

        #Plot using Matplotlib
        elif type_of_scatter_plot == 'Multiple Regression':
            custom_data = df[selected_columns_names]
            custom_data = custom_data.apply(pd.to_numeric)
            custom_plot = sns.lmplot(x=custom_data[X_value], y=custom_data[Y_value], hue=Hue)
            st.write(custom_plot)
            st.pyplot()

        covariance = cov(custom_data[X_value], custom_data[Y_value])
        corr = pearsonr(custom_data[X_value], custom_data[Y_value])
        
        st.markdown("---")

        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader('Covariance:')
            st.write(covariance[0,1])
            st.subheader('Correlation Coefficient:')
            st.write(corr[0])

        with col2:
            st.subheader('Mean:')
            st.write("{}: {}".format(X_value, mean(custom_data[X_value])))
            st.write("{}: {}".format(Y_value, mean(custom_data[Y_value])))
            st.subheader('Standard Deviation:')
            st.write("{}: {}".format(X_value, std(custom_data[X_value])))
            st.write("{}: {}".format(Y_value, std(custom_data[Y_value])))

    st.set_option('deprecation.showPyplotGlobalUse', False)
