#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import requests as r
import pandas as pd
from datetime import datetime
import time


# In[ ]:


st.title("Learn a new language")


# In[ ]:


with st.form(key="language selection")
    language = st.selectbox("Which language do you want to learn?", ["Spanish"], ["German"], ["Japanese"])
    submit_button = st.form_submit_button(label='Get Started!')
    if submit_button:
        if language in (["Spanish"], ["German"]):
            st.link_button("Babbel is the right place to learn " +language, "https://my.babbel.com/en_GB/product-preview/SPA/default/node/0")
        else:
            st.link_button("Let Toucan helps you while we're adding " + language)


# In[ ]:





# In[ ]:





# In[ ]:




