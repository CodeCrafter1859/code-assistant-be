from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import SignUp, SignIn, VerifyOTPRequest
from app.services.user_auth_service import register_user, login_user, verify_otp_service

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
        raise HTTPException(status_code=400, detail=result["message"])

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


@auth_router.post('/verify-otp')
def verify_otp(request: VerifyOTPRequest):
    message = verify_otp_service(request.email, request.otp)
    return message