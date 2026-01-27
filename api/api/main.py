from fastapi import FastAPI

app = FastAPI(title="SAT Prep API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
