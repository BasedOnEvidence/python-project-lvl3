import requests


class FakeResponse:
    def __init__(self, content=b'', text='', status_code=200):
        self._content = content
        self._text = text
        self._status_code = status_code

    @property
    def content(self):
        return self._content

    @property
    def text(self):
        return self._text

    @property
    def status_code(self):
        return self._status_code

    def raise_for_status(self):
        if self.status_code > 400:
            raise requests.HTTPError
