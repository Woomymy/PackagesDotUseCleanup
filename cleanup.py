#!/usr/bin/env python

from sys import argv, exit
from lib.colorp import printc

if __name__ == "__main__":
    if len(argv) < 2:
        printc("No arguments!", 31)
        exit(1)

