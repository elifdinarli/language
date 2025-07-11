#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import requests as r
import pandas as pd


# In[ ]:


st.title("Contentful Bulk Edit Tool - MVP")
st.subheader("Example use case: creating banner sections with an existing Flags CTA")


# In[ ]:


headers = {'Authorization': st.secrets["token"], 
           'Content-Type': 'application/vnd.contentful.management.v1+json'}


# In[ ]:


file = st.file_uploader("Upload a CSV")


if file is not None:
    df = pd.read_csv(file)
    st.write(df)
else:
    st.write("Please upload a file.")



# In[43]:


def banner(content_type, entry_title, color_palette, title, layout, cta):
    banner = {
        'fields': {
            'entryTitle': {'en-US': entry_title},
            'colorPalette': {'en-US': color_palette},
            'titleRichText': {'en-US': {
                'data': {},
                'content': [{
                    'data': {},
                    'content': [{
                        'data': {},
                        'marks': [],
                        'value': title,
                        'nodeType': 'text'
                    }],
                    'nodeType': 'paragraph'
                }],
                'nodeType': 'document'
            }},
            'layout': {'en-US': layout},
            'callToAction': {'en-US': [
                {
                    'sys': {
                        'type': 'Link',
                        'linkType': 'Entry',
                        'id': cta
                    }
                }
            ]}
        }
    }
    headers = {'Authorization': st.secrets["token"], 
               'Content-Type': 'application/vnd.contentful.management.v1+json',
               'X-Contentful-Content-Type': content_type}
    create = r.post("https://api.contentful.com/spaces/zuzqvf4m2o58/environments/master/entries", headers=headers, json=banner)
    result = create.json()
    return(result['sys']['id'])


# In[32]:


for index, row in df.iterrows():
    entry_title = row['entry_title']
    color_palette = row['color_palette']
    title = row['title']
    layout = row['layout']
    cta = row['cta']
    entry_id = banner(entry_title, color_palette, title, layout, cta)
    url = "https://app.contentful.com/spaces/zuzqvf4m2o58/environments/master/entries/"+str(entry_id)
    st.write(entry_title)
    st.link_button("Click me", url)


# In[ ]:
