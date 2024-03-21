import requests
server_address = 'http://localhost:8000/'

def send_request(request_type, url):
    end_point = server_address + request_type
    response = requests.post(end_point, json={"url" : url})
    if response.status_code == 200:
        result = response.json()
        return result["result"]
    else:
        return "Error: Unable to produce results."

# Example usage
audio_url = "https://www.signalogic.com/melp/EngSamples/Orig/male.wav"  # Replace with the URL of your audio file
transcription = send_request('transcribe_audio', audio_url)
print("Transcription:", transcription)

image_url = "https://huggingface.co/datasets/Narsil/image_dummy/resolve/main/parrots.png"  # Replace with the URL of your image
caption = send_request('generate_caption', image_url)
print("Caption:", caption)
