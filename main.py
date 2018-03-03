from pprint import pprint

import shutil

import sys

from functions import *
import json
from boostnote import Boostnote

args = sys.argv
shouldLog = True
inputDir = "."
outputDir = "markdown"

i = 0
while i < len(args):
    arg = args[i]

    if arg == '-i':
        inputDir = args[i + 1]
        i += 1
    elif arg == '-o':
        outputDir = args[i + 1]
        i += 1
    elif arg == '-q':
        shouldLog = False
    elif arg == '--help':
        print('''The following commands are supported:

'-i <directory>' - specifies the input directory
'-o <directory>' - specifies the output directory
'-q' - prevents logging output''')
        exit()

    i += 1

print('Deleting {} directory'.format(outputDir))
shutil.rmtree(outputDir, ignore_errors=True)
print('Successfully deleted')

paths = get_files(inputDir, "cson")
folders = {}

boostnote_config = json.load(open(inputDir + "/boostnote.json"))

for folder in boostnote_config['folders']:
    folders[folder['key']] = folder['name']

for path in paths:
    note = Boostnote(path)
    note.folder_name = folders.get(note.folder_id)
    note.export(outputDir)


