import unittest

from challenge.Challenge3 import Challenge3


class TestChallenge3(unittest.TestCase):
    def test_init(self):
        pass

    def test_challenge3_score(self):
        """test challenge 3 score"""
        p1 = b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
        a = Challenge3(p1)
        scores = a.score()
        expected = [120, 55, 54, 27, 49, 51, 57, 21, 40, 43, 45, 52, 58, 59, 60, 61, 62, 63, 127]
        self.assertEqual(scores, expected)

    def test_i2hexlified(self):
        """testing i2hexlified static method"""
        self.assertEqual(Challenge3.i2hexlified(1), b'01')
        self.assertEqual(Challenge3.i2hexlified(9), b'09')
        self.assertEqual(Challenge3.i2hexlified(65), b'41')

    def test_is_text(self):
        """method is_text or not"""
        self.assertTrue(Challenge3(b'41424344').is_text())
        self.assertTrue(Challenge3(b'2031397a').is_text())
        self.assertTrue(Challenge3(b'0a0d').is_text())
        self.assertFalse(Challenge3(b'00').is_text())
        self.assertFalse(Challenge3(b'08').is_text())

    def test_challenge3(self):
        """test challenge 3"""
        p1 = b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
        a = Challenge3(p1)
        d = a.crack()
        self.assertEqual(d.raw, b"Cooking MC's like a pound of bacon")

    def test_score_two(self):
        """method score """
        p1 = b'baba'
        a = Challenge3(p1)
        self.assertEqual(a.score(), [0xba])

    def test_score_skip(self):
        """method score that skips spaces"""
        p1 = b'baba202020'
        a = Challenge3(p1)
        self.assertEqual(a.score([0x20]), [0x20, 0xba])

    def test_score_twice(self):
        """method score twice"""
        p1 = b'baba202020'
        a = Challenge3(p1)
        self.assertEqual(a.score([]), [0x20, 0xba])
        self.assertEqual(a.score(a.score([])), [0x20, 0xba])


if __name__ == '__main__':
    unittest.main()
