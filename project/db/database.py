import sqlite3
import re

def check_flag_from_db(database_path, pattern):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute("SELECT flag FROM flags LIMIT 1")
        flag = cursor.fetchone()

        if flag is not None:
            if re.match(pattern, flag[0]):
                return f"Flag matches the pattern: {flag[0]}"
            else:
                return "Flag does not match the pattern."
        else:
            return "No flag found in the database."
    except sqlite3.Error as e:
        return f"Database error: {e}"
    finally:
        if conn:
            conn.close()

database_path = "data.db"
pattern = r'^[a-zA-Z0-9]{18}$'

result = check_flag_from_db(database_path, pattern)
print(result)
