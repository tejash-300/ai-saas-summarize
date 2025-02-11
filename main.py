from fastapi import FastAPI
from transformers import pipeline
import uvicorn

# Initialize FastAPI app
app = FastAPI()

# Load BART model for text summarization
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.get("/")
def home():
    return {"message": "BART Summarization API is Running!"}

@app.get("/summarize/")
def summarize(text: str):
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return {"summary": summary[0]['summary_text']}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
