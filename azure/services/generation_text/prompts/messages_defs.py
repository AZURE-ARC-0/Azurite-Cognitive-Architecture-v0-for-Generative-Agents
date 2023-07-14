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
        pass

    @classmethod
    def add_message(
        cls,
        message: Dict[str, str] = message
    ) -> None:
        pass

    @classmethod
    def create_message(
        cls,
        message: message,
        role: Optional[role] = None
    ) -> None:
        pass

    @classmethod
    def save_message(
        cls,
        message: message,
        filepath: str
    ) -> None:
        pass

    @classmethod
    def retrive_messages(
        cls,
        filepath: str,
        num_messages: Optional[int] = None
    ) -> List[Dict[str, str]]:
        pass

    @classmethod
    def check_roles(
        cls,
        role: str
    ) -> str:
        pass

    @classmethod
    def get_context(
        cls,
        message: str,
        role: Optional[role] = None,
        num_messages: Optional[int] = None
    ) -> List[Dict[str, str]]:
        pass
