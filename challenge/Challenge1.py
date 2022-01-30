import base64
import binascii


class Challenge1:
    """
    Convert hex to base64.
    Always operate on raw bytes, never on encoded strings.
    Only use hex and base64 for pretty-printing.
    """

    def __init__(self, hxb: bytes = b''):
        """init with hex bytes that is stored as raw bytes"""
        self.raw = binascii.unhexlify(hxb)

    def as_base64(self) -> bytes:
        """return the base64 encoded of the raw bytes"""
        return base64.encodebytes(self.raw)

    def as_hexlify(self) -> bytes:
        """return the hex bytes of the raw bytes"""
        return binascii.hexlify(self.raw)

    def __str__(self):
        """show structure with 3 representations of the raw bytes"""
        s = {
            "bytes": self.raw,
            "base64": self.as_base64(),
            "hex": self.as_hexlify()
        }
        return str(s)

    def __repr__(self):
        """representative str, like the constructor"""
        return f'Challenge1({self.as_hexlify()})'
        # TODO what is the {xx!r} I see in examples