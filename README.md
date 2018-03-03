# Boostnote export #

Boostnote is a note taking app that lets you keep control of your markdown notes, everything is saved
in a local directory in normal text files, however, each file contains metadata for boostnote. The idea
is to run this script and remove all meta data from the files and save the plain markdown files
in an `export` directory so that they can be viewed in github.

# Setup #

Install the cson package

- `pip install cson`

Create a `config.py` file in the root directory of the project and add the following config variables:

- `BOOSTNOTE_DIR` - the directory where you notes are stored
