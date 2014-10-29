import sys
from Crypto.Hash import SHA256
from binascii import hexlify

video_file = 'week6-collision-resistance-lecture.mp4'
#video_file = 'birthday-attack-lecture.mp4'

def make_bytes_array(filepath):

	bytes_array = []

	with open(filepath, 'rb') as f:
	
		byte = f.read(1024)

		while len(byte) != 0:
			bytes_array.append(byte)
			byte = f.read(1024)

	return bytes_array



### Compute hashes for the bytes -- starting from the last one and ending at the first
def compute_small_hash_on_bytes_array(bytes_array):
	
	last_hash = ""
	for i in range(len(bytes_array)-1, -1, -1):
		
		h = SHA256.new()
		byte = bytes_array[i]

		if last_hash == "":
			h.update(byte)

		else:
			h.update(byte + last_hash)

		last_hash = h.digest()

	return hexlify(last_hash)


if __name__ == '__main__':

	if len(sys.argv) > 1:
		filepath = sys.argv[1]
	else:
		filepath = video_file

	print("Making bytes array for {}".format(filepath))
	bytes_array = make_bytes_array(filepath)
	print("Computing hash...")
	last_hash = compute_small_hash_on_bytes_array(bytes_array)
	print("Last hash computed for {}: \n{}".format(filepath, last_hash))




