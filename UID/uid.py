#!/usr/bin/env python3

import base2
import base16
import base58
import base64

from datetime import datetime

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
# TODO fix the bit masks
MILLIS_MASK = (2 ** MILLIS_BITS - 1) << (COUNTER_BITS + SHARD_BITS)
COUNTER_MASK = (2 ** COUNTER_BITS - 1) << (SHARD_BITS)
SHARD_MASK = (2 ** SHARD_BITS - 1)


LAST_MILLIS = 0
COUNTER = 0
MAX_COUNTER = 2**COUNTER_BITS
EPOCH = datetime(1970, 1, 1)


def generate(base=10):
    '''Generates a uid with the given base'''
    global LAST_MILLIS
    global COUNTER

    while True:
        millis = int((datetime.utcnow() - EPOCH).total_seconds() * 1000)
        # if the counter has exceeded greatest possible size or we are at a new millisecond break the loop
        if COUNTER < MAX_COUNTER or LAST_MILLIS != millis:
            break
        time.sleep(5)

    # reset the counter if we are in a new millisecond
    COUNTER += 1

    if LAST_MILLIS != millis:
        COUNTER = 0
    LAST_MILLIS = millis

    # pack it up and convert base
    uid = pack(LAST_MILLIS, COUNTER, SHARD_ID)
    return uid


def pack(millis, counter, shard):
    '''Combines the three items into a single uid number'''
    uid = (((millis << COUNTER_BITS) + counter) << SHARD_BITS) + shard

    return uid


def unpack(uid):
    '''Separates the uid into its three parts'''

    # TODO this shouldn't use array ranges, you can use masks
    millis = uid[MILLIS_BITS:]
    counter = uid[MILLIS_BITS:COUNTER_BITS]
    shard = uid[:SHARD_BITS]
    return (millis, counter, shard)
