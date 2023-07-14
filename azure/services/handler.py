#services/handler.py
from services.generation_text.openai_text import OpenAITextGeneration
from services.generation_text.prompts.message_manager import MessageManager
import base64
from typing import Optional


class DataHandler():
    def __init__(self, persona_image=None):
        self.openai_text = OpenAITextGeneration()
        self.message_manager = MessageManager()
        self.image_path = persona_image

    def handle_chat(
            self,
            user_message: str,
            role: Optional[str] = None,
            num_messages: Optional[int] = None):
        prompt_list = self.message_manager.get_context(
            user_message,
            role,
            num_messages,
        )
        response = self.openai_text.send_chat_complete(prompt_list)
        self.handle_bot_response(response["choices"][0]["message"])
        return response

    def handle_bot_response(self, store_message):
        combine_message = []
        for message in store_message:
            combine_message += [message]
        self.message_manager.add_message(message=store_message)

    def handle_image(self):
        with open(self.image_path, "rb") as f:
            content = f.read()
        return base64.b64encode(content).decode("utf-8")
