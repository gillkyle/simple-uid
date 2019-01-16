from unittest import TestCase
from baseX import BaseXConverter

# Run this from its parent directory:
#
#    python3 -m unittest tests/test_baseX
#

class BaseXTester(TestCase):

    def test_base2(self):
        conv = BaseXConverter('01')
        i = 1234567890
        self.assertEqual(conv.convert(i), '{:0b}'.format(i))    # test against python's builtin
        self.assertEqual(i, conv.invert(conv.convert(i)))
