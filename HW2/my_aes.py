"""
Incase rule one ever needs to be broken
"""

import sys


def random(size=16):
	with open("../res/weak_randomness.txt", 'r') as file:
		random_bytes = file.read(size)
	return random_bytes


def encrpyt(k, m):
	ciphertext = strxor(k, m)
	ciphertext = ciphertext.encode('hex')
	return ciphertext

def main(message):
	key = random(1024)
	ciphertext = encrpyt(key, message)
	return ciphertext


if __name__ == '__main__':

	if len(sys.argv) <= 1:
		print "Please provide a string for encrpytion"
	else:
		print main(sys.argv[1]) 
 

