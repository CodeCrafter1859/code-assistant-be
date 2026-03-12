from pydantic import BaseModel

class CodeRequest(BaseModel):
    prompt: str
    language: str