from pprint import pprint
from functions import *
from config import *
import json
from boostnote import Boostnote

paths = get_files(BOOSTNOTE_DIR, "cson")
folders = {}

boostnote_config = json.load(open(BOOSTNOTE_DIR + "/boostnote.json"))

for folder in boostnote_config['folders']:
    folders[folder['key']] = folder['name']

for path in paths:
    note = Boostnote(path)
    note.folder_name = folders.get(note.folder_id)
    pprint(note.folder_name)


