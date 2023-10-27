import sqlite3
from hash_pass import hash_password

db_name = "vuln-db.db"

def database_connection(database_name):
    conn = sqlite3.connect(database_name)
    return conn

def create_users_table(conn):
    cursor = conn.cursor()
    create_users_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
    """
    cursor.execute(create_users_table_sql)
    conn.commit()
    cursor.close()

def user_exists(conn, username):
    cursor = conn.cursor()
    select_user_sql = """
    SELECT COUNT(*) FROM users WHERE username = ?;
    """
    cursor.execute(select_user_sql, (username,))
    count = cursor.fetchone()[0]
    cursor.close()
    return count > 0

def insert_user(username, password):
    conn = database_connection(db_name)
    if not table_exists(conn, "users"):
        create_users_table(conn)  # Create the "users" table if it doesn't exist

    try:
        if user_exists(conn, username):
            return "User with this username already exists."
        else:
            cursor = conn.cursor()
            insert_user_sql = """
            INSERT INTO users (username, password)
            VALUES (?, ?);
            """
            cursor.execute(insert_user_sql, (username, password))
            conn.commit()
            cursor.close()
            return "User inserted successfully."

    except sqlite3.Error as e:
        return f"Error inserting user: {e}"

    finally:
        conn.close()

def table_exists(conn, table_name):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    result = cursor.fetchone()
    cursor.close()
    return result is not None

if __name__ == "__main__":
    username = "ctf"
    password = "aneasyone"
    hashed_password = hash_password(password)
    result = insert_user(username, hashed_password)
    print(result)


# :

# ambassador:bake808easy194
# ctf:aneasyone