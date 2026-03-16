from fastapi import APIRouter, Depends
from models import NoteCreate
from repositories import NoteRepository
from services import NoteService

router = APIRouter(prefix="/notes", tags=["notes"])

def get_service():
    repo = NoteRepository()
    return NoteService(repo)

@router.post("/")
def create_note(payload: NoteCreate, service: NoteService = Depends(get_service)):
    return service.create_note(payload.title, payload.body)

@router.get("/{note_id}")
def get_note(note_id: int, service: NoteService = Depends(get_service)):
    note = service.get_note(note_id)
    return note
