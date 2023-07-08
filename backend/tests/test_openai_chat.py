import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.text.openai_chat import OpenAIChatBot
from langchain.schema import HumanMessage


def test_openai_chat():
    chat_bot = OpenAIChatBot(model="gpt-4")
    messages = [HumanMessage(content="write a haiku about a duck finding a fedora")]
    response = chat_bot.get_chat_response(messages=messages)

    generations = response.generations
    llm_output = response.llm_output
    run = response.run

    text = generations[0][0].text

    token_usage = llm_output["token_usage"]
    model_name = llm_output["model_name"]
    run_id = run[0].run_id

    new_object = {
        "text": text,
        "token_usage": token_usage,
        "model_name": model_name,
        "run_id": run_id,
    }
    print(f"=====\n{text}\n=====\n")

    return new_object


if __name__ == "__main__":
    test_openai_chat()
