#!/usr/bin/env python3


class BaseXConverter(object):
    '''
    Converts positive, base-10 numbers to base-X numbers using a custom alphabet.
    The base is given by the length of the alphabet specified in the constructor.
    The first character in the alphabet has a value of zero,
    the second character a value of one, and so forth.

    Examples:
        Base2:  BaseXConverter('01')
        Base2:  BaseXConverter('<>')     # custom alphabet: < is a zero value and > is a one value
        Base4:  BaseXConverter('0123')
        Base20: BaseXConverter('0123456789abcdefghij')

    See the unit tests at the bottom of the file for many examples.
    '''

    def __init__(self, alphabet):
        '''
        The base is taken from the number of characters in the alphabet.
        '''
        self.decimal_digits = '0123456789'
        self.alphabet = list(alphabet)
        self.base = len(alphabet)
        # 10110100001100011110001011100110011010110000000000111100000010
        # to come backwards and invert, you'll need a symbol for the value 13 for instance
        self.alphabet_index = {}

    def convert(self, val):
        '''
        Converts value from base 10 to base X.
        Base 10 --> 15
        Base 2  --> 1111
        The return value is a baseX integer, wrapped as a string.
        '''
        x = 0
        # iterate through letters in alphabet
        for digit in str(val):
            try:
                x = x * len(self.decimal_digits) + \
                    self.decimal_digits.index(digit)
            except ValueError:
                raise ValueError('invalid character in argument')

        # base case, while converting each digit
        if x == 0:
            bXval = self.alphabet[0]
        else:
            bXval = ''
            # find where the digit is in the given alphabet
            while x > 0:
                digit = x % len(self.alphabet)
                bXval = self.alphabet[digit] + bXval
                x = int(x // len(self.alphabet))
        return bXval

    def invert(self, bXval):
        '''
        Converts a value from base X to base 10.
        The bXval should be a baseX integer, wrapped as a string.
        Raises a ValueError if bXval contains any chars not in the alphabet.
        '''
        x = 0
        for digit in str(bXval):
            try:
                x = x * len(self.alphabet) + \
                    self.alphabet.index(digit)
            except ValueError:
                raise ValueError('invalid character in argument')

        # base case, while converting each digit
        if x == 0:
            val = self.decimal_digits[0]
        else:
            val = ''
            # find where the digit corresponds to a number
            while x > 0:
                digit = x % len(self.decimal_digits)
                val = self.decimal_digits[digit] + val
                x = int(x // len(self.decimal_digits))
        return val
