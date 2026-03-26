from sqlalchemy.orm import Session
from src.models.user_model import User
from src.schemas.user_schema import UserCreate


def create_user(db: Session, user: UserCreate):
    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password,
        contact_number=user.contact_number
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_all_users(db: Session):
    return db.query(User).all()
