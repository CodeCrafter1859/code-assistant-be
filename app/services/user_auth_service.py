import bcrypt
from app.repository.auth_repo import (
    create_user,
    get_user_credentials_by_email,
    get_user_id_by_email,
)

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

    
    _, stored_password = user
    if not bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
        return {"error": "Invalid password"}

    return {"message" : "login successful"}
