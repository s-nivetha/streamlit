import streamlit as st

st.title("Nivi's Test App")

name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello, {name}! Welcome to Nivi's Test App.")
