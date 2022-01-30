import binascii

from challenge.Challenge1 import Challenge1


class Challenge2(Challenge1):
    """
    Fixed XOR.
    Write a function that takes two equal-length buffers and produces their XOR combination.
    """

    def __init__(self, hxb: bytes = b''):
        super().__init__(hxb)

    def __eq__(self, other):
        """
        Overload eq.

        :param other: Challenge2 object
        :return: True or False
        """
        return repr(self) == repr(other)

    def __xor__(self, other):
        """
        Overload ^ xor operator.
        Self ^ other into new object.
        Both raw bytes must have the same length.

        :param other: Challenge2 object
        :return: new Challenge2 object with result of xor
        """
        if len(self.raw) != len(other.raw):
            print("[-] Parameters do not have an equal length.")
            raise ValueError("Must have equal length")

        raw = b''
        for i in range(0, len(self.raw)):
            raw += bytes([self.raw[i] ^ other.raw[i]])
        return Challenge2(binascii.hexlify(raw))

    def xor(self, hxb: bytes = b''):
        """
        Xor self with hxb, returns hex bytes with result.
        The hxb can be shorter, it will be repeated to
        match the length of self.

        :param hxb: hex bytes
        :return: hex bytes with result of xor
        """
        other_raw = binascii.unhexlify(hxb)
        result_raw = b''
        ln = len(other_raw)
        for i in range(0, len(self.raw)):
            result_raw += bytes([self.raw[i] ^ other_raw[i % ln]])
        return binascii.hexlify(result_raw)

# TODO: the __xor__ and xor have different implementations: refactor
