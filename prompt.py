import streamlit as st


st.title("Create your Custom Prompts")

selection = st.sidebar.selectbox('Select', ('Home','Personal PII','Medical PII','Financial PII'))

if selection == 'Home':
  st.write("Welcome to Data Privacy using LLMs")

if selection == 'Personal PII':
  country = st.selectbox('Select', ('Pakistan','USA'))
  personal_pii_options = st.multiselect(
    "What are your favorite colors?",
    ["Name","Email","Phone","Address", "Date of Birth","Mother's name","Social Media Handles","National ID Number (e.g., CNIC, SSN, Aadhaar)","Passport Number","Driver’s License Number","Voter ID Number","Tax Identification Number","Bank Account Number","Credit/Debit Card Numbers","Digital Wallet IDs (PayPal, Apple Pay, etc.)"],
    default=["Name","Email","Phone"],
    )
  st.write(personal_pii_options)


