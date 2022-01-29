import unittest
from challenge.Challenge1 import Challenge1


class TestChallenge1(unittest.TestCase):
    hxb = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    b64 = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

    def test_init(self):
        """Test init"""
        ch = Challenge1(self.hxb)
        self.assertIsNotNone(ch)

    def test_as_hexlify(self):
        """method as_hexlify"""
        ch = Challenge1(self.hxb)
        self.assertEqual(ch.as_hexlify(), self.hxb)

    def test_as_base64(self):
        """method as_base64"""
        ch = Challenge1(self.hxb)
        self.assertEqual(ch.as_base64().strip(), self.b64)

    def test_repr(self):
        """method __repr__"""
        ch = Challenge1(self.hxb)
        self.assertEqual(ch.__repr__(), f'Challenge1({self.hxb})')

if __name__ == '__main__':
    unittest.main()
