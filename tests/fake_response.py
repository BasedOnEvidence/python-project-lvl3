class FakeResponse:
    def __init__(self, content=b'', text=''):
        self._content = content
        self._text = text

    @property
    def content(self):
        return self._content

    @property
    def text(self):
        return self._text
