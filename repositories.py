import os
import sqlite3
from datetime import datetime, timezone

DB_PATH = os.getenv("DB_PATH", os.path.join(os.path.dirname(__file__), "data", "notes.db"))
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def get_conn():
    conn = sqlite3.connect(DB_PATH, detect_types=sqlite3.PARSE_DECLTYPES)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    with conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                body TEXT,
                created_at TEXT NOT NULL
            )
            """
        )
    conn.close()

class NoteRepository:
    def create(self, title: str, body: str | None):
        conn = get_conn()
        try:
            cur = conn.cursor()
            now = datetime.now(timezone.utc).isoformat()
            cur.execute(
                "INSERT INTO notes (title, body, created_at) VALUES (?, ?, ?)",
                (title, body, now)
            )
            note_id = cur.lastrowid
            conn.commit()

            cur.execute(
                "SELECT id, title, body, created_at FROM notes WHERE id = ?",
                (note_id,)
            )
            row = cur.fetchone()
            return NoteOut(**row)
        finally:
            conn.close()
