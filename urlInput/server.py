from fastapi import FastAPI
from transformers import pipeline
import requests
from io import BytesIO
from pydantic import BaseModel

app = FastAPI()

class Request(BaseModel):
    url: str = None

class TextRequest(BaseModel):
    data: str = None

@app.post("/transcribe_audio/")
async def transcribe_audio_api(audio_request: Request):
    transcription = transcribe_audio_huggingface(audio_request.url)
    return {"result": transcription}

@app.post("/generate_caption/")
async def generate_caption_api(image_request: Request):
    caption = generate_caption_huggingface(image_request.url)
    return {"result": caption}

def transcribe_audio_huggingface(url):
    endpoint = "https://api-inference.huggingface.co/models/facebook/wav2vec2-base-960h"
    headers = {"Authorization": "Bearer api_key"}  # Replace 'api_key' with your Hugging Face API key 
    data = {"url": url}
    
    response = requests.post(endpoint, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        transcription = result["text"]
        return transcription
    else:
        return f"Error: Unable to transcribe audio for {url}"

def generate_caption_huggingface(url):
    captioner = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base", max_new_tokens = 50)
    result = captioner(url) # https://huggingface.co/datasets/Narsil/image_dummy/resolve/main/parrots.png
    text = result[0]["generated_text"]
    return text

