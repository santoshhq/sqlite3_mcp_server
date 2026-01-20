from fastmcp import FastMCP
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE_DIR, "database.db")

mcp = FastMCP(name="Database")

# ------------------------------------------------
def get_conn():
    conn = sqlite3.connect(PATH, check_same_thread=False)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            mobileNumber TEXT NOT NULL
        )
    """)

    conn.commit()
    return conn

# ------------------------------------------------
@mcp.tool
def add_user(username: str, email: str, mobileNumber: str):
    """Add a new user to the database."""
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (username, email, mobileNumber)
        VALUES (?, ?, ?)
    """, (username, email, mobileNumber))

    conn.commit()
    conn.close()

    return {
        "status": "success",
        "message": f"User {username} added successfully"
    }

# ------------------------------------------------
@mcp.tool
def get_user_by_email(email: str):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, username, email, created_at, mobileNumber
        FROM users
        WHERE email = ?
    """, (email,))

    user = cursor.fetchone()
    conn.close()

    if not user:
        return {"status": "not_found"}

    return {
        "id": user[0],
        "username": user[1],
        "email": user[2],
        "created_at": user[3],
        "mobileNumber": user[4]
    }

# ------------------------------------------------
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0" , port=6060)
