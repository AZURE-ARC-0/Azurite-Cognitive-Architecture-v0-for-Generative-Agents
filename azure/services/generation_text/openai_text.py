import os
import sys
import openai
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

openai.api_key = os.getenv("OPENAI_API_KEY")


class OpenAITextGeneration():
    def __init__(self):
        pass

    def send_chat_complete(self, prompt_list):
        messages = list(prompt_list)
        print(messages)
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
                stream=True
                )
            print(response)
            return response
        except ConnectionError as e:
            print(f"There was an error connecting to OpenAI: {e}")
            raise
