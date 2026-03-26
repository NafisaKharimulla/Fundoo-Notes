from sqlalchemy.orm import Session
from src.models.notes_model import Note
from src.schemas.notes_schema import NoteCreate


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


def get_all_notes(db: Session):
    return db.query(Note).all()
