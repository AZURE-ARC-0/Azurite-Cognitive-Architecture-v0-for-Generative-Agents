from services.generation_text.openai_text import OpenAITextGeneration

def test_send_chat_complete():

    openai_text_gen = OpenAITextGeneration()

    prompt_list = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"}
    ]

    response = openai_text_gen.send_chat_complete(prompt_list)

    assert response["role"] == "assistant"
    assert isinstance(response["content"], str)
