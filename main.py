from pprint import pprint
from functions import *

files = get_files("./test", "txt")

for file in files:
    pprint(file)
    pprint(open(file, 'r').read())
    pprint("")


