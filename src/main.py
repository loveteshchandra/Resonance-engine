from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.core.pipeline import TranscreationPipeline

app = FastAPI(
    title="ResonanceEngine API",
    description="Generative AI backend for high-fidelity Transcreation.",
    version="0.1.0"
)

# Initialize pipeline
pipeline = TranscreationPipeline()

class TranscreateRequest(BaseModel):
    text: str
    target_language: str
    context: str = "General"

class TranscreateResponse(BaseModel):
    original: str
    transcreated: str
    meta: dict

@app.get("/")
def read_root():
    return {"message": "ResonanceEngine API is running. Visit /docs for documentation."}

@app.post("/transcreate", response_model=TranscreateResponse)
def transcreate(request: TranscreateRequest):
    try:
        result = pipeline.process(request.text, request.target_language)
        return {
            "original": request.text,
            "transcreated": result["transcreated_text"],
            "meta": result["pipeline_trace"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
