# Client-Server Model using FASTAPI

This repository implements a client-server model for obtaining image captions, audio transcriptions, and text translations by sending API requests using the Python FastAPI framework.


For testing the client-server model on our local machine, for the sake of simplicity, custom-trained models are not utilized in the server code. Instead, we employ pre-trained Hugging Face models. The server leverages Hugging Face APIs to fulfill client requests.

## Installation

To set up the project, first install the required dependencies by running the following command:

```bash
pip install -r requirements.txt 
```

## Execution
Hugging Face API Key: To use the fileInput and urlInput functionalities, you need to obtain an API key from Hugging Face. You can acquire the API key from [here](https://huggingface.co/settings/tokens). Once obtained, replace the placeholder 'api_key' in server.py with your actual API key.

### Running the Server and Client:

Navigate to the folder of interest using the command line (e.g., cd urlInput).
- Running the Server and Client:
  Navigate to the folder of interest using the command line (e.g., cd urlInput).
  Start the server by running the command:
  ```bash
  uvicorn server:app --reload
  ```
- Run the client script using Python:
  ```bash
  python3 client.py
  ```
### Testing with Swagger UI:
- Start the server by running the command:
  ```bash
  uvicorn server:app --reload
  ```
- After starting the server, copy the HTTP address of the server and append '/docs' to it. 
  For example: http://127.0.0.1:8000/docs
- Open this address in your browser. Now, the APIs can be tested from the Swagger UI.

## Folder Information
### fileInput
Server uses hugginface APIS to handle Client requests.
- The client sends a **file** in the API request to the server.
- The server processes the file and sends the response back to the client.
- For testing with different inputs, specify the path of your local file in the image_path or audio_path variables in client.py file.

### urlInput
Server uses hugginface APIS to handle Client requests.
- The client sends a **publicly accessible URL** of an image or an audio file in the API request to the server.
- The server processes the URL and sends the response back to the client.
- For testing with different inputs, modify the URL in the image_url or audio_url variables in client.py file.

### textTranslation
The server maintains pre-trained text translation model in it and processes client requests by itself.
- The client sends text (in English) in the API request to the server.
- The server processes the text and sends the translated response back to the client.
- For testing with different inputs, change the text in the text variable in client.py file.