import json


class Messages():

    def __init__(self):
        self.message_history = "static/messages/message_history.jsonl"

    def create(self, message, role="user"):
        if not message:
            return "please enter a message"
        if role == "user":
            #self.save_recent_message(message)
            return {"role": "user", "content": message}
        if role == "assistant":
            self.save_recent_message(message)
            return {"role": "assistant", "content": message}
        if role == "system":
            self.save_recent_message(message)
            return {"role": "system", "content": message}
        else:
            return "Unknown role"

    def save_recent_message(self, message):
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
