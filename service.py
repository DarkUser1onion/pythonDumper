import logging

from typing import Optional
from models import NoteOut
from repositories import NoteRepository

logger = logging.getLogger(__name__)

class NoteService:
    def __init__(self, repo: NoteRepository):
        self.repo = repo

    def create_note(self, title: str, body: Optional[str] = None) -> NoteOut:
        logger.info(f"Service: creating note with title: {title}")
        if not title or not title.strip():
            raise ValueError("title empty")
        return self.repo.create(title=title.strip(), body=body)

    def get_note(self, note_id: int) -> Optional[NoteOut]:
        logger.info(f"Service: fetching note id: {note_id}")
        return self.repo.get(note_id)
