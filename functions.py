import os
from os import listdir
from os.path import isfile


def get_files(dir, extension):
    items = listdir(dir)
    files = []

    for item in items:
        item = dir + "/" + item
        if isfile(item):
            temp_extension = os.path.splitext(item)[1][1:]
            if temp_extension == extension:
                files.append(item)
        else:
            children = get_files(item, extension)

            for child in children:
                files.append(child)

    return files


def log(should_log, message, args=[]):
    if should_log:
        print(message.format(args))
