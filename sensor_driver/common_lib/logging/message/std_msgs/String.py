"""ZCM type definitions
This file automatically generated by zcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class String(object):
    __slots__ = ["data"]

    IS_LITTLE_ENDIAN = False;
    def __init__(self):
        self.data = ""

    def encode(self):
        buf = BytesIO()
        buf.write(String._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        __data_encoded = self.data.encode('utf-8')
        buf.write(struct.pack('>I', len(__data_encoded)+1))
        buf.write(__data_encoded)
        buf.write(b"\0")

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != String._get_packed_fingerprint():
            raise ValueError("Decode error")
        return String._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = String()
        __data_len = struct.unpack('>I', buf.read(4))[0]
        self.data = buf.read(__data_len)[:-1].decode('utf-8', 'replace')
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if String in parents: return 0
        tmphash = (0xf6801b5b4e7647d8) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + ((tmphash>>63)&0x1)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if String._packed_fingerprint is None:
            String._packed_fingerprint = struct.pack(">Q", String._get_hash_recursive([]))
        return String._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
