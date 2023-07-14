from pydantic import BaseModel
from typing import Dict, List, Optional, Literal


class MessagesDefs(BaseModel):
    context: List[Dict[str, str]] = []
    primer: Dict[str, str] = []
    message_history: str = "azure/static/messages/message_history.jsonl"
    primer_path: str = "azure/static/templates/primers.jsonl"
    message: Dict[str, str] = None
    messages: List[Dict[str, str]] = []
    primer: Optional[Dict[str, str]] = []
    role: Optional[Literal["user", "assistant", "system"]] = "user"


    @classmethod
    def set_default_primer(
        cls,
        primer: primer = None
    ) -> None:
        """
        Set the default primer for the class.

        Parameters:
            primer (primer, optional): The primer to set as the default. Defaults to None.

        Returns:
            None
        """
        pass

    @classmethod
    def add_message(
        cls,
        message: Dict[str, str] = message
    ) -> None:
        """
        Adds a message to the class.

        Args:
            message (message): The message to be added.

        Returns:
            None
        """
        pass

    @classmethod
    def create_message(
        cls,
        message: message,
        role: Optional[role] = None
    ) -> None:
        """
        Create a new message.

        Args:
            message: The content of the message.
            role: The role of the user sending the message (optional).

        Returns:
            None.
        """

        pass

    @classmethod
    def save_message(
        cls,
        message: message,
        filepath: str
    ) -> None:
        """
        Save a message to a file.

        Args:
            message: The message to be saved.
            filepath: The path to the file where the message will be saved.

        Returns:
            None.
        """
        pass

    @classmethod
    def retrive_messages(
        cls,
        filepath: str,
        num_messages: Optional[int] = None
    ) -> List[Dict[str, str]]:
        """
        Retrieves a list of messages from the specified file.

        Args:
            filepath (str): The path to the file containing the messages.
            num_messages (Optional[int], optional): The maximum number of messages to retrieve. Defaults to None.

        Returns:
            List[Dict[str, str]]: A list of dictionaries representing each message, with keys for 'sender' and 'message'.

        """
        pass

    @classmethod
    def check_roles(
        cls,
        role: str
    ) -> str:
        """
        Check the roles of a user.

        Args:
            role (str): The role of the user.

        Returns:
            str: The result of checking the roles.
        """
        pass

    @classmethod
    def get_context(
        cls,
        message: str,
        role: Optional[role] = None,
        num_messages: Optional[int] = None
    ) -> List[Dict[str, str]]:
        """
        Retrieves the context of a message.

        Args:
            message (str): The message to retrieve the context for.
            role (Optional[role], optional): The role of the user requesting the context. Defaults to None.
            num_messages (Optional[int], optional): The number of messages to retrieve. Defaults to None.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing the context information.
        """
        pass
