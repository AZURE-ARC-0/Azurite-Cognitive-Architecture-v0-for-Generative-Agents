import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.text.openai_messages import Messages


def test_openai_messages():
    prompts = Messages()
    system_message = prompts.get_message(message="You are a friendly and helpful chatbot. You provide verbose and detailed answers to queries. If you do not know the answer to something you simply say 'I dont know.'")
    print(f"\nsystem_message:\n {system_message}\n-------")
    human_message = prompts.get_message(message="hi", role="user")
    print(f"\nhuman_message:\n {human_message}\n-------")
    ai_message = prompts.get_message(message="Hi there! How can I help you?", role="ai")
    print(f"\nai_message:\n {ai_message}\n-------")
    #chat_prompt = prompts.get_chat_prompt_template([system_message, human_message, ai_message])
    #print(f"\nchat_prompt:\n {chat_prompt}\n-------")
    #human_template = prompts.get_prompt_templates(message="{text}", input_variables=("text"), role="user")
    #print(f"\nhuman_template:\n {human_template}\n-------")

if __name__ == "__main__":
    test_openai_messages()