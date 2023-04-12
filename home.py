import streamlit as st
import openpyxl
import pandas as pd
from st_aggrid import AgGrid
st.set_page_config(layout="wide")

# Add a title and intro text
st.title('Excel files modifier.')
st.text('This is a web app to allow word replacement and adding margin to costs within excel files.')


# Sidebar setup
st.sidebar.title('Beta...')
upload_file = st.sidebar.file_uploader('Upload an excel file')

# Check if file has been uploaded
if upload_file is not None and upload_file.name.endswith(".xlsx"):
    st.session_state["uploaded"] = upload_file
    workbook = openpyxl.load_workbook(filename=upload_file, read_only=False)
    sheet = workbook.active
    st.session_state["workbook"] = workbook
    st.session_state["sheet"] = sheet
else:
    upload_file = None
try:
    st.sidebar.write("Currently uploaded: "+st.session_state["uploaded"].name)
    st.text("Imagine theres a real-time preview of the file here...")
except KeyError:
    st.sidebar.write("No file uploaded")


