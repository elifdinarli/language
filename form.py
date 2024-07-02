#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import requests as r
import pandas as pd



# In[ ]:





# In[ ]:


with st.form(key="language selection"):
    language = st.selectbox("Which language do you want to learn?", ["Spanish", "Japanese"])
    submit_button = st.form_submit_button(label='See your options')
    if submit_button:
        if language in ("Spanish"):
            st.link_button("Babbel is the right place to learn " +language+"!", "https://my.babbel.com/en_GB/product-preview/SPA/default/node/0")
        else:
            st.link_button("Let Toucan helps you while we're adding " + language, "https://jointoucan.com/")


# In[ ]:





# In[ ]:





# In[ ]:




