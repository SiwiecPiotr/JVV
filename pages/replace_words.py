import streamlit as st
import functions

try:
    sheet = st.session_state["sheet"]
    workbook = st.session_state["workbook"]
    st.text("Imagine theres a real-time preview of the file here...")
    st.sidebar.text_input(label="To be replaced: ", key="OLD_WORD", placeholder="Enter here: ", )
    st.sidebar.text_input(label="Replacement: ", key="NEW_WORD", placeholder="Enter here: ", )
    if st.sidebar.button(label="Replace", on_click=functions.dummy):
        functions.switcheroo(st.session_state["OLD_WORD"], st.session_state["NEW_WORD"], st.session_state['sheet'])
    else:
        pass
except KeyError:
    st.write("Load a file first")