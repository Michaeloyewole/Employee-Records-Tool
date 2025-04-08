import streamlit as st  
import pandas as pd  

st.title('HR Management System')  

# Placeholder welcome message  
st.write('Welcome to the HR Management System!')  

# Example of a simple form for data input  
st.header('Add New Employee')  
first_name = st.text_input('First Name')  
last_name = st.text_input('Last Name')  
email = st.text_input('Email')  
if st.button('Submit'):  
    st.write('Employee added:', first_name, last_name, email)  
