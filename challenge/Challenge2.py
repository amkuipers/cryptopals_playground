import binascii

from challenge.Challenge1 import Challenge1


class Challenge2(Challenge1):
    """
    Fixed XOR.
    Write a function that takes two equal-length buffers and produces their XOR combination.
    If your function works properly, then when you feed it the string:
    '1c0111001f010100061a024b53535009181c' ... after hex decoding, and when XOR against:
    '686974207468652062756c6c277320657965' ... should produce:
    '746865206b696420646f6e277420706c6179'
    """

    def __init__(self, hxb: bytes = b''):
        super().__init__(hxb)

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __xor__(self, other):
        """XOR self with the other!"""
        if len(self.raw) == len(other.raw):
            raw = b''
            for i in range(0, len(self.raw)):
                raw += bytes([self.raw[i] ^ other.raw[i]])
            return Challenge2(binascii.hexlify(raw))
        else:
            print("[-] Parameters do not have an equal length.")
            return b''

    def xor(self, hxb: bytes = b''):
        """XOR self with hxb"""
        other = binascii.unhexlify(hxb)
        rawres = b''
        ln = len(other)
        for i in range(0, len(self.raw)):
            rawres += bytes([self.raw[i] ^ other[i % ln]])
        return binascii.hexlify(rawres)
