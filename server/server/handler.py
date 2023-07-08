from services.text_generation.openai import openai
from services.text_generation.messages import Messages
from services.text_generation.prompt_templates import PromptTemplates

class Handler():
    def __init__(self):
        self.openai = openai()
        self.messages = Messages()
        self.prompt_templates = PromptTemplates()

    def handle_chat(self, message, role):
        prompt = self.messages.create(message, role)
        response = self.openai.send_chat_complete(prompt)
        return response.choices[0].message