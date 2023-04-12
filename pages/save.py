import streamlit as st
import io, functions

try:
    workbook = st.session_state["workbook"]
    st.text("Imagine theres a real-time preview of the file here...")
    st.sidebar.text_input(label="Filename: ", placeholder="Enter here: ", key="FILENAME")
    if st.sidebar.button(label="Save", on_click=functions.dummy):
        workbook.save("temp_name.xlsx")
        with open("temp_name.xlsx", "rb") as tmp:
            buffer = io.BytesIO(tmp.read())
        st.sidebar.download_button(
            label="Download Excel worksheet",
            data=buffer,
            file_name=st.session_state["FILENAME"] + ".xlsx",
            mime="application/vnd.ms-excel", )
        for key in st.session_state.keys():
            del st.session_state[key]

    else:
        pass
except KeyError:
    st.write("Load a file first")