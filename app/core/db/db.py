import sqlite3

db_conn = sqlite3.connect('data/auth_server.db')

def init_db():
    cursor = db_conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS
        licenses(
            licence_key     TEXT NOT NULL UNIQUE,
            machine_id  	TEXT,
            created_at      DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
            updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
            PRIMARY KEY("licence_key")
        )
    """)
    cursor.close()


