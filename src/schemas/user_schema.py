from pydantic import BaseModel

# request schema (while creating user)
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    contact_number: str


# response schema (while returning user)
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    contact_number: str

    class Config:
        from_attributes = True
