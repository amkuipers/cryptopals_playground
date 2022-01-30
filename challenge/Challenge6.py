import base64
import binascii

from challenge.Challenge3 import Challenge3


class Challenge6(Challenge3):
    """
    breaking
    """

    def __init__(self, hxb: bytes = b''):
        super().__init__(hxb)

    @staticmethod
    def bit_count(int_type):
        count = 0
        while int_type:
            int_type &= int_type - 1
            count += 1
        return count

    @staticmethod
    def distance(raw1, raw2):
        """
        Write a function to compute the edit distance/Hamming distance between two strings.
        The Hamming distance is just the number of differing bits. The distance between:
        this is a test
        and
        wokka wokka!!!
        is 37. Make sure your code agrees before you proceed.
        """
        # both strings are same length
        # loop each char
        # xor them
        # count the bits that are 1 (not the same)
        if len(raw1) == len(raw2):
            sum = 0
            for i in range(0, len(raw1)):
                x = raw1[i] ^ raw2[i]
                diff = Challenge6.bit_count(x)
                # print("[+] distance ", i, ":", hex(b1[i]), " ^ ", hex(b2[i]), " = ", hex(x), " bits1: ", diff)
                sum += diff
            return sum
        else:
            print("[-] Length is not equal")
            return -1

    @staticmethod
    def transpose(arr):
        """from array, take every first char, put in first new array, ..."""
        la = len(arr)  # length of array
        ls = len(arr[0])  # length of a string
        answer = []
        for i in range(0, ls):
            s = b''
            for j in range(0, la):
                ch = arr[j][i:i + 1]
                s += ch
            answer.append(s)
        return answer

    def cut(self, key_len=3):
        """cut raw into array with strings of s length"""
        a = []
        for i in range(0, len(self.raw), key_len):
            p = self.raw[i:i + key_len]
            a.append(p)
        return a

    def normalized_distance2(self, key_len):
        p1 = self.raw[0:key_len]
        p2 = self.raw[key_len:key_len * 2]
        distance = Challenge6.distance(p1, p2)  # bytes
        normalized = distance / key_len
        return normalized

    def normalized_distance4(self, key_len):
        p1 = self.raw[0:key_len]
        p2 = self.raw[key_len:key_len * 2]
        p3 = self.raw[key_len*2:key_len * 3]
        p4 = self.raw[key_len*3:key_len * 4]
        # 12 13 14 23 24 34
        norm12 = Challenge6.distance(p1, p2) / key_len
        norm13 = Challenge6.distance(p3, p4) / key_len
        norm14 = Challenge6.distance(p3, p4) / key_len
        norm23 = Challenge6.distance(p2, p3) / key_len
        norm24 = Challenge6.distance(p3, p4) / key_len
        norm34 = Challenge6.distance(p3, p4) / key_len
        normalized = (norm12 + norm13 + norm14 + norm23 + norm24 + norm34) / 6
        return normalized

    def find_key_sizes(self):
        ln = len(self.raw)
        maxkeysize = 40 if ln/2 > 40 else int(ln/2)
        minkeysize = 2
        print(f'[+] Looking for key sizes {minkeysize}..{maxkeysize}')
        counts = [0] * maxkeysize
        # key size 1 is the normal xor crack method.
        # counts[0] and [1] stay 0 since these key sizes are not used here
        for key_len in range(minkeysize, maxkeysize):
            if ln > key_len*4:
                nd = self.normalized_distance4(key_len)
            else:
                nd = self.normalized_distance2(key_len)
            counts[key_len] = nd
        # print(f'[+] key size, normalized distance {counts}')
        keysizes = self._order(counts, [])
        return keysizes  # pop() = last is the most probable key size

    @staticmethod
    def load_base64(filename='tests/6.txt'):
        """load file """
        b64 = ''
        file = open(filename, 'r')
        for line in file:
            b64 += line.strip()  # remove newline
        file.close()
        # return new object
        raw = base64.b64decode(b64)
        return Challenge6(binascii.hexlify(raw))

    def crack_key(self, try_keys=3):
        """crack multi character key"""
        kss = self.find_key_sizes()
        for i in range(0, try_keys):  # try for 3 most probable key sizes
            ks = kss.pop()      # last + remove from list
            arr = self.cut(ks)    # cut in parts of key size
            tra = self.transpose(arr)  # flip
            keys = ''
            stopped = False
            # per transposed block
            for j in range(0, ks):
                # print(f'[+] Cracking block {j}')
                cha = Challenge6(binascii.hexlify(tra[j]))
                cra = cha.crack()
                if cra == -1:
                    stopped = True  # not found
                    break
                keys += chr(cra)
            if not stopped:
                print(f'Cracked and found {keys}')
                return keys  # key text
            else:
                continue  # next key size
        return ''  # no key

    def decode_key(self, key=''):
        """decode with string key"""
        hxl = self.xor(binascii.hexlify(bytes(key, 'ascii')))
        dec = binascii.unhexlify(hxl)
        print(f'Decoded to {dec}')
        return dec  # decoded bytes
