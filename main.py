import shutil

import sys

from functions import *
import json
from boostnote import Boostnote

args = sys.argv
should_log = True
input_dir = "."
output_dir = "markdown"

i = 0
while i < len(args):
    arg = args[i]

    if arg == '-i':
        input_dir = args[i + 1]
        i += 1
    elif arg == '-o':
        output_dir = args[i + 1]
        i += 1
    elif arg == '-q':
        should_log = False
    elif arg == '--help':
        print('''The following commands are supported:

'-i <directory>' - specifies the input directory
'-o <directory>' - specifies the output directory
'-q' - prevents logging output''')
        exit()

    i += 1

log(should_log, 'Deleting {} directory', output_dir)
shutil.rmtree(output_dir, ignore_errors=True)
log(should_log, 'Successfully deleted')

paths = get_files(input_dir, "cson")
folders = {}

boostnote_config = json.load(open(input_dir + "/boostnote.json"))

for folder in boostnote_config['folders']:
    folders[folder['key']] = folder['name']

for path in paths:
    note = Boostnote(path)
    note.folder_name = folders.get(note.folder_id)
    note.export(should_log, output_dir)
