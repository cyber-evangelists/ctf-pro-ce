import sqlite3
from hash_pass import hash_password

db_name = "vuln-db.db"

def database_connection(database_name):
    conn = sqlite3.connect(database_name)
    return conn
    
def check_user(username, password):
    conn = database_connection(db_name)
    cursor = conn.cursor()
    select_user_sql = """
    SELECT password FROM users WHERE username = ?;
    """
    cursor.execute(select_user_sql, (username,))
    stored_password = cursor.fetchone()
    cursor.close()

    if not stored_password:
        return None     # "User not found."
    elif stored_password[0] == password:
        if username != 'carlossol':
            return False
        return True     # "Password is correct."
    else:
        return False    # "Password is incorrect."
    
    
def execute_query(query, params=None):
    conn = database_connection(db_name)
    cursor = conn.cursor()

    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        # If it's a SELECT query, fetch the results
        if query.strip().lower().startswith("select"):
            result = cursor.fetchall()
        else:
            conn.commit()
            result = None

        cursor.close()
        conn.close()

        return result

    except sqlite3.Error as e:
        conn.rollback()
        cursor.close()
        conn.close()
        return e
    
if __name__ == '__main__':
    response = check_user('carlossol', hash_password('admin@123'))
    print(response)
    
    query = "select username from users --;select password from users;"
    temp = execute_query(query)
    print(temp)