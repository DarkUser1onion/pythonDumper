from pydantic import BaseModel
from typing import Optional

class NoteCreate(BaseModel):
    title: str
    body: str = ""

class NoteOut(BaseModel):
    id: int
    title: str
    body: Optional[str] = None
    created_at: str
