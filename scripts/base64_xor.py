from base64 import b64decode
import sys

key, text = list(map(b64decode, sys.argv[1:]))

result = ""
for i,j in zip(key, text):
    result += chr(i^j)

print("flag:", result)
