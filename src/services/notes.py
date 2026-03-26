from sqlalchemy.orm import Session
from src.models.notes_model import Note
from src.schemas.notes_schema import NoteCreate
from src.utils.logger import logger


def create_note(db: Session, note: NoteCreate):
    new_note = Note(
        title=note.title,
        description=note.description,
        user_id=note.user_id
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note

logger.info("Note created successfully")

def get_all_notes(db: Session):
    return db.query(Note).all()


def update_note(db: Session, note_id: int, note: NoteCreate):
    existing_note = db.query(Note).filter(Note.id == note_id).first()

    if existing_note is None:
        return {"message": "Note not found"}

    existing_note.title = note.title
    existing_note.description = note.description

    db.commit()
    db.refresh(existing_note)

    return existing_note

def delete_note(db: Session, note_id: int):
    note = db.query(Note).filter(Note.id == note_id).first()

    if not note:
        # This will raise proper HTTP exception instead of returning None
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Note not found")

    db.delete(note)
    db.commit()

    return {"message": "Note deleted successfully"}
