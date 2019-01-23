#!/usr/bin/env python3

import base2
import base16
import base58
import base64

from datetime import datetime
import time

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
# FILLED_MASK = (2 ** MILLIS_BITS - 1)
MILLIS_MASK = (2 ** MILLIS_BITS - 1) << (COUNTER_BITS + SHARD_BITS)
COUNTER_MASK = (2 ** COUNTER_BITS - 1) << (SHARD_BITS)
SHARD_MASK = (2 ** SHARD_BITS - 1)


COUNTER = 0
MAX_COUNTER = 2**COUNTER_BITS
EPOCH = datetime(1970, 1, 1)
LAST_MILLIS = int((datetime.utcnow() - EPOCH).total_seconds() * 1000)


def generate(base=10):
    '''Generates a uid with the given base'''
    global LAST_MILLIS
    global COUNTER

    millis = int((datetime.utcnow() - EPOCH).total_seconds() * 1000)

    # reset the counter if we are in a new millisecond
    COUNTER += 1

    if LAST_MILLIS != millis:
        COUNTER = 0
    LAST_MILLIS = millis

    # pack it up
    uid = pack(LAST_MILLIS, COUNTER, SHARD_ID)
    # convert uid based on the given base using the converter class
    if (base == 10):
        # already in base 10
        converted_uid = uid
    elif (base == 2):
        converted_uid = base2.convert(uid)
    elif (base == 16):
        converted_uid = base16.convert(uid)
    elif (base == 58):
        converted_uid = base58.convert(uid)
    elif (base == 64):
        converted_uid = base64.convert(uid)
    else:
        converted_uid = uid
    print(converted_uid)
    return converted_uid


def pack(millis, counter, shard):
    '''Combines the three items into a single uid number'''
    uid = (((millis << COUNTER_BITS) | counter) << SHARD_BITS) | shard
    return uid


def unpack(uid):
    '''Separates the uid into its three parts'''
    # TODO this shouldn't use array ranges, you can use masks
    uid_length = len(uid)
    if (uid_length >= 62):
        base = 2
    elif (uid_length == 19):
        base = 10
    elif (uid_length == 16):
        base = 16
    elif (uid_length == 11):
        if any(x in "0OIl" for x in uid):
            base = 64
        else:
            base = 58
    else:
        base = 10

    if (base == 10):
        inverted_uid = uid
    elif (base == 2):
        inverted_uid = base2.invert(uid)
    elif (base == 16):
        inverted_uid = base16.invert(uid)
    elif (base == 58):
        inverted_uid = base58.invert(uid)
    elif (base == 64):
        inverted_uid = base64.invert(uid)
    else:
        inverted_uid = uid

    print("---inverted---")
    print(inverted_uid)
    millis = int(inverted_uid) & MILLIS_MASK
    counter = int(inverted_uid) & COUNTER_MASK
    print(bin(counter))
    shard = int(inverted_uid) & SHARD_MASK
    print(bin(shard))
    print(millis, counter, shard)

    return (millis, counter, shard)
