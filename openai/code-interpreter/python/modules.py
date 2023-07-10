import sys
from contextlib import redirect_stdout
log = open("/mnt/data/modules.txt", "w")
with redirect_stdout(log):
    help("modules")

# now rewrite the file to
# - remove the intro and help comments from the file
# - split and sort the module list

'/mnt/data/modules.txt'
