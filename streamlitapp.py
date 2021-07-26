import streamlit as st
import pandas as pd
from ast import literal_eval
from cdqa.utils.converters import pdf_converter
from cdqa.pipeline import QAPipeline
from cdqa.utils.download import download_model

import urllib.request
from fpdf import FPDF
import base64
import os
import webbrowser



st.set_page_config(page_title='QNA MODEL', layout = 'wide', initial_sidebar_state = 'auto')
col1,col2 = st.beta_columns([1,6])

with col2:
    menu = ['DEWA REGULATIONS FOR  ELECTRICAL INSTALLATIONS',
    'ASHRAE]
    choice = st.sidebar.selectbox("Choose Form",options = menu)
if choice == 'DEWA REGULATIONS FOR  ELECTRICAL INSTALLATIONS':
                    try:
                      BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                      docs_path = os.path.join(BASE_DIR, "DEWA")
                      df = pdf_converter(directory_path = docs_path)
                      BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                      models_path = os.path.join(BASE_DIR, "bert_qa.joblib")
                      cdqa_pipeline = QAPipeline(reader = models_path)
                      cdqa_pipeline.fit_retriever(df=df)
                      n_predictions=st.sidebar.slider(label="Number Of Predictions",min_value=1,max_value=10)
                      #query = ' What is Fire Fighting system for above 90m building height ?'
                      st.title('Query Answering AI Bot')
                      query=st.text_input("Enter Text: ")
                      if query:
                        prediction = cdqa_pipeline.predict(query, n_predictions=n_predictions)
                        for i,value in enumerate(prediction):
                          answer,title,paragraph,predictionsss=value
                          answer_var=st.write("Answer: "+answer)
                          title_var=title.replace(" ","%20")
                          url="https://github.com/hebaarch/fire-and-safety-guidelinesraw/main/dewa/"+title_var+".pdf"
            
                          paragraph_var=st.write("Paragraph: " + paragraph)
                          page_number = st.write("Page Number: " + title)
                          st.markdown("Download This Report Here [link](%s)" % url)
                
                elif choice == 'ASHRAE':

                    try:
                      BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                      docs_path = os.path.join(BASE_DIR, "ASHRAE")
                      df = pdf_converter(directory_path = docs_path)
                      BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                      models_path = os.path.join(BASE_DIR, "bert_qa.joblib")
                      cdqa_pipeline = QAPipeline(reader = models_path)
                      cdqa_pipeline.fit_retriever(df=df)
                      n_predictions=st.sidebar.slider(label="Number Of Predictions",min_value=1,max_value=10)
                      #query = ' What is Fire Fighting system for above 90m building height ?'
                      st.title('Query Answering AI Bot')
                      query=st.text_input("Enter Text: ")
                      if query:
                        prediction = cdqa_pipeline.predict(query, n_predictions=n_predictions)
                        for i,value in enumerate(prediction):
                          answer,title,paragraph,predictionsss=value
                          answer_var=st.write("Answer: "+answer)
                          title_var=title.replace(" ","%20")
                          url="https://github.com/hebaarch/fire-and-safety-guidelinesraw/main/ashrae/"+title_var+".pdf"
                          paragraph_var=st.write("Paragraph: " + paragraph)
                          page_number = st.write("Page Number: " + title)
                          st.markdown("Download This Report Here [link](%s)" % url)

