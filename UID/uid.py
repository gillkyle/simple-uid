#!/usr/bin/env python3

import base2, base16, base58, base64

##############################################################################################################################################################################
#  A uid class based on time, counter, and shard id.                                                                                                                         #
#                                                                                                                                                                            #
# |                | Time Component                 | Time Component                            | Space Component                                                            |
# |----------------|--------------------------------|-------------------------------------------|----------------------------------------------------------------------------|
# | Number of Bits | 42 bits                        | 13 bits                                   | 8 bits                                                                     |
# | Description    | Milliseconds since Jan, 1970   | Counter (allows more than one UID per ms) | Shard ID (assigned explicitly to a server, process, or database)           |
# | Maximum Value  | 4,398,046,511,104 (May, 2109)  | 8,192 per ms                              | 256 unique locations                                                       |


# range is 0-255
SHARD_ID = 1

# sizes
MILLIS_BITS = 42
COUNTER_BITS = 13
SHARD_BITS = 8

# the masks
MILLIS_MASK =
COUNTER_MASK =
SHARD_MASK =


LAST_MILLIS = 0
COUNTER = 0


def generate(base=10):
    '''Generates a uid with the given base'''
    global LAST_MILLIS
    global COUNTER

    # get the millisecond, waiting if needed if we've hit the max counter
    # reset the counter if we are in a new millisecond
    # pack it up and convert base
    return uid


def pack(millis, counter, shard):
    '''Combines the three items into a single uid number'''
    return uid


def unpack(uid):
    '''Separates the uid into its three parts'''
    millis =
    counter =
    shard =
    return (millis, counter, shard)
