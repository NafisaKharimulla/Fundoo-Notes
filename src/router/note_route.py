from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.config.database import get_db
from src.schemas.notes_schema import NoteCreate, NoteResponse
from src.services.notes import create_note, get_all_notes

router = APIRouter(prefix="/notes", tags=["Notes"])


# Create note
@router.post("/", response_model=NoteResponse)
def add_note(note: NoteCreate, db: Session = Depends(get_db)):
    return create_note(db, note)


# Get all notes
@router.get("/", response_model=list[NoteResponse])
def read_notes(db: Session = Depends(get_db)):
    return get_all_notes(db)
