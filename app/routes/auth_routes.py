from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import SignUp, SignIn
from app.services.user_auth_service import register_user, login_user

auth_router = APIRouter()

@auth_router.post("/signup")
def create_user(request: SignUp):

    result = register_user(
        request.first_name,
        request.last_name,
        request.email,
        request.password

    )

    if not result["success"]:
        raise HTTPException(status_code=400, message=result["message"])

    return {
        "message": "User created successfully",
        "id": result["user_id"]
    }

@auth_router.post("/signin")
def signin_user(request: SignIn):

    message = login_user(
        request.email,
        request.password

    )
    return message