import binascii

from challenge.Challenge2 import Challenge2


class Challenge3(Challenge2):
    """
    Single-byte XOR cipher
    The hex encoded string:

    1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
    ... has been XOR-ed against a single character. Find the key, decrypt the message.

    You can do this by hand. But don't: write code to do it for you.

    How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric.
    Evaluate each output and choose the one with the best score.

    Achievement Unlocked
    You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.
    """

    def __init__(self, hxb: bytes = b''):
        super().__init__(hxb)

    @staticmethod
    def i2hexlified(i: int = 0) -> bytes:
        """int to a hexlified bytes string: 0 to b'00' """
        return binascii.hexlify(bytes([i]))

    def is_text(self, notext=b'@~`$^<>#|"\\'):
        """ check if raw string is printable """
        for c in self.raw:
            if c == 0x0a or c == 0x0d:
                continue
            if c in notext:
                return False
            if c < 0x20 or c >= 0x7f:
                return False
        return True

    def score(self, skips=[]):
        """count the bytes score, except skips"""
        counts = [0] * 256
        for i in range(0, len(self.raw)):
            b = self.raw[i]
            counts[b] += 1
        highest = -1
        index = -1
        for i in range(0, len(counts)):
            if i in skips:
                continue
            if counts[i] > highest:
                highest = counts[i]
                index = i
        # recursive method call
        return self.score(skips + [index]) if highest > 0 else skips

    def crack(self):
        """crack single xor, based on english frequency, and printable text"""
        freq = b'ETAOIN SHRDLU'
        scores = self.score()
        for i in scores:
            for j in freq:
                h = Challenge3.i2hexlified(i ^ j)
                d = Challenge3(self.xor(h))
                if d.is_text():
                    print(f"[+] cracked xor {hex(i)}^{hex(j)}={hex(i^j)}")
                    return d
        return Challenge3(b'')
