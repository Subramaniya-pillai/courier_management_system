import mysql.connector

def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",  # Example: "localhost"
            user="root",  # Example: "root"
            password="Vineeth1246@",
            database="courier_db"
        )
        if conn.is_connected():
            print("Database connected successfully!")
            return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
