import os
from langchain.chat_models import ChatOpenAI
from services.text.context_window import ContextWindow
from dotenv import load_dotenv

load_dotenv()

class OpenAIChatBot():
    def __init__(self, model="gpt-3.5-turbo"):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.chat = ChatOpenAI(model=model)

    def get_chat_response(self, messages):
        response = self.chat.generate(messages=[messages])
        print(response)
        return response
