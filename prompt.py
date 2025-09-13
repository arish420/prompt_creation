import streamlit as st


st.title("Create your Custom Prompts")

selection = st.sidebar.selectbox('Select', ('Home','Personal PII','Medical PII','Financial PII'))

if selection == 'Home':
  st.write("Welcome to Data Privacy using LLMs")

if selection == 'Personal PII':
  country = st.selectbox('Select', ('Pakistan','USA'))
  options = st.multiselect(
    "What are your favorite colors?",
    ["Green", "Yellow", "Red", "Blue"],
    default=["Yellow", "Red"],
    )

