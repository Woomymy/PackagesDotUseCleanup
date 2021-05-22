from sys import stdout
def printc(string, color, out=stdout):
    print(f"\x1b[{color}m{string} \x1b[m", file=out)
