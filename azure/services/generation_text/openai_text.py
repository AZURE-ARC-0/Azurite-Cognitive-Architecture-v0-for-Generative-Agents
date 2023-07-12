import os
import sys
import openai
from dotenv import load_dotenv
from services.generation_text.prompts.messages import Messages

load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

openai.api_key = os.getenv("OPENAI_API_KEY")


class OpenAITextGeneration():
    def __init__(self):
        self.messages = Messages()

    def send_chat_complete(self, message):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt_list
            )
        return response.choices[0]["message"]

    def get_prompt_list(self, message, role=None):
        message_prompt = self.messages.create(message, role)
        primer = self.messages.primer
        context = self.messages.context_window.create_prompts(message_prompt)