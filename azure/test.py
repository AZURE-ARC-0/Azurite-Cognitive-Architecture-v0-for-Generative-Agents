from services.generation_text.prompts.message_manager import (
    MessageManager,
    DataHandler,
    OpenAITextGeneration
)


# Create instances of the necessary classes
data_handler = DataHandler()
openai_text = OpenAITextGeneration()
message_manager = MessageManager()

# Simulate a user message
user_message = "Hello, I'm a user!"

# Handle the user message and get the response
response = data_handler.handle_chat(user_message)

# Print the response
print(response)