from services.generation_text.prompts.context_window import ContextWindow


def test_add_message():
    context_window = ContextWindow()
    result = context_window.add_message("test message")
    assert result is None
    assert context_window.context[-1] == "test message"


def test_clear_context():
    context_window = ContextWindow()
    context_window.add_message("test message")
    context_window.clear_context()
    assert len(context_window.context) == 0


def test_check_queue():
    context_window = ContextWindow()
# sourcery skip: no-loop-in-tests
    for i in range(11):
        context_window.add_message(f"test message {i}")
    assert len(context_window.context) == 11
    assert context_window.context[0] == "test message 0"


def test_create_prompts():
    context_window = ContextWindow()
# sourcery skip: no-loop-in-tests
    for i in range(5):
        context_window.add_message(f"test message {i}")
    prompts = context_window.create_prompts("test message 5")
    assert len(prompts) == 7
    assert prompts[0] == context_window.context
    assert prompts[6] == "test message 5"
    print(context_window.__str__())
    print(context_window.__repr__())
