import bcrypt
from app.repository.auth_repo import (
    create_user,
    get_user_credentials_by_email,
    get_user_id_by_email,
)
from app.utils.jwrt_handler import create_access_token


def register_user(first_name, last_name, email, password):
    existing_user = get_user_id_by_email(email)

    if existing_user:
        return {
            "success": False,
            "message": "user already exists"
        }

    hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    user_id = create_user(first_name, last_name, email, hash_password)

    return {
        "success": True,
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
