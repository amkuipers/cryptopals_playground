import base64
import binascii


class Challenge1:
    """
    Convert hex to base64.
    Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
    """

    def __init__(self, hxb: bytes = b''):
        """init with hex bytes that will be converted to raw"""
        self.raw = binascii.unhexlify(hxb)
        # self.hxb = hxb

    def as_base64(self) -> bytes:
        """return the base64 encoded of the raw bytes"""
        return base64.encodebytes(self.raw)

    def as_hexlify(self) -> bytes:
        return binascii.hexlify(self.raw)

    def __str__(self):
        """debug str"""
        s = {
            "bytes": self.raw,
            "base64": self.as_base64(),
            "hex": self.as_hexlify()
        }
        return str(s)

    def __repr__(self):
        """representative str"""
        return f'Challenge1({self.as_hexlify()})'
