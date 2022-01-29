import unittest
from challenge.Challenge1 import Challenge1


class TestChallenge1(unittest.TestCase):
    def test_init(self):
        """Test init"""
        hxb = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        b64 = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

        ch = Challenge1(hxb)

        self.assertEqual(ch.as_hexlify(), hxb)
        self.assertEqual(ch.as_base64().strip(), b64)


if __name__ == '__main__':
    unittest.main()
