from fastapi import APIRouter
from app.schemas.code_schema import CodeRequest
from app.services.code_generation_service import generate_code

router = APIRouter()

@router.post("/generate-code")
def generate_code_api(request: CodeRequest):

    code = generate_code(
        request.prompt,
        request.language
    )

    return {
        "generated_code": code
    }