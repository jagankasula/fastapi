from fastapi import FastAPI
from transformers import MarianMTModel, MarianTokenizer
from pydantic import BaseModel

app = FastAPI()

# Load the model and tokenizer
translation_model_name = "Helsinki-NLP/opus-mt-en-de"
tokenizer = MarianTokenizer.from_pretrained(translation_model_name)
translation_model = MarianMTModel.from_pretrained(translation_model_name)

class Request(BaseModel):
    text: str = None

@app.post("/translate_to_german/")
async def translate_to_german_api(request: Request):
    translation = translate_to_german(request.text)
    return {"result": translation}

def translate_to_german(data):
    inputs = tokenizer(data, return_tensors="pt", padding=True, truncation=True)
    translated = translation_model.generate(**inputs)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text

