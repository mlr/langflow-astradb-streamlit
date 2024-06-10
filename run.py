import streamlit as st
from langflow.load import run_flow_from_json
from dotenv import load_dotenv
load_dotenv()

USER = "user"
ASSISTANT = "assistant"

question: str = st.chat_input("Enter a prompt here")

if question:
    st.chat_message(USER).write(question)
    result = run_flow_from_json("chat-rag.json", input_value=question)
    chat_result = result[0].outputs[0].results
    st.chat_message(ASSISTANT).write(f"{chat_result}")

# question = "Who is the RFP for?"
# print(f"User: {question}")
#
# result = run_flow_from_json("chat-rag.json", input_value=question)
# print(f"System: {result[0].outputs[0].results}")
