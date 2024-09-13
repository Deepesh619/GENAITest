#from src.MCQGEN.mcqgen import response
#from src.MCQGEN.logger import logging
import streamlit as st
import src.MCQGEN.mcqgen as mcq

st.title('SFMC Chat bot')

# Create a text input box for the user to enter messages
user_input = st.chat_input("Message SFMC AI Chatbot")

messages = st.container(height=300)

if user_input:
    response = mcq.test(user_input)
    #st.text(response)
    
    messages.chat_message("user").write(user_input)
    messages.chat_message("assistant").write(response)