import json
from services.generation_text.prompts.messages_defs import MessagesDefs
from services.system_tools.ye_logger_of_yor import get_logger
from services.system_tools.error_handling import (
    FileLoadError,
    ParseError,
    MessageError,
    HistoryError,
    ContextError,
    PrimerError,
    RoleError

)
logger = get_logger()


class MessageManager(MessagesDefs):

    def __init__(self):
        super().__init__()
        self.set_default_primer()

    def set_default_primer(self, primer=None):
        """
        Set the default primer for the model.

        Parameters:
            primer (optional): A JSON object representing the primer. If not provided, the primer will be loaded from the primer file.

        Raises:
            FileLoadError: If there was an error loading the primer file.
            ParseError: If the primer file contains invalid JSON.
            PrimerError: If there was an unexpected error setting the primer.

        Returns:
            None
        """
        try:
            if not primer:
                with open(self.primer_path, 'r', encoding='utf-8') as f:
                    line = f.readline()
                    primer = json.loads(line)
            self.primer = primer
            self.context.append(self.primer)
        except FileLoadError as e:
            raise FileLoadError(
                "Could not load primer file"
            ) from e
        except json.JSONDecodeError as e:
            raise ParseError(
                "Invalid Json format. Ensure List[Dict[str, str]]."
            ) from e
        except Exception as e:
            raise PrimerError(
                "Unexpected error setting primer"
            ) from e

    def add_message(self, message):
        """
        Adds a message to the context.

        Parameters:
            message (str): The message to be added to the context.

        Raises:
            MessageError: If there is an error adding the message.

        Returns:
            None
        """
        try:
            self.context.append(message)
        except Exception as e:
            logger.error("Error adding message: %s", e)
            raise MessageError("Error adding message") from e

    def create_message(self, message, role=None):
        """
        Creates a message with the given content and role.

        Args:
            message (str): The content of the message.
            role (str, optional): The role of the message. Defaults to None.

        Returns:
            None

        Raises:
            MessageError: If there is an error creating the message.

        Examples:
            create_message("Hello, world!", "admin")
        """
        try:
            role = self.check_roles(role)
            created_message = {"role": role, "content": message}
            self.add_message(created_message)
            self.save_message(created_message, self.message_history)
        except MessageError as e:
            print("There was an error creating the message:", e)
            raise

    def save_message(self, message, filepath):
        """
        Saves the given message to the specified file.

        Parameters:
            message (str): The message to be saved.
            filepath (str): The path of the file to save the message to.

        Raises:
            MessageError: If an error occurs while saving the message.

        Returns:
            None
        """
        try:
            with open(filepath, 'a') as file:
                file.write(json.dumps(message) + "\n")
        except Exception as e:
            raise MessageError("Unexpected error saving message") from e

    def retrieve_messages(self, filepath, num_messages=None):
        """
        Retrieve a specified number of messages from a file.

        Args:
            filepath (str): The path to the file containing the messages.
            num_messages (int, optional): The number of messages to retrieve.
                If not specified, defaults to 8.

        Returns:
            list: A list of retrieved messages.

        Raises:
            FileNotFoundError: If the message history file is not found at the given filepath.
            PermissionError: If there is no permission to read the file.
            HistoryError: If there is an unexpected error reading the message history.
        """
        try:
            if not num_messages:
                num_messages = 8
            lines = []
            with open(filepath, 'r') as file:
                for i, line in enumerate(file):
                    if i >= num_messages:
                        break
                    lines.append(json.loads(line.strip()))
            return lines
        except FileNotFoundError:
            logger.error("Message history not found at %s", filepath)
            return []
        except PermissionError:
            logger.error("No permission to read %s", filepath)
            return []
        except Exception as e:
            logger.error("Unexpected error retrieving messages: %s", e)
            raise HistoryError(
                "Unexpected error reading message history"
                ) from e

    def check_roles(self, role=None):
        """
        Check the validity of the given role.

        Parameters:
            role (str, optional): The role to be checked. Defaults to None.

        Returns:
            str: The valid role.

        Raises:
            ValueError: If the role is not one of the allowed roles.
            RoleError: If an unexpected error occurs while checking the role.
        """
        try:
            if not role:
                role = "user"
            roles = ["user", "system", "assistant"]
            if role not in roles:
                raise ValueError(f"Invalid role: {role}")
            else:
                return role
        except Exception as e:
            raise RoleError("Unexpected error checking role") from e

    def get_context(self, user_message, role=None, num_messages=None):
        """
        Retrieves the context for the chatbot conversation.

        Args:
            user_message (str): The message sent by the user.
            role (str, optional): The role of the user. Defaults to None.
            num_messages (int, optional): The number of previous messages to retrieve. Defaults to None.

        Returns:
            list: The updated conversation context.

        Raises:
            ContextError: If there was an error getting the context history.
            ContextError: If there was an unexpected error getting the context.
        """
        try:
            self.context.insert(0, self.primer)
            history = self.retrieve_messages(
                self.message_history,
                num_messages
                )
            for message in history:
                self.add_message(message)
            self.create_message(user_message, role)
            return self.context

        except ContextError as e:
            raise ContextError(
                "There was an error getting context history"
                ) from e
        except MessageError as e:
            raise ContextError(
                "Unexpected error getting context"
                ) from e
