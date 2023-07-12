from services.generation_text.openai_text import OpenAITextGeneration
from services.generation_text.prompts.messages import Messages
import base64


class DataHandler():
    def __init__(self):
        self.openai_text = OpenAITextGeneration()
        self.messages = Messages()
        self.image_path = "azure/static/images/Azurite001.png"

    def handle_chat(self, data, role):
        prompt = self.messages.create(message=data, role=role)
        response = self.openai_text.send_chat_complete(prompt)
        print(response)
        return response

    def handle_image(self):
        with open(self.image_path, "rb") as f:
            content = f.read()
        return base64.b64encode(content).decode("utf-8")
