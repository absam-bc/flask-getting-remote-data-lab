import requests
import json


class GetRequester:
    def __init__(self, url):
        self.url = url

    # Send a GET request and return the raw response bytes.
    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    # Convert the response bytes into Python data.
    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)
