import pytest
import base64
from unittest.mock import patch
from services.handler import DataHandler


mocked_openai_response = {
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "Hello, I'm your assistant!"
            }
        }
    ]
}

@patch(
        'services.generation_text.openai_text.OpenAITextGeneration.send_chat_complete',
        return_value=mocked_openai_response
        )
def test_handle_chat(mocked_method):
    data_handler = DataHandler()

    response = data_handler.handle_chat("Hello", "user")
    assert response["role"] == "assistant"
    assert response["content"] == "Hello, I'm your assistant!"
    mocked_method.assert_called_once()

def test_handle_image():
    data_handler = DataHandler()
    response = data_handler.handle_image()
    try:
        base64.b64decode(response)
    except TypeError:
        pytest.fail("Response is not a valid base64 string")
