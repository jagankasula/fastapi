import io
import requests
import shutil

from fastapi import FastAPI, UploadFile, File
from transformers import pipeline
from PIL import Image


app = FastAPI()

@app.post("/generate_caption/")
async def generate_caption_api(image: UploadFile = File(...)):
    # Read the image file
    contents = await image.read()    
    # Convert the binary data to an image
    image = Image.open(io.BytesIO(contents))
    caption = generate_caption_huggingface(image)
    return {"caption": caption}

@app.post("/transcribe_audio/")
async def upload_audio(audio: UploadFile = File(...)):
    with open("uploaded_audio.wav", "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)
    transcription = transcribe_audio_huggingface("uploaded_audio.wav")
    return {"transcription": transcription}

def generate_caption_huggingface(image):
    captioner = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base", max_new_tokens = 50)
    result = captioner(image)
    text = result[0]["generated_text"]
    return text

def transcribe_audio_huggingface(audio_file):
    endpoint = "https://api-inference.huggingface.co/models/facebook/wav2vec2-base-960h"
    headers = {"Authorization": "Bearer api_key"}  # Replace 'api_key' with your Hugging Face API key 
    # Read the audio file
    with open(audio_file, "rb") as file:
        audio_data = file.read()
    # Send the audio data to the Hugging Face API
    response = requests.post(endpoint, data=audio_data, headers=headers)
    if response.status_code == 200:
        result = response.json()
        transcription = result["text"]
        return transcription
    else:
        return f"Error: Unable to transcribe audio"