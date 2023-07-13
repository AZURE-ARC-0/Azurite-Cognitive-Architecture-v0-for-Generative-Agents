import json
from messages_defs import MessagesDefs
from services.system_tools.ye_logger_of_yor import logger


class Messages(MessagesDefs):

    def __init__(self):
        super().__init__()
        self.message_history = "azure/static/messages/message_history.jsonl"
        self.primer_path = "azure/static/templates/primers.jsonl"
        self.context = []
        self.primer = {}
        self.set_default_primer()

    def set_default_primer(self, primer=None):
        try:
            if not primer:
                with open(self.primer_path, 'r', encoding='utf-8') as f:
                    line = f.readline()
                    primer = json.loads(line)
            self.primer = primer
            self.context.append(self.primer)
        except FileNotFoundError as e:
            logger.error("Primer file not found: %s", e)
            raise PrimerNotFoundError("Primer file could not be opened") from e
        except json.JSONDecodeError as e:
            logger.error("Invalid primer file: %s", e)
            raise PrimerParseError("Primer file is invalid JSON") from e
        except Exception as e:
            logger.error("Unexpected error loading primer: %s", e)
            raise PrimerLoadError("Unexpected error loading primer") from e


    def add_message(self, message):
        self.context.append(message)

    def create_message(self, message, role=None):
        try:
            role = self.check_roles(role)
            created_message = {"role": role, "content": message}
            self.add_message(created_message)
            self.save_message(created_message, self.message_history)
        except ValueError as e:
            print("There was an error creating the message:", e)
            raise

    def save_message(self, message, filepath):
        with open(filepath, 'a') as file:
            file.write(json.dumps(message) + "\n")

    def retrieve_messages(self, filepath, num_messages=None):
        if not num_messages:
            num_messages = 8
        lines = []
        with open(filepath, 'r') as file:
            for i, line in enumerate(file):
                if i >= num_messages:
                    break
                lines.append(json.loads(line.strip()))
        return lines

    def check_roles(self, role =None):
        if not role:
            role = "user"
        roles = ["user", "system", "assistant"]
        if role not in roles:
            raise ValueError(f"Invalid role: {role}")
        else:
            return role

    def get_context(self, user_message, role=None, num_messages=None):
        self.context.insert(0, self.primer)
        history = self.retrieve_messages(self.message_history, num_messages)
        for message in history:
            self.add_message(message)
        self.create_message(user_message, role)
        return self.context
