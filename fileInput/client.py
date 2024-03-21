import requests

def send_request_image(filename):
    url = "http://localhost:8000/generate_caption/"
    files = {"image": open(filename, "rb")}
    response = requests.post(url, files=files)
    print(response.json())

def send_request_audio(filename):
    url = "http://localhost:8000/transcribe_audio/"
    files = {"audio": open(filename, "rb")}
    response = requests.post(url, files=files)
    print(response.json())

if __name__ == "__main__":
    image_path = "image.jpeg"
    send_request_image(image_path)

    audio_path = "audio.wav"
    send_request_audio(audio_path)
