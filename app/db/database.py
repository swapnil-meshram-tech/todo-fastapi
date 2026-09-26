import sqlite3
from pathlib import Path
from app.core.config import settings

DB_PATH = Path(settings.DATABASE_URL.replace("sqlite:///db/test.db", ""))

sqlite3.connect("")


def get_db():
    conn = sqlite3.connect(DB_PATH, timeout=30.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("PRAGMA synchronous = ")
    conn.execute("PRAGMA busy_timeout = 5000")
    conn.execute("PRAGMA foreign_keys = ON")

    try:
        yield conn
    finally:
        conn.close()


def init_db():
    Path(settings.DATABASE_URL).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH, timeout=30.0)

    conn.commit()
    conn.close()
