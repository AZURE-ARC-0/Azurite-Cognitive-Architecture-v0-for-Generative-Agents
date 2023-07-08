from langchain.schema import AIMessage, HumanMessage, SystemMessage
from services.text.context_window import ContextWindow
import json

class Messages:
    def __init__(self):
        self.context_window = ContextWindow()
        self.context = self.context_window.context

    def get_message(self, message, role="user"):
        if not message:
            return "Please provide a message"
        if not role:
            return "Please provide a role"
        try:
            if role == "user":
                message = HumanMessage(content=message)
            if role == "assistant":
                message = AIMessage(content=message)
            if role == "system":
                message = SystemMessage(content=message)
            self.context_window.add_message(message=message)

            return self.context
        except Exception as e:
            print(e)
            return "Error generating message"

    def save_message(self, message):
         with open(self.message_history, "r+") as file:
            json_data = json.load(file)
            json_data.append(self, message)
            file.seek(0)
            json.dump(json_data, file, indent=4)
            file.truncate()

    def get_recent_messages(self):
        with open(self.message_history, "r") as file:
            json_data = json.load(file)
        return [message for i, message in enumerate(json_data) if i < 10]

if __name__ == "__main__":
    Messages()
