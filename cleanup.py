#!/usr/bin/env python

"""
Simple tool to cleanup /etc/portage/package.use(/*)
"""

# We import "exit" as "cexit" because pylint
from sys import argv, exit as cexit
from os.path import isdir, isfile
from lib.colorp import printc
from lib.getpackageslist import get_packages_list
from lib.sort import sort_packages

if __name__ == "__main__":
    if len(argv) < 2:
        printc("No arguments!", 31)
        cexit(1)

    usepath = argv[1]
    if not isdir(usepath) and not isfile(usepath):
        printc(f"Unable to determine file type of {usepath}!", 31)
        cexit(1)
    packages = get_packages_list(usepath)
    filecontent = sort_packages(packages)
    print(filecontent)
