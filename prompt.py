import streamlit as st


st.title("Create your Custom Prompts")

selection = st.sidebar.selectbox('Select', ('Personal PII','Medical PII','Financial PII'))
