from board.database import get_pg_db_conn

def init_db():
    conn = get_pg_db_conn()
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS post;")
    cur.execute("""
        CREATE TABLE post (
            id serial PRIMARY KEY,
            created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            author TEXT NOT NULL,
            message TEXT NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Database initialized!")

if __name__ == "__main__":
    init_db()

