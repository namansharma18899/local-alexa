import json
import time
import requests


class Text_to_speech:
    def __init__(self) -> None:
        pass

    def convert(self, text, result_file_loc):
        url = "https://large-text-to-speech.p.rapidapi.com/tts"
        payload = {
            "text": "Perfection is achieved not when there is nothing more to add, but rather when there is nothing more to take away."
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "03071123f7msh5a182c134adcd12p133db6jsn4672e87a3916",
            "X-RapidAPI-Host": "large-text-to-speech.p.rapidapi.com",
        }
        response = requests.post(url, json=payload, headers=headers)
        id = json.loads(response.text)["id"]
        eta = json.loads(response.text)["eta"]
        time.sleep(eta)
        response = requests.request("GET", url, headers=headers, params={"id": id})
        while "url" not in json.loads(response.text):
            response = requests.get("GET", url, headers=headers, params={"id": id})
            print("sleeping")
            time.sleep(5)
        if not "error" in json.loads(response.text):
            result_url = json.loads(response.text)["url"]
            response = requests.get(result_url)
            with open(result_file_loc, "wb") as f:
                f.write(response.content)
            print("doneeee")
