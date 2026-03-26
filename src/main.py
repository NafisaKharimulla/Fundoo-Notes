from fastapi import FastAPI
from src.config.database import Base, engine
from src.router import user_route
from src.models import user_model
from src.models import notes_model
from src.router import note_route

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_route.router)

app.include_router(note_route.router)


@app.get("/")
def home():
    return {"message": "Fundoo Notes API is running"}
