#!/usr/bin/env python

"""
Simple tool to cleanup /etc/portage/package.use(/*)
"""

# We import "exit" as "cexit" because pylint
from sys import argv, exit as cexit, stderr
from os.path import isdir, isfile
from lib.colorp import printc
from lib.getpackageslist import get_packages_list
from lib.process import process_packages

def main():
    """
    Cleanup /etc/portage/package.use(/*)
    """
    if len(argv) < 2:
        printc("No arguments!", 31)
        cexit(1)
    usepath = argv[1]
    if not isdir(usepath) and not isfile(usepath):
        printc(f"Unable to determine file type of {usepath}!", 31)
        cexit(1)
    packages = get_packages_list(usepath)
    (packages, removed) = process_packages(packages)
    print(packages)
    for pack in removed:
        printc(f"Removed \"{pack}\" because it isn't installed!", 33, stderr)

if __name__ == "__main__":
    main()
