"""Write a Python program to print to stderr."""
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


eprint("foo", "bar", "baz", sep="---")