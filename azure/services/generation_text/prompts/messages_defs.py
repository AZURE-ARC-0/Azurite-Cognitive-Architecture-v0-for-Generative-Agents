from pydantic import BaseModel
from typing import Dict, List, Optional, Literal


class MessagesDefs(BaseModel):

    role = str
    content = str
    key = Literal["primer", "messages", "context"]
    role = Literal["user", "system", "assistant"]
    messages = [{
        "role": role,
        "content": str
    }]
    json_encoders = Dict[messages]
    context = List[key[messages]] = []
    primer_path = str
    message_history = messages
    primer = Dict[str, str]
    message = Dict[str, str]

    @classmethod
    def set_default_primer(
        cls,
        primer: primer = None
    ) -> None:
        pass

    @classmethod
    def add_message(
        cls,
        message: message
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
