import base64
import binascii
from challenge.Challenge1 import Challenge1


class Challenge2(Challenge1):
    """
    Fixed XOR.
    Write a function that takes two equal-length buffers and produces their XOR combination.
    If your function works properly, then when you feed it the string:
    '1c0111001f010100061a024b53535009181c' ... after hex decoding, and when XOR'd against:
    '686974207468652062756c6c277320657965' ... should produce:
    '746865206b696420646f6e277420706c6179'
    """

    def __init__(self, hxb: bytes = b''):
        super().__init__(hxb)


    def __eq__(self, other):
        return repr(self) == repr(other)

    def __xor__(self, other):
        """XOR self with other!"""
        if len(self.raw) == len(other.raw):
            #print("[+] Equal length")
            #print("[+] p1 ", self.raw)
            #print("[+] p2 ", other.raw)
            raw = b''
            b'\x01\x02\x03\x05'
            for i in range(0, len(self.raw)):
                ox = self.raw[i] ^ other.raw[i] # decimal int number
                raw += bytes([ox])
                #print("[+] i ", i, ", xor #", ox)
                #oxb = ox.to_bytes(1,'big')
                #print("[+] i ", i, ", xor ", oxb)
                #oxh = binascii.hexlify(oxb)
                #print("[+] i ", i, ", xor x", oxh)
                #os = str(oxh, 'utf-8')
                #print("[+] i ", i, ", xor ", os)
                #o = o+os
            hxl = binascii.hexlify(raw)
            return Challenge2(hxl)
        else:
            print("[-] Parameters do not have an equal length.")
            return b''




