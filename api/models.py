from pydantic import BaseModel


class PalindromeModel(BaseModel):
    text: str = ''
