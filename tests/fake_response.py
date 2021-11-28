import requests


class FakeResponse:
    def __init__(self, content=b'', text='', status_code=200):
        self._content = content
        self._text = text
        self.status_code = status_code

    @property
    def content(self):
        return self._content

    @property
    def text(self):
        return self._text

    @property
    def is_connection_normal(self):
        try:
            self.raise_connection_error()
        except Exception:
            return False
        return True

    def raise_connection_error(self):
        if self.status_code > 400:
            raise requests.HTTPError
