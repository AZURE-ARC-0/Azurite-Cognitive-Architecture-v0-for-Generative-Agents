def create_prompts(self, message):
    prompts = [self.primer]
    prompts.extend(iter(self.context_window))
    prompts.append(message)
    return prompts