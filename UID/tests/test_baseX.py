from unittest import TestCase
from baseX import BaseXConverter

# Run this from its parent directory:
#
#    python3 -m unittest tests/test_baseX
#


class BaseXTester(TestCase):

    def test_base2(self):
        conv = BaseXConverter('01')
        i = 15
        # python has built in binary conversion with {:0b}, compare against our converter
        # test against python's builtin
        self.assertEqual(conv.convert(i), '{:0b}'.format(i))
        self.assertEqual(str(i), conv.invert(conv.convert(i)))

    def test_base10(self):
        conv = BaseXConverter('0123456789')
        i = 32
        self.assertEqual(conv.convert(i), '32')
        self.assertEqual(str(i), conv.invert(conv.convert(i)))
