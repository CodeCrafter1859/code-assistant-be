from app.database import get_connection


def register_user(first_name, last_name, email, password):
    conn = get_connection()
    cur = conn.cursor()


    cur.execute("SELECT id FROM users WHERE email = %s;", (email,))
    existing_user = cur.fetchone()

    if existing_user:
        cur.close()
        conn.close()
        return {
            "success": False,
            "message": "user already exists"
        }
    
    query = """
    INSERT INTO users (first_name, last_name, email, password)
    VALUES (%s, %s, %s, %s)
    RETURNING id;
    """

    cur.execute(query,(
        first_name,
        last_name,
        email,
        password
    ))

    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return {
        "success": True,
        "user_id": str(user_id)
    }


def login_user(email, password):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    SELECT  email, password
    FROM users
    WHERE email = %s;
    """

    cur.execute(query,(email,))
    user = cur.fetchone()
    
    cur.close()
    conn.close()
    if not user:
        return {"error": "user not found"}

    
    _, stored_password = user
    if password != stored_password:
        return {"error": "Invalid password"}

    return {"message" : "login successful"}
