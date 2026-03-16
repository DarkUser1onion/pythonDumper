from typing import Optional
from models import NoteOut
from repositories import NoteRepository

class NoteService:
    def __init__(self, repo: NoteRepository):
        self.repo = repo

    def create_note(self, title: str, body: Optional[str] = None) -> NoteOut:
        if not title or not title.strip():
            raise ValueError("title empty")
        return self.repo.create(title=title.strip(), body=body)

    def get_note(self, note_id: int) -> Optional[NoteOut]:
        return self.repo.get(note_id)
