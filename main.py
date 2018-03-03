from pprint import pprint
from functions import *
from config import *
import json
from boostnote import Boostnote

paths = get_files(BOOSTNOTE_DIR, "cson")

boostnote_config = json.load(open(BOOSTNOTE_DIR + "/boostnote.json"))

# pprint(boostnote_config)

for path in paths:
    note = Boostnote(path)
    pprint(note.folder)


