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


def main():
    print('do something here')


# start things up!
prof = profile.Profile()
prof.runcall(main)
prof.print_stats()
