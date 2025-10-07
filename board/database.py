import psycopg2
import os

def get_pg_db_conn():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "psql-db"),
        database=os.environ.get("DB_NAME", "flask_db"),
        user=os.environ.get("DB_USER", "admin"),
        password=os.environ.get("DB_PASS", "P4ssw0rd"),
        port=os.environ.get("DB_PORT", "5432"),
    )

