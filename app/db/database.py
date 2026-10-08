import sqlite3
from collections.abc import Iterator
from pathlib import Path
from urllib.parse import urlparse

from app.core.config import settings

DB_PATH = Path(urlparse(settings.database_url).path.lstrip("/"))


def get_db() -> Iterator[sqlite3.Connection]:
    conn = sqlite3.connect(DB_PATH, timeout=30.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA synchronous = NORMAL")
    conn.execute("PRAGMA foreign_keys = ON")

    try:
        yield conn
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH, timeout=30.0)
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("PRAGMA synchronous = NORMAL")
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pending' 
                CHECK(status IN ('Pending', 'In Progress', 'Completed')),
            created_at TEXT NOT NULL DEFAULT (datetime('now'))
        );
    """)

    conn.commit()
    conn.close()
