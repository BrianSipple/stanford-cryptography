from Crypto.Cipher import AES

def strxor(a, b):
	"""
	XOR of two strings
	"""
	if len(a) > len(b):
		return "".join(chr( ord(x) ^ ord(y) ) for (x, y) in zip(a[:len(b)], b) )
	else:
		return "".join(chr( ord(x) ^ ord(y) ) for (x, y) in zip(a, b[:len(a)]) )


def decrypt_cbc(key, ciphertext):
	"""
	Cipher-block chaining decryption
	"""
	key = key.decode('hex')
	ciphertext = ciphertext.decode('hex')
	
	decrypted_text = AES.new(key).decrypt(ciphertext[16:])
	decrypted_text = strxor(decrypted_text, ciphertext[:-16])
	
	return decrypted_text[:-ord(decrypted_text[-1])]


def decrypt_ctr(key, ciphertext):
	"""
	Counter-mode decrpytion
	"""
	key = key.decode('hex')
	iv = int(ciphertext[:32], 16)
	
	ciphertext = ciphertext[32:].decode('hex')

	enc_iv = ""

	for i in range(len(ciphertext) / 16 + 1):
		c_iv = hex(iv + i).rstrip("L").lstrip("0x")  # Only use what's after "0x" and before "L"
		c_iv = "0"*(32-len(c_iv)) + c_iv
		enc_iv = enc_iv + AES.new(key).encrypt(c_iv.decode('hex'))
	return strxor(enc_iv, ciphertext)


CBC = [
  ("1", "140b41b22a29beb4061bda66b6747e14", "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"),
  ("2", "140b41b22a29beb4061bda66b6747e14", "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"),
]

CTR = [
  ("3", "36f18357be4dbd77f050515c73fcf9f2", "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"),
  ("4", "36f18357be4dbd77f050515c73fcf9f2", "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451")
]


if __name__ == "__main__":

	for q, key, ciphertext in CBC:
		print "Question " + q + ": " + decrypt_cbc(key, ciphertext)

	for q, key, ciphertext in CTR:
		print "Question: " + q + ": " + decrypt_ctr(key, ciphertext)






