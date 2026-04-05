from datetime import datetime, timedelta
import bcrypt
from app.repository.auth_repo import (
    create_user,
    get_user_by_email,
    get_user_credentials_by_email,
    get_user_id_by_email,
    verify_user,
)
from app.utils.email_verify_smtp import send_otp_email
from app.utils.jwrt_handler import create_access_token
import random



def generate_otp():
    return str(random.randint(100000, 999999))


def register_user(first_name, last_name, email, password):
    existing_user = get_user_id_by_email(email)

    if existing_user:
        return {
            "success": False,
            "message": "user already exists"
        }

    hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    otp = generate_otp()
    otp_expiry = datetime.utcnow() + timedelta(minutes=5)
    user_id = create_user(first_name, last_name, email, hash_password, otp, otp_expiry, is_verified=False)

    send_otp_email(email, otp)

    return {
        "success": True,
        "message": "OTP sent to email",
        "user_id": str(user_id)
    }


def login_user(email, password):
    user = get_user_credentials_by_email(email)

    if not user:
        return {"error": "user not found"}

    
    id, stored_password = user
    if not bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
        return {"error": "Invalid password"}

    access_token = create_access_token({"id": id, "email": email})

    return {
        "success": True,
        "access_token": access_token,
        "token_type": "bearer"
    }


def verify_otp_service(email, otp):
    user = get_user_by_email(email)

    if not user:
        return {"success": False, "message": "user not found"}

    user_id, stored_otp, otp_expiry, is_verified = user

    if is_verified:
        return {"success": False, "message": "user already verified"}

    if stored_otp != otp:
        return {"success": False, "message": "invalid otp"}

    if datetime.utcnow() > otp_expiry:
        return {"success": False, "message": "otp expired"}

    verify_user(email)

    return {
        "success": True,
        "message": "account verified successfully"
    }