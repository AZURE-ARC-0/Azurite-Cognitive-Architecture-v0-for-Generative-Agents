import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import openai
from dotenv import load_dotenv

from messages import Messages

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIAPI():
    def __init__(self):
        self.model = self.change_model()
        self.messages = Messages()
    def send_chat_complete(self, messages):
        response = openai.Completion.create(
            model = self.model
            messages = messages
        )
    def change_model(self, model="gpt-3.5-turbo"):
        self.model = model
        return f"Model changed to {self.model}"
