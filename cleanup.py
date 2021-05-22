#!/usr/bin/env python

from sys import argv, exit, stderr
from lib.colorp import printc
from lib.getpackageslist import get_packages_list
from lib.sort import sort_packages
from os.path import isdir, isfile

if __name__ == "__main__":
    if len(argv) < 2:
        printc("No arguments!", 31)
        exit(1)
    
    usepath = argv[1]
    if not isdir(usepath) and not isfile(usepath):
        printc(f"Unable to determine file type of {usepath}!", 31)
    packages = get_packages_list(usepath)
    filecontent = sort_packages(packages)
    print(filecontent)
