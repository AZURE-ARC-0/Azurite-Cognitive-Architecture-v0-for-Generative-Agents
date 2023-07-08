import unittest
from services.text_generation.messages import Messages


class MessagesTest(unittest.TestCase):
    def setUp(self):
        self.messages = Messages()

    def test_create_user_message(self):
        message = "Hello, how can I assist you?"

        expected_output = {"role": "user", "message": message}
        result = self.messages.create(message, role="user")
        self.assertEqual(result, expected_output)

    def test_create_assistant_message(self):
        message = "Sure, I can help with that."

        expected_output = {"role": "assistant", "message": message}
        result = self.messages.create(message, role="assistant")
        self.assertEqual(result, expected_output)

    def test_create_system_message(self):
        message = "This action requires authentication."

        expected_output = {"role": "system", "message": message}
        result = self.messages.create(message, role="system")
        self.assertEqual(result, expected_output)

    def test_create_unknown_role(self):
        message = "Unknown role message"

        expected_output = "Unknown role"
        result = self.messages.create(message, role="unknown")
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
