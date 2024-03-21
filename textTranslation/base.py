from transformers import MarianMTModel, MarianTokenizer

# Load the model and tokenizer
model_name = "Helsinki-NLP/opus-mt-en-de"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Define input text
text = "Hello, how are you?"

# Tokenize input text
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

# Perform translation
translated = model.generate(**inputs)

# Decode translated text
translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

# Print translated text
print("Translated text:", translated_text)

