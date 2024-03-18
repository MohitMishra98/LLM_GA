from openai import OpenAI
import streamlit as st
import os

st.title("Innovate Automate")

BASE_URL = "https://api.groq.com/openai/v1"

client = OpenAI(api_key="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",base_url=BASE_URL)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "mixtral-8x7b-32768"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your prompt here"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})