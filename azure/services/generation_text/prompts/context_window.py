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

    def clear_context(self):
        self.context = []

    def check_queue(self):
        if len(self.context) > 10:
            self.context.pop(0)
        else:
            return self.context

    def create_prompts(self, message):
        prompts = [self.context]
        prompts.extend(iter(self.context))
        prompts.append(message)
        return prompts
