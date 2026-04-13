from fastapi import FastAPI

app = FastAPI(title="HabitXP API")

@app.get("/")
def root():
    return {"message": "HabitXP API is live"}