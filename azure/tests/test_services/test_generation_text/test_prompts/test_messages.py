import pytest
from services.generation_text.prompts.messages import Messages


def test_create():
    messages = Messages()
    message = "Test message"

    result = messages.create_message(message, role="user")
    assert result == {"role": "user", "content": message}

    result = messages.create_message(message, role="assistant")
    assert result == {"role": "assistant", "content": message}

    result = messages.create_message(message, role="system")
    assert result == {"role": "system", "content": message}

    result_test = messages.create_message(message, role="unknown")

    @pytest.mark.xfail
    def unkonwn_role(result):
        assert result["role"] == "unknown"

    result = unkonwn_role(result_test)

    result = messages.create("", role="user")
    assert result == "No message provided."
