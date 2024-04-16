import sqlite3

db_conn = sqlite3.connect('data/auth_server.sqlite', check_same_thread=False)

def init_db():
    cursor = db_conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS
        licenses(
            license_key     TEXT NOT NULL UNIQUE,
            machine_id  	TEXT,
            created_at      DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
            updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
            PRIMARY KEY("license_key")
        )
    """)
    cursor.close()


