from os.path import isfile, isdir
from os import listdir
from lib.colorp import printc

def get_packages_list(usepath):
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
            for f in files:
                for line in open(f"{usepath}/{f}").readlines():
                    lines.append(line.strip())
        except IOError:
            printc(f"Can't read dir {usepath}", 31)

    return lines
