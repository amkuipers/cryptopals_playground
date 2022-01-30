import binascii

from challenge.Challenge2 import Challenge2


class Challenge3(Challenge2):
    """
    Single-byte XOR cipher
    """

    # TODO refactor staticmethod and classmethod, see
    # https://realpython.com/instance-class-and-static-methods-demystified/

    def __init__(self, hxb: bytes = b''):
        super().__init__(hxb)

    @staticmethod
    def i2hexlified(i: int = 0) -> bytes:
        """
        Convert int into a hex bytes.
        Example: 0 to b'00'

        :param i: int to convert
        :return: hex bytes of i
        """
        return binascii.hexlify(bytes([i]))

    def is_text(self, no_text=b'"#$<>@\\^`|~') -> bool:
        """
        Check if raw string is printable.
        Use to discard raw strings with non-printable characters.
        It accepts CR, LF and printable ASCII, except no_text.
        The no_text is only based on *this* challenge.
        So !%&'()*+,-./ and :;=? and []_ and {} are considered text.

        :param no_text: optional bytes with characters that are not considered text
        :return: True when is_text else False
        """
        for c in self.raw:
            if c == 0x0a or c == 0x0d:
                continue
            if c < 0x20 or c >= 0x7f:
                return False
            if c in no_text:
                return False
        return True

    def _order(self, counts, skips=[]):
        """descending used in score()"""
        # TODO: refactor
        highest = -1
        index = -1
        for i in range(0, len(counts)):
            if i in skips:
                continue
            if counts[i] > highest:
                highest = counts[i]
                index = i
        # recursive method call
        return self._order(counts, skips + [index]) if highest > 0 else skips

    def score(self, skips=[]):
        """count the bytes score, except skips"""
        # TODO: refactor
        counts = [0] * 256
        for i in range(0, len(self.raw)):
            b = self.raw[i]
            counts[b] += 1
        return self._order(counts, skips)

    def crack(self):
        """crack single xor, based on english frequency, and printable text"""
        freq = b'ETAOIN SHRDLU' + b'etaoinshrdlu' + b'BCFGJKMPQVWXYZ' + b'bcfgjkmpqvwxyz'
        # TODO freq works probably in this challenge only
        scores = self.score()
        for i in scores:
            for j in freq:
                h = self.i2hexlified(i ^ j)
                d = Challenge3(self.xor(h))
                if d.is_text():  # notext filter default
                    # print(f"[+] cracked xor {hex(i)}^{hex(j)}={hex(i^j)}")
                    return i ^ j  # return the int
        return -1  # not found

    def decode_xor(self, key: int):
        """
        Decode the raw, using known key and XOR.
        Returning new object with decoded result.

        :param key: int with key
        :return: new Challenge3 with decoded result
        """
        return Challenge3(self.xor(self.i2hexlified(key)))
