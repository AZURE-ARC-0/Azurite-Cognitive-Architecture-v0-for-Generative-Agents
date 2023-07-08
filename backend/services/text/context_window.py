import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from langchain.schema import messages_to_dict, messages_from_dict
class ContextWindow():

    def __init__(self):
        self.context = []

    def add_message(self, message):
        try:
            self.check_queue()
            return self.context.append(message)
        except Exception as e:
            print(f"Error: \n{e}")
            return "Error adding context"

    def check_queue(self):
        if len(self.context) > 10:
            self.context.pop(0)
        else:
            return self.context


    def to_dict(self):
        return messages_to_dict(self.history.messages)

    def from_dict(self):
        return messages_from_dict(self.history.messages)

    def save_to_file(self):
        with open("static/message_history.jsonl", "w") as file:
            for message in self.context:
                json.dump(message, file)