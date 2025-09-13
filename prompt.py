import streamlit as st
from langchain_core.prompts import PromptTemplate
import io


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

  with st.expander("Regular Expression/Few-shots"):

    regular_exp = st.write("Enter Regular Expression/Few-shots, if required -> e.g key: mac-address, value: regular expression to match mac-address")
    user_dict = {}
    num_entries = st.number_input("How many key-value pairs do you want to add?", min_value=0, value=0)
    
    for i in range(int(num_entries)):
        key = st.text_input(f"Enter Key{i+1}:", key=f"key_{i}")
        value = st.text_input(f"Enter Regular Expression {i+1}:", key=f"value_{i}")
        if key:  # Only add if a key is provided
            user_dict[key] = value
    
    if user_dict:
        st.write("Your dictionary:")
        st.write(user_dict)
  if st.button("Generate Prompt"):
    # pass
    prompt_text = """You are a Data Privacy Expert. You need to extract Personally Identifiable Information (PII).\n
                            ### Your target PII is as follows:"""
    for i in personal_pii_options:
        # st.write(i)
        prompt_text = prompt_text + """\n - """ + i + """\n"""
    for i in user_dict.keys():
        prompt_text = prompt_text + """\n""" + i + """ : """ + user_dict[i] + """\n"""
    

    prompt_text = prompt_text + """ ### Output Format:
                            {{
                              pii: actual content
                            }}

                            Target Country: While extracting the above fields, keep in mind the format followed in {target_country}.

                            Note:
                            No leading and trailing explanation with output. Just a dictionary only.


                            ### Target Text: {sensitive_text}"""
                            # input_variables=['sensitive_text','target_country']
    

    st.markdown(prompt_text)                        # )
    # Save + Download
  # if st.button("Save & Download Template"):
    personal_pii = PromptTemplate(template=prompt_text,input_variables=['sensitive_text'])
    st.write(personal_pii)
    buffer = io.StringIO()
    personal_pii.save(buffer)   # saves as JSON to file-like object
    data = buffer.getvalue()
    st.download_button(
        label="Download PromptTemplate JSON",
        data=data,
        file_name=f"{name}.json",
        mime="application/json"
    )
  

    
    










  


  
  
