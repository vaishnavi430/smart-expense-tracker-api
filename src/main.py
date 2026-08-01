from fastapi import FastAPI

app = FastAPI(
    title="Smart Expense Tracker API",
    version="1.0.0",
    description="Take-home assignment for Software Engineering Apprenticeship"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Expense Tracker API"
    }