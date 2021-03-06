import unittest

from challenge.Challenge3 import Challenge3


class TestChallenge4(unittest.TestCase):
    """
    Detect single-character XOR
    One of the 60-character strings in this file has been encrypted by single-character XOR.
    Find it.
    (Your code from #3 should help.)
    """
    def test_load(self):
        """load file """
        res = b''
        file = open('tests/4.txt', 'r')
        for line in file:
            ch = Challenge3(bytes(line.strip(), 'ascii'))
            key = ch.crack()
            if key == -1:
                continue
            cr = ch.decode_xor(key)
            res = cr.raw
            break
        file.close()
        self.assertEqual(res, b'Now that the party is jumping\n')


if __name__ == '__main__':
    unittest.main()
