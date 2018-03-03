from pprint import pprint

import cson


class Boostnote:

    TYPE_TEXT_SNIPPET = "SNIPPET_NOTE"
    TYPE_TEXT_MARKDOWN = "MARKDOWN_NOTE"

    _content = ""
    _obj_type = ""
    _title = ""
    _folder = ""

    def __init__(self, cson_file_path):
        data = cson.load(open(cson_file_path))
        self._obj_type = data['type']
        self._title = data['title']
        self._folder = data['folder']

        if self.obj_type == self.TYPE_TEXT_MARKDOWN:
            self._content = data['content']

    @property
    def obj_type(self):
        return self._obj_type

    @property
    def content(self):
        return self._content

    @property
    def title(self):
        return self._title

    @property
    def folder(self):
        return self._folder
