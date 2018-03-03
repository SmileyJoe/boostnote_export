# Boostnote export #

Boostnote is a note taking app that lets you keep control of your markdown notes, everything is saved
in a local directory in normal text files, however, each file is in the cson format. The idea
is to run this script and get the markdown data from the files and save it
in a specified directory so that they can be viewed in github, or any other markdown application.

# Setup #

Install the required package

- `pip install cson`

# Usage #

The script can be called with the following parameters:

- `--help` - prints out the help section for the script
- `-i` - specifies that the next parameter will be the input directory
- `-o` - specifies that the next parameter will be the output directory
- `-q` - turns off the logging
