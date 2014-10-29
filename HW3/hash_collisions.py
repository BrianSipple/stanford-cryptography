from binascii import unhexlify, hexlify
from itertools import cylce

s1 = "48656c6c6f"
s2 = "61736b"


def hex_to_ascii_text(hex_bytes):
	return ''.join(chr(ord(x)) for x in unhexlify(hex_bytes))

def xor_hex_bytes(s1, s2):
	# We can encode all of s1 with a shorter key s2 by cycling the bytes:
	if len(s1) >= len(s2):	
		print hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(s1[-len(s2):]), cycle(unhexlify(s2)))))

	else:
		print hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(cycle(unhexlify(s1)), unhexlify(s2[:len(s1)]))))



