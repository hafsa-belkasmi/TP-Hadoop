import requests

def detect_fake_news(text):
    response = requests.post(
        "http://127.0.0.1:5001/detect_json",
        json={"text": text},
        timeout=120
    )

    if response.status_code == 200:
        return response.json()["result"]

    return "ERROR"