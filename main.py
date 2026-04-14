from fastapi import FastAPI
from app.db.session import engine, Base
from app.models import *

app = FastAPI(title="HabitXP API")

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "HabitXP API is live"}