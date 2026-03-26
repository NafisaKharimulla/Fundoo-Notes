from pydantic import BaseModel

# request schema
class NoteCreate(BaseModel):
    title: str
    description: str
    user_id: int


# response schema
class NoteResponse(BaseModel):
    id: int
    title: str
    description: str
    user_id: int

    class Config:
        from_attributes = True
