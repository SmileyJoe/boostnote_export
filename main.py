from pprint import pprint

import shutil

from functions import *
from config import *
import json
from boostnote import Boostnote

OUTPUT_DIR = "markdown"

print('Deleting {} directory'.format(OUTPUT_DIR))
shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
print('Successfully deleted')

paths = get_files(BOOSTNOTE_DIR, "cson")
folders = {}

boostnote_config = json.load(open(BOOSTNOTE_DIR + "/boostnote.json"))

for folder in boostnote_config['folders']:
    folders[folder['key']] = folder['name']

for path in paths:
    note = Boostnote(path)
    note.folder_name = folders.get(note.folder_id)
    note.export(OUTPUT_DIR)


