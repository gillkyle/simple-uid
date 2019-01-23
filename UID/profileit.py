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
        generate()
        generate(2)
        generate(16)
        generate(58)
        generate(64)

    # base 2
    unpack('10110100001111000110001100000101101000110000000000001000000010')
    # base 10
    unpack('3246841075322585346')
    # base 16
    unpack('2D0F18C168C00302')
    # base 58
    unpack('8Y8TANpLKdB')
    # base 64
    unpack('2qF6C5em0K2')


# start things up!
prof = profile.Profile()
prof.runcall(main)
prof.print_stats()
