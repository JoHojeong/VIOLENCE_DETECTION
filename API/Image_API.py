import requests
import json


class IMAGEAPI():
    def __init__(self):
        ...

    def infer(self):
        ...

    @staticmethod
    def send_requests(url: str,
                      headers: dict,
                      image):
        # files = {'image': open(image, 'rb')}
        files = {'image' : image}

        response = requests.post(
            url,
            files=files,
            headers=headers
        )

        rescode = response.status_code

        if (rescode==200):
            return response.text
        else:
            return rescode

    @staticmethod
    def read_json(json_path):
        return json.load(open(json_path, 'rb'))
