from pydantic import BaseModel

class TestSchema(BaseModel):
    prompt: str
    language: str