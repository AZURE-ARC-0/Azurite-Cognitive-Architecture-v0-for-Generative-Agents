import json
import logging
from io import BytesIO
logger = logging.getLogger(__name__)
class MessageManager:



    def __init__(self):
        self.context = []
        self.primer = None
        self.primer_path = "azure/static/templates/primers.jsonl"
        self.history_path = "azure/static/messages/message_history.jsonl"
        self.set_default_primer()

    def set_default_primer(self, primer=None):
        if not primer:
            with open(self.primer_path, "r") as f:
                primer = json.loads(f.read())
        self.primer = primer
        self.context.append(self.primer)
        print(self.context)

    def create_message(self, message, role=None):
        if not role:
            role = "user"
        role = self.check_roles(role)
        created_message = {"role": role, "content": message}
        self.add_message(created_message)
        self.save_message(created_message, self.history_path)
        return [created_message]

    def save_message(self, message, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            message = BytesIO.readline(f.read().strip().split("\n"))
            print(json.dumps(json.dumps(message)))
            logger.log(message)

    def retrieve_messages(self, filepath, num_messages=None):
        if not num_messages:
            num_messages = 8
        with open (filepath, "r", encoding="utf-8") as f:
            message = f.read().strip().split("\n")
            print(json.dumps(json.dumps(message)) )

        print(f"Retrieved {num_messages} messages from {filepath}")

    def check_roles(self, role=None):
        roles = ["user", "system", "assistant"]
        if role not in roles:
            role = "user"
        return role

    def get_context(self, user_message, role=None, num_messages=None):
        if not num_messages:
            num_messages = 8
        self.add_message(self.primer)
        self.retrieve_messages(self.history_path, num_messages)
        self.create_message(user_message, role)

    def add_message(self, message):
        self.context.append(message)


class MockSystem:
    def __init__(self):
        self.message_system = []

    def open_primer_path(self, primer_path):
        return_values = [
            {"role": "system",
             "content": "You are a friendly and helpful chat bot.You answer honestly and if you dont know something you just let the user know. You reply with enthusiastic and friendly responses."}
        ]
        self.message_system.append(return_values)
        if primer_path == "azure/static/templates/primers.jsonl":
            return json.dumps(return_values)

    def open_history_path(self, history_path):
        return_values = [
            {"role": "user", "content": "yay it works!"},
            {"role": "assistant", "content": "Oh, does it? Well I'm glad you got it working"},
            {"role": "user", "content": "whats your name?"},
            {"role": "assistant", "content": "I am Eris Bloom! Ready for a bit of adventure?"},
            {"role": "user", "content": "can you give me a brief description of your self for your info card?"},
        ]
        for message in return_values:
            self.message_system.append(message)
        if history_path == "azure/static/messages/message_history.jsonl":
            return json.dumps(return_values)

    def mock_save_message(self, message, filepath):
        if filepath == "azure/static/templates/messages.jsonl":
            self.message_system.append(message)
        response = f"\nMessage saved: {message}\n"
        return response

    def mock_create_message(self, message, role):
        return_values = [
            "hello how are you today?",
            "user"
        ]
        value2 = [
            "great how are you?",
            "assistant"
        ]

    def mock_get_context(self, user_message, role, num_messages):
        user_message = "amazing, what a great day!"
        role = "user"
        num_messages = 8
        return user_message, role, num_messages


# Create instances of the classes
message_manager = MessageManager()
mock_system = MockSystem()

# Use the instances to call the methods and simulate a conversation
user_message = "Hello, how are you today?"
role = "user"
num_messages = 8

message_manager.get_context(user_message, role, num_messages)

print("\nMockSystem messages:")
print(mock_system.message_system)
