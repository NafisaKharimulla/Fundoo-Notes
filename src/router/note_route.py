from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.services import notes
from src.schemas.notes_schema import NoteCreate
from src.config.database import get_db
from src.schemas.notes_schema import NoteCreate, NoteResponse
router = APIRouter(prefix="/notes", tags=["Notes"])


# Create note
@router.post("/", response_model=NoteResponse)
def create_note_endpoint(note: NoteCreate, db: Session = Depends(get_db)):
    return notes.create_note(db, note)

# Get all notes
@router.get("/", response_model=list[NoteResponse])
def read_notes(db: Session = Depends(get_db)):
    return get_all_notes(db)

@router.put("/{note_id}", response_model=NoteResponse)
def edit_note(note_id: int, note: NoteCreate, db: Session = Depends(get_db)):
    return update_note(db, note_id, note)


@router.delete("/notes/{note_id}")
def remove_note(note_id: int, db: Session = Depends(get_db)):
    return notes.delete_note(db, note_id)
