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

  regular_exp = st.write("Enter Regular Expression, if required -> e.g key: mac-address, value: regular expression to match mac-address")
  user_dict = {}
  num_entries = st.number_input("How many key-value pairs do you want to add?", min_value=0, value=1)
  
  for i in range(int(num_entries)):
      key = st.text_input(f"Enter Key{i+1}:", key=f"key_{i}")
      value = st.text_input(f"Enter Regular Expression {i+1}:", key=f"value_{i}")
      if key:  # Only add if a key is provided
          user_dict[key] = value
  
  if user_dict:
      st.write("Your dictionary:")
      st.write(user_dict)


