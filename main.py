import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.header("The Best Company")
content = """
The incontrovertible benefits and blessings of fellowship with the Holy Spirit can’t be overemphasized. 
The Holy Spirit wants to be involved with every part of your life, and you must let Him. 
He wants your progress, advancement, prosperity, and success to be evident for all to see
 """
st.subheader("Our Team")
col1, col2, col3 = st.columns(3)
pd = pd.read_csv('data.csv')
with col1:
    for index, row in pd[:4].iterrows():
        st.header(f"{row['first name'].capitalize()}  {row['last name'].capitalize()}")
        st.write(row['role'].title())
        st.image("images/" + row['image'])
with col2:
    for index, row in pd[4:8].iterrows():
        st.header(f"{row['first name'].capitalize()}  {row['last name'].capitalize()}")
        st.write(row['role'].title())
        st.image("images/" + row['image'])
with col3:
    for index, row in pd[8:].iterrows():
        st.header(f"{row['first name'].capitalize()}  {row['last name'].capitalize()}")
        st.write(row['role'].title())
        st.image("images/" + row['image'])