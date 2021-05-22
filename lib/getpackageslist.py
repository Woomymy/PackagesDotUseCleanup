"""
Helper to get packages list and removing comments
"""
from os.path import isfile, isdir
from os import listdir
from lib.colorp import printc

def get_packages_list(usepath):
    """
    Read a file / a dir and get package.use directives
    """
    lines = []
    if isfile(usepath):
        try:
            for line in open(usepath).readlines():
                lines.append(line.strip())
        except IOError:
            printc(f"Can't open file {usepath}", 31)
    elif isdir(usepath):
        try:
            files = listdir(usepath)
            for usefile in files:
                for line in open(f"{usepath}/{usefile}").readlines():
                    lines.append(line.strip())
        except IOError:
            printc(f"Can't read dir {usepath}", 31)

    return lines

def clean_packages_list(packages):
    """
    Remove comments from the package list
    """
    lines = []
    for line in packages:
        if not line.startswith("#"):
            lines.append(line)
    return lines
