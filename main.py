from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import heapq
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

app = FastAPI()

class TextRequest(BaseModel):
    text: str

def gemini_summarize_text(text):
    # Load API key from .env file
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    # Configure the Gemini API client
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    # Prepare the prompt
    prompt = f"Summarize the following text in a maximum of 100 tokens:\n\n{text}"

    # Send the request to the Gemini API
    # compl = genai.generate_text( model="models/gemini-1.5-flash", prompt=prompt, max_output_tokens=100)
    config = genai.types.GenerationConfig(max_output_tokens=100)
    result = model.generate_content(prompt, generation_config=config)

    # Return the generated summary
    return result.text

@app.post("/summarize")
async def summarize_text(request: TextRequest):
    text = request.text
    if not text:
        raise HTTPException(status_code=400, detail="Text field is required")
    
    summary = gemini_summarize_text(text)
    # try:
    # except:
    #     raise HTTPException(status_code=500, detail="Failed to generate summary")
    
    # print("AAA", summary)
    return {"summary": summary}

@app.post("/token_count")
async def count_tokens(request: TextRequest):
    text = request.text
    if not text:
        raise HTTPException(status_code=400, detail="Text field is required")
    
    tokens = word_tokenize(text)
    return {"token_count": len(tokens)}

# To run the app, use the command: uvicorn main:app --reload