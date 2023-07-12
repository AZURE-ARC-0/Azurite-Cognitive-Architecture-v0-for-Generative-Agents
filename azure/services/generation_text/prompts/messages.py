from services.generation_text.prompts.context_window import ContextWindow
from services.generation_text.prompts.primer_context import PrimerContext

class Messages():

    def __init__(self):
        self.message_history = "azure/static/messages/message_history.jsonl"
        self.message = None
        self.context_window = ContextWindow()
        self.primer_context = PrimerContext()

    def create(self, message="testing this", role="user"):
        if not message:
            return "No message provided."
        if not role:
            role = "user"
        if role == "user":
            self.message = {"role": "user", "content": message}
        if role == "assistant":
            self.message = {"role": "assistant", "content": message}
        if role == "system":
            self.message = {"role": "system", "content": message}
        self.context_window.create_prompts(self.message)
        print(self.context_window.context)
        return self.context_window.context
