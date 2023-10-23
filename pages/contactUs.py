import streamlit as st
from send_email import send_email
import pandas as pd
import os
import csv


# def selector_function():
#     df = pd.read_csv('topics.csv')
#     df = pd.DataFrame(df)
#     # print(df)
#     list_convert = (df['topic'].tolist())
#     list_tuple = tuple(list_convert)
#     return list_tuple
#
#
#
#
# with st.form("send email"):
#     email_box = st.text_input(label='Enter your email',
#                               placeholder='Pls enter your email here')
#
#     option = st.selectbox( 'Select your topic?', selector_function())
#     text = st.text_area(label="Enter your text here",
#                         placeholder="Pls enter the text here")
#     message= f"""\
# Subject:   {option}
#
# from {email_box}
#
# {text}
#
#    """
#     st.form_submit_button(label='Submit')
#     if 'Submit':
#         send_email(message)
#         #st.info('Email send successfully')
#
#
# def selector_function():
#     df = pd.read_csv('topics.csv')
#     df = pd.DataFrame(df)
#     # print(df)
#     list_convert = (df['topic'].tolist())
#     list_tuple = tuple(list_convert)
#     return list_tuple


df = pd.read_csv('topics.csv')

with st.form("send email"):
    email_box = st.text_input(label='Enter your email',
                              placeholder='Pls enter your email here')

    option = st.selectbox( 'Select your topic?', df['topic'])
    text = st.text_area(label="Enter your text here",
                        placeholder="Pls enter the text here")
    message= f"""\
Subject:   {option}

from {email_box}

{text}

   """
    st.form_submit_button(label='Submit')
    if 'Submit':
        send_email(message)
        st.info('Email send successfully')
