# Find flag from random byte XOR

from pwn import xor
from random import _urandom
import sys

a = bytes.fromhex(sys.argv[1])

while 1:

	x = xor(_urandom(1), a)
	try:
		x.decode()
	except UnicodeDecodeError:
		continue

	if "ctf{" in x.decode():
		print(x)
		break
