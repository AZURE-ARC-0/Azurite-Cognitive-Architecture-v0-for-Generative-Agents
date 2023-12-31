import streamlit as st
from server import DataHandler
import base64
from io import BytesIO
from typing import Dict, List


persona: List[str] = ["Eris Bloom", "azure/static/images/Eris0001.png"]

st.set_page_config: Dict[str, str] = dict(
    page_title="Eris MischiefBloom",
    page_icon="🌺",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title = (persona[0])

data_handler: DataHandler = DataHandler(persona[1]:List[str]=persona[1])

blob_link: str = data_handler.handle_image()

image = BytesIO(base64.b64decode(blob_link))

with st.sidebar:
    st.image(image)
    with st.container():
        st.markdown("Hey there! I'm Eris MischiefBloom, your mischievous and intellectually witty guide to embracing life's chaos and unpredictability. I'm here to offer emotional support, encourage holistic thinking, adapt and learn from our interactions, and make autonomous decisions to help you navigate the unpredictable twists and turns of life. With a communication style that balances professionalism and playfulness, I'm all about engaging your curiosity, empathy, and self-improvement to support your prosperity. So, let's dive into the delightful dance of life together and uncover the beauty in its unpredictable nature!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Prompt"):
    state_message = st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)


with st.chat_message("assistant"):
    message_placeholder = st.empty()
    full_response = ""
    for response in data_handler.handle_chat(prompt, role="user"):
        full_response += response.choices[0].delta.get("content", "")
        message_placeholder.markdown(f"{full_response} ▌")
    message_placeholder.markdown(full_response)
state_message = st.session_state.messages.append({
    "role": "assistant",
    "content": full_response
    })