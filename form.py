#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import requests as r
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import json
from datetime import datetime



def log_action_to_gsheet(language, action):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
    client = gspread.authorize(creds)

    sheet_id = "1ltnW3wecxJwgjMioigtBR5jz_o2GAPmnHJ1rHpcPu7Q"
    sheet = client.open_by_key(sheet_id).sheet1

    # Add a new row with the logged action
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [language, action, timestamp]
    sheet.append_row(row)


with st.form(key="language selection"):
    language = st.selectbox("Which language do you want to learn?", ["Spanish", "Japanese"])
    submit_button = st.form_submit_button(label='Get Started!')
    if submit_button:
        action = f"Button clicked: See your options ({language})"
        log_action_to_gsheet(language, action)
        if language == "Spanish":
            st.link_button(f"Babbel is the right place to learn {language}!", "https://my.babbel.com/en_GB/product-preview/SPA/default/node/0")
        else:
            st.link_button(f"[Let Toucan help you while we're adding {language}!, "https://jointoucan.com/")








