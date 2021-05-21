#!/usr/bin/env python

from sys import argv, exit
from lib.colorp import printc
from lib.getpackageslist import get_packages_list, clean_packages_list
from os.path import isdir, isfile

if __name__ == "__main__":
    if len(argv) < 2:
        printc("No arguments!", 31)
        exit(1)
    
    usepath = argv[1]
    if not isdir(usepath) and not isfile(usepath):
        printc(f"Unable to determine file type of {usepath}!", 31)
    packages = get_packages_list(usepath)
    packages = clean_packages_list(packages)
    categories = {}
    
    for package in packages:
        
        parts = package.split('/')
        if len(parts) != 2:
            printc(f"Skipping {package} because package is invalid", 33)
            continue
        if not parts[0] in categories:
            categories[parts[0]] = [parts[1]]
        else:
            categories[parts[0]].append(parts[1])

