import streamlit as st
import functions
letters = list(functions.letters.keys())
try:
    sheet = st.session_state["sheet"]
    st.sidebar.text_input(label="Margin", key="MRG", placeholder="Enter here:")
    st.sidebar.selectbox("In which column can prices be found?", letters, key="LETTER")
    if st.sidebar.button(label="Add margin", on_click=functions.dummy):
        try:
            value = float(st.session_state["MRG"])
            column_nr = st.session_state["LETTER"]
            column_nr = functions.a_to_1(column_nr)
            functions.findncalc(column_nr, value, sheet)
        except KeyError:
            pass
        except ValueError:
            pass
except KeyError:
    st.write("Load a file first")