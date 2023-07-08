import base64
from services.text.openai_chat import OpenAIChatBot
from services.text.openai_messages import Messages
from services.text.prompt_templates import PromptTemplates
from services.vectorstore.web_scraper import WebScraper
from services.vectorstore.chroma import ChromaDB

class Handler():
    def __init__(self):
        self.openai = OpenAIChatBot()
        self.messages = Messages()
        self.prompt_templates = PromptTemplates()
        self.web_scraper = WebScraper()
        self.vectorstore = ChromaDB()
        self.image_path = "static\images\Azurite001.png"

    def handle_chat(self, message, role):
        prompt = self.messages.create(message, role)
        self.messages.save_message()
        response = self.openai.get_chat_response(prompt)
        return response.choices[0].message

    def handle_image(self):
        with open(self.image_path, "rb") as file:
            image_data = file.read()
            base64_data = base64.b64encode(image_data).decode("utf-8")
            blob_link = f"data:image/png;base64,{base64_data}"
        return blob_link

    def handle_recent_messages(self):
        return self.messages.get_recent_messages()

    def handle_scrape_site(self, links):
        return self.web_scraper.get_page_data(links)

    def vectordb_add_document(self, data):
        self.vectorstore.add_document(data)