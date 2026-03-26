from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.config.database import get_db
from src.schemas.user_schema import UserCreate, UserResponse
from src.services.user import create_user, get_all_users

router = APIRouter(prefix="/users", tags=["Users"])


# Create User
@router.post("/", response_model=UserResponse)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


# Get All Users
@router.get("/", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)):
    return get_all_users(db)
