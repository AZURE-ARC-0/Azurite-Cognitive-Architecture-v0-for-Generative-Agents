from services.generation_text.prompts.messages import Messages


def test_create():
    messages = Messages()
    message = "Test message"

    result = messages.create(message, role="user")
    assert result == {"role": "user", "content": message}

    result = messages.create(message, role="assistant")
    assert result == {"role": "assistant", "content": message}

    result = messages.create(message, role="system")
    assert result == {"role": "system", "content": message}

    result = messages.create(message, role="unknown")
    assert result == "Unknown role"

    result = messages.create("", role="user")
    assert result == "No message provided."
