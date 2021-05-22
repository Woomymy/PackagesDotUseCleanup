"""
Color-printing related module
"""

from sys import stdout
# Use 97(white) as default color
def printc(string, color=97, out=stdout):
    """
    Print a text in color using ANSI escape codes
    Example:
    ```python
    from sys import stderr
    red_ansi_code = 31
    printc("Hello", red_ansi_code) # Will print "Hello" on standart output
    printc("Hello, world", red_ansi_code, stderr) # Will print "Hello, world" on the stderr
    ```
    """
    print(f"\x1b[{color}m{string} \x1b[m", file=out)
