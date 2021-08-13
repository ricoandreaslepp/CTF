from Crypto.Util.number import long_to_bytes, bytes_to_long
from gmpy2 import mpz, to_binary

ALPHABET = bytearray(b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#")

# string or bytes, base in integer
def base_n_decode(bytes_in, base):
	bytes_out = to_binary(mpz(bytes_in, base=base))[:1:-1]
	return bytes_out

# I need key to decrypt
def decrypt(bytes_in, bytes_key):
	out = bytes_in
	for i in bytes_key:
		out = base_n_decode(out, ALPHABET.index(i))
	return out


def brute():
	with open("flag_enc", "rb") as f:
		enc = f.read()

	out = enc
	key = 1
	while True:
		out = enc
		print("Trying key of length:", key)
		for i in range(key):

			for base in range(2, 37):
				try:
					out = base_n_decode(out, base).decode()
					print(f"Used base: {base}")
					break
				except:
					continue
		if 'uiuctf' in out:
			return out
		else:
			key += 1

def with_key(key):
	with open("test_enc", "rb") as f:
		ct = f.read()

	rev_key = bytes(key)[::-1]

	print(decrypt(ct, bytearray(rev_key)).decode())	

print(brute())