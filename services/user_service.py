from db.connection import get_db
from werkzeug.security import generate_password_hash, check_password_hash

def get_all_users():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()
    conn.close()
    return [{"id": u[0], "name": u[1], "email": u[2]} for u in users]

def get_user_by_id(user_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return {"id": user[0], "name": user[1], "email": user[2]}
    return None

def create_user(data):
    try:
        name = data['name']
        email = data['email']
        password = generate_password_hash(data['password'])
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        conn.close()
        return True, "User created successfully"
    except Exception as e:
        return False, str(e)

def update_user(user_id, data):
    try:
        name = data.get('name')
        email = data.get('email')
        if not name or not email:
            return False, "Missing fields"
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
        conn.commit()
        conn.close()
        return True, "User updated successfully"
    except Exception as e:
        return False, str(e)

def delete_user(user_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    if deleted:
        return True, f"User {user_id} deleted"
    return False, "User not found"

def search_users(name):
    if not name:
        return []
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users WHERE name LIKE ?", (f"%{name}%",))
    users = cursor.fetchall()
    conn.close()
    return [{"id": u[0], "name": u[1], "email": u[2]} for u in users]

def login_user(data):
    try:
        email = data['email']
        password = data['password']
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, password FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()
        if user and check_password_hash(user[1], password):
            return {"status": "success", "user_id": user[0]}
        return {"status": "failed"}
    except Exception:
        return {"status": "error"}
