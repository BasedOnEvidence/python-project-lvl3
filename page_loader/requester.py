import requests


def make_request(url):
    response = requests.get(url)
    response.raise_for_status()
    return response
