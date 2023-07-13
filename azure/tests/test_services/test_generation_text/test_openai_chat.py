from services.generation_text.openai_text import OpenAITextGeneration


def test_send_chat_complete():

    openai_text_gen = OpenAITextGeneration()

    message = "Who won the world series in 2020?"

    response = openai_text_gen.send_chat_complete(message)
    test_message = "Who won the world series in 2020?"
    assert response.choices[0]["message"]["content"] == test_message
    assert isinstance(response["content"], str)
