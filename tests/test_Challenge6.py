import binascii
import unittest

from challenge.Challenge6 import Challenge6


class TestChallenge6(unittest.TestCase):
    """
    Break repeating-key XOR

    It is officially on, now.
    This challenge isn't conceptually hard, but it involves actual error-prone coding.
    The other challenges in this set are there to bring you up to speed.
    This one is there to qualify you. If you can do this one, you're probably just fine up to Set 6.

    It's been base64'd after being encrypted with repeating-key XOR.

    Decrypt it.

    Here's how:

    1.
    Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.

    2.
    Write a function to compute the edit distance/Hamming distance between two strings.
        The Hamming distance is just the number of differing bits. The distance between:
    this is a test
    and
    wokka wokka!!!
    is 37. Make sure your code agrees before you proceed.

    3.
    For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes,
    and find the edit distance between them. Normalize this result by dividing by KEYSIZE.

    4.
    The KEYSIZE with the smallest normalized edit distance is probably the key.
    You could proceed perhaps with the smallest 2-3 KEYSIZE values.
    Or take 4 KEYSIZE blocks instead of 2 and average the distances.

    5.
    Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.

    6.
    Now transpose the blocks: make a block that is the first byte of every block,
    and a block that is the second byte of every block, and so on.

    7.
    Solve each block as if it was single-character XOR. You already have code to do this.

    8.
    For each block, the single-byte XOR key that produces the best looking histogram is
    the repeating-key XOR key byte for that block. Put them together and you have the key.

    This code is going to turn out to be surprisingly useful later on.
    Breaking repeating-key XOR ("Vigenere") statistically is obviously an academic exercise,
    a "Crypto 101" thing. But more people "know how" to break it than can actually break it,
    and a similar technique breaks something much more important.

    No, that's not a mistake.
    We get more tech support questions for this challenge than any of the other ones.
    We promise, there aren't any blatant errors in this text.
    In particular: the "wokka wokka!!!" edit distance really is 37.

    """
    def test_bit_count(self):
        """bit_count static"""
        self.assertEqual(Challenge6.bit_count(0x11), 2)
        self.assertEqual(Challenge6.bit_count(0x31), 3)
        self.assertEqual(Challenge6.bit_count(0xff), 8)

    def test_distance(self):
        """distance static"""
        b1 = b'this is a test'
        b2 = b'wokka wokka!!!'
        self.assertEqual(Challenge6.distance(b1, b2), 37)

    def test_cut(self):
        """break raw into key_len length strings"""
        b1 = b'abcdefghijkl'
        ch = Challenge6(binascii.hexlify(b1))
        arr = ch.cut(3)
        self.assertEqual(arr, [b'abc', b'def', b'ghi', b'jkl'])

    def test_transpose(self):
        """transpose array"""
        b1 = b'abcdefghijkl'
        ch = Challenge6(binascii.hexlify(b1))
        arr = ch.cut(3)
        trp = Challenge6.transpose(arr)
        self.assertEqual(trp, [b'adgj', b'behk', b'cfil'])

    def test__order(self):
        """order tests"""
        ch = Challenge6()
        self.assertEqual(ch._order([1, 2, 3]), [2, 1, 0])
        self.assertEqual(ch._order([3, 2, 1]), [0, 1, 2])
        # when 0 then not in result
        self.assertEqual(ch._order([0, 0, 1]), [2])
        self.assertEqual(ch._order([0, 1, 1]), [1, 2])
        # when floats
        self.assertEqual(ch._order([1.1, 1.2, 1.3]), [2, 1, 0])

    def test_normalized_distance2(self):
        """normalized distance"""
        b1 = b'000000' + b'010101'
        ch = Challenge6(b1)
        nd = ch.normalized_distance2(key_len=3)
        self.assertEqual(nd, 3/3)

    def test_normalized_distance4(self):
        """normalized distance"""
        b1 = b'000000' + b'010101'
        ch = Challenge6(b1)
        nd = ch.normalized_distance2(key_len=3)
        self.assertEqual(nd, 3/3)

    def test_find_key_size(self):
        ch = Challenge6.load_base64('tests/6.txt')
        ks = ch.find_key_sizes()
        print(f'[+] Found key sizes file {ks}')

    def test_crack_key(self):
        ch = Challenge6.load_base64('tests/6.txt')
        key = ch.crack_key()
        expected = 'Terminator X: Bring the noise'
        self.assertEqual(key, expected)
        #
        lines = ch.decode_key(key).decode('ascii')
        # song text contains this word, longer than the key
        self.assertTrue('Supercalafragilisticexpialidocious' in lines)
        self.assertTrue('Sparkamatic' in lines)

    def test_load_base64(self):
        """test load file """
        ch = Challenge6.load_base64('tests/6.txt')
        # verified with other tool
        self.assertEqual(len(ch.raw), 2876)
        self.assertEqual(len(ch.raw), 0xb3c)
        self.assertEqual(ch.raw[0], 0x1d)
        self.assertEqual(ch.raw[-1], 0x63)


if __name__ == '__main__':
    unittest.main()
