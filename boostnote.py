from functions import log

import cson
import os


class Boostnote:

    TYPE_TEXT_SNIPPET = "SNIPPET_NOTE"
    TYPE_TEXT_MARKDOWN = "MARKDOWN_NOTE"

    _content = ""
    _obj_type = ""
    _title = ""
    _folder_id = ""
    _folder_name = ""

    def __init__(self, cson_file_path):
        data = cson.load(open(cson_file_path))
        self._obj_type = data['type']
        self._title = data['title']
        self._folder_id = data['folder']

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
    def folder_id(self):
        return self._folder_id

    @property
    def folder_name(self):
        return self._folder_name

    @folder_name.setter
    def folder_name(self, value):
        self._folder_name = value

    def file_name(self):
        return self._title.lower().replace(" ", "_") + ".md"

    def directory_name(self):
        return self._folder_name.replace(" ", "_")

    def export(self, should_log,  base_directory):
        directory = base_directory + "/" + self.folder_name
        full_path = directory + "/" + self.file_name()
        if not self._content:
            log(should_log, 'Skipping: No content: {}', full_path)
        else:
            if not os.path.exists(directory):
                os.makedirs(directory)

            file = open(full_path, 'w')
            file.write(self.content)
            file.close()
            log(should_log, 'Created: {}', full_path)
