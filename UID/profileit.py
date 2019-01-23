#!/usr/bin/env python3

#   Profiles the base conversion code.  Run this from its parent directory:
#
#       python3 profileit.py
#

try:
    import cProfile as profile
except ImportError:
    import profile
from uid import generate
from uid import unpack


def main():
    for i in range(1):
        a = generate(2)
        b = generate()
        c = generate(16)
        d = generate(58)
        e = generate(64)

    # unpack the last generated uids
    unpack(a)
    unpack(b)
    unpack(c)
    unpack(d)
    unpack(e)


# start things up!
prof = profile.Profile()
prof.runcall(main)
prof.print_stats()
