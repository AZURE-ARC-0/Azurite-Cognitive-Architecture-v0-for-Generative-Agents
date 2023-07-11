import streamlit as st
from server import DataHandler
import base64
from io import BytesIO

data_handler = DataHandler()

st.title("Hex Port")

blob_link = data_handler.handle_image()
image = BytesIO(base64.b64decode(blob_link))

with st.sidebar:
    st.image(image, use_column_width=True)

if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if prompt := st.chat_input("What is up?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        full_response += data_handler.handle_chat(prompt, role="user")["content"]
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})