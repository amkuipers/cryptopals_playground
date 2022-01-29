import unittest
from challenge.Challenge2 import Challenge2


class TestChallenge2(unittest.TestCase):
    def test_init(self):
        pass

    def test_simple(self):
        """basic check"""
        a = Challenge2(b'4040')
        b = Challenge2(b'0303')
        c = Challenge2(b'4343')
        self.assertEqual(a ^ b, c)

    def test_xor(self):
        """actual challenge 2"""
        p1 = b'1c0111001f010100061a024b53535009181c'
        p2 = b'686974207468652062756c6c277320657965'
        ou = b'746865206b696420646f6e277420706c6179'

        a = Challenge2(p1)
        b = Challenge2(p2)
        c = Challenge2(ou)
        self.assertEqual(a ^ b, c)


if __name__ == '__main__':
    unittest.main()
