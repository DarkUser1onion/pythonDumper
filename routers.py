from fastapi import APIRouter, Depends, status, HTTPException
from models import NoteCreate
from repositories import NoteRepository
from services import NoteService

router = APIRouter(prefix="/notes", tags=["notes"])

def get_service():
    repo = NoteRepository()
    return NoteService(repo)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_note(payload: NoteCreate, service: NoteService = Depends(get_service)):
    try:
        return service.create_note(payload.title, payload.body)
    except ValueError:
        raise HTTPException(
            status_code=422,
            detail={"error": "Validation", "reason": "title_empty"}
        )

@router.get("/{note_id}")
def get_note(note_id: int, service: NoteService = Depends(get_service)):
    note = service.get_note(note_id)
    if not note:
        raise HTTPException(
            status_code=404,
            detail={"error": "Not found", "reason": "note_not_found"}
        )
    return note
