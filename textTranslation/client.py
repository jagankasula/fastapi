import requests

api = 'http://localhost:8000/translate_to_german/'

def send_request(text):
    response = requests.post(api, json={"text" : text})
    if response.status_code == 200:
        result = response.json()
        return result["result"]
    else:
        return "Error: Unable to produce results."

text = "How are you?"
translation = send_request(text)
print("Translation:", translation)
