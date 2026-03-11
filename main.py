from fastapi import FastAPI
from schemas.test_schema import TestSchema
from services.test_service import generate_code

app = FastAPI()

@app.get("/")
def home():
    return {"message":"AI Coding Assistant API"}

@app.post("/test-api")
def generate_code_api(request: TestSchema):
    
    code = generate_code(request.prompt, request.language)

    return {
        "prompt": request.prompt,
        "language": request.language,
        "generated_code": code
    }