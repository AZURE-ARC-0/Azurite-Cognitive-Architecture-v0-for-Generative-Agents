import streamlit as st
from server import DataHandler
import base64
from io import BytesIO

persona = ["Eris Bloom", "azure/static/images/Eris0001.png"]

data_handler = DataHandler(persona_image=persona[1])

st.title(persona[0])

blob_link = data_handler.handle_image()
image = BytesIO(base64.b64decode(blob_link))

with st.sidebar:
    st.image(image)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in data_handler.handle_chat(prompt, role="user"):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(f"{full_response} ▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({
        "role": "assistant",
        "content": full_response
        })