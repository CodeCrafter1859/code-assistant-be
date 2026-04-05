from app.database import get_connection


def get_user_id_by_email(email):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE email = %s;", (email,))
    user = cur.fetchone()

    cur.close()
    conn.close()
    return user


def create_user(first_name, last_name, email, hashed_password):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    INSERT INTO users (first_name, last_name, email, password)
    VALUES (%s, %s, %s, %s)
    RETURNING id;
    """

    cur.execute(
        query,
        (
            first_name,
            last_name,
            email,
            hashed_password,
        ),
    )

    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return user_id


def get_user_credentials_by_email(email):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    SELECT email, password
    FROM users
    WHERE email = %s;
    """

    cur.execute(query, (email,))
    user = cur.fetchone()

    cur.close()
    conn.close()
    return user
