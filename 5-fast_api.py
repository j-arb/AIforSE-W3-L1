from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import heapq

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/summarize")
async def summarize_text(request: TextRequest):
    text = request.text
    if not text:
        raise HTTPException(status_code=400, detail="Text field is required")
    
    # Tokenize sentences
    sentence_list = nltk.sent_tokenize(text)
    
    # Calculate word frequencies
    stopwords_list = set(stopwords.words("english"))
    word_frequencies = {}
    for word in nltk.word_tokenize(text):
        if word.lower() not in stopwords_list:
            if word.lower() not in word_frequencies:
                word_frequencies[word.lower()] = 1
            else:
                word_frequencies[word.lower()] += 1
    
    # Calculate sentence scores
    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies:
                if len(sent.split(" ")) < 30:  # Only consider sentences less than 30 words
                    if sent not in sentence_scores:
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]
    
    # Get the top 5 sentences as summary
    summary_sentences = heapq.nlargest(5, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    
    # Ensure summary is less than 100 words
    summary_words = word_tokenize(summary)
    if len(summary_words) > 100:
        summary = ' '.join(summary_words[:100])
    
    return {"summary": summary}

@app.post("/token_count")
async def count_tokens(request: TextRequest):
    text = request.text
    if not text:
        raise HTTPException(status_code=400, detail="Text field is required")
    
    tokens = word_tokenize(text)
    return {"token_count": len(tokens)}

# To run the app, use the command: uvicorn main:app --reload