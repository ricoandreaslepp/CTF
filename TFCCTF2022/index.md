# TFCCTF 2022

Most challenges were running on a docker so it's hard to make writeups for them after the ctf has ended, but here's one without a docker for the sake of it.

# Secrets Of Tenochtitlan

Extract all the png files, recognize that they are aztec codes, search for an aztec decoding API with no luck, use python's zxing library instead, sort the files based on exiftool's 'Time/Date Original'.

I ended up using python to extract the zip files and decode the aztecs while also using bash for exiftool and sorting the files based on the time of creation. Sloppy code, but definitely good enough for a ctf.

``` pyramid.zip, script.sh and script.py``` in the same folder, run with ```python3 script.py pyramid.zip```

```python
import subprocess
import zxing
import zipfile
import sys
import os

# first file has to be zip
def recursive_extract(filename, extract_to=os.getcwd()):

	with zipfile.ZipFile(filename) as z:
		z.extractall(path=extract_to)
	os.unlink(filename)

	for file in os.listdir():
		if os.path.splitext(file)[-1].lower() == ".zip":
			recursive_extract(file, extract_to)


try:
	recursive_extract(sys.argv[1])
except FileNotFoundError:
	pass

subprocess.call("./script.sh", shell=True)

flag = ""
r = zxing.BarCodeReader()
for img in open("out.txt"):
	flag += r.decode(img.split(" ")[0]).raw

os.unlink("./out.txt")
print(flag)
```

with script.sh being
```bash
for i in $(ls | grep png); do
    echo -n $i >> out.txt
    exiftool -DateTimeOriginal $i | cut -d ":" -f 2 >> out.txt
done

sort -o out.txt -n -k2 out.txt
```

# Keep talking and nobody goes BOOM

Honestly a really cool and unique challenge.

```python
import base64
from pwn import *
import sys

PORT = int(sys.argv[1])
R1_KEY = None
R2_KEY = None

def recvpadding(c):

	for _ in range(3):
		c.recvline()

def first():
	global R1_KEY
	r1.recvuntil(b'key: ')
	R1_KEY = r1.recvuntil(b' ', drop=True).decode()
	r1.recv(2048)
	
	r2.recv(2048)
	r2.sendline(R1_KEY.encode())

def second_helper(c):
	c.recvuntil(b'\n\n\n')
	return base64.b64decode(c.recvuntil(b'\n', drop=True).strip()).decode()

def second():
	global R2_KEY
	second_helper(r1)
	x = second_helper(r2).split(" ")
	R2_KEY = x[5]
	r1.send(R2_KEY.encode())

def third():
	r1.recvuntil(b'bomb:\n\n')
	wires = r1.recvuntil(b'\n\n', drop=True).decode().split("|")
	r1.recvuntil(b'>>> ')
	
	r2.recvuntil(b'Instructions:\n\n')
	for _ in range(5):
		r2.recvline()

	ans = []
	no_rules_apply = True
	if (wires.count("RED") > 2):
		ans.extend([3, 5])
		no_rules_apply = False

	if (wires[2] == "GREEN"):
		ans.append(1)
		no_rules_apply = False

	ignore_next = False
	if len(wires)<5:
		ans.append(3)
		ignore_next = True

	if not ignore_next:
		if wires[-2]=="BLUE":
			ans.append(len(wires)-2)

	if no_rules_apply:
		ans = [2, 6]

	r1.sendline(" ".join(map(str, ans)).encode())

def fourth_helper(c):
	c.recvuntil(b'Instructions:\n\n')
	ins = c.recvuntil(b'\n\nThese', drop=True)

	c.recvuntil(b'bomb:\n\n')
	wires = c.recvuntil(b'\n\n', drop=True).decode().split("|")
	return wires

# instructions for defusing your teammates bomb
# defuse your teammate's bomb
def fourth():
	w1 = fourth_helper(r1)
	w2 = fourth_helper(r2)

	ans1, ans2 = [], []
	# how to defuse r2
	ans2.append(w2.count("WHITE"))
	if w2.count("GREEN")>w2.count("BLUE")+w2.count("RED"):
		ans2.extend([5, 20, 27, 31])

	if w2.count("RED")%2==0:
		ans2.extend([4, 6, 19, 21, 26, 28, 30, 32])

	if w2[13]=="BLUE":
		ans2.append(14)

	# how to defuse r1
	ans1.append([i for i, n in enumerate(w1) if n=="BLACK"][2]+1)

	if w1.count("BLUE")<10 and w1.count("RED")>20:
		bw = [i for i, n in enumerate(w1) if n=="BLUE"]
		ans1.extend([bw[0]+1, bw[1]+1])

	if w1.count("GREEN")>w1.count("BLACK"):
		ans1.extend([2, 4, 15, 17, 20, 22])

	r1.recvuntil(b'>>> ')
	r2.recvuntil(b'>>> ')
	r1.sendline(" ".join(map(str, ans1)).encode())
	r2.sendline(" ".join(map(str, ans2)).encode())

def fifth_helper(key: bytes) -> "binary string encoded in bytes":
	return "0"+bin(int.from_bytes(key.encode(), 'big'))[2:]

def fifth():
	r1.recvuntil(b'>>> ')
	r2.recvuntil(b'>>> ')

	r1.sendline(fifth_helper(R2_KEY+R1_KEY))
	r2.sendline(fifth_helper(R1_KEY+R2_KEY))

	r1.recvuntil(b'flag: ')
	flag = r1.recvuntil(b'\n', drop=True)
	print(flag.decode())


def main():
	recvpadding(r1)
	r1.sendline(b'')

	recvpadding(r2)
	r2.sendline(b'')

	first()

	recvpadding(r1)
	recvpadding(r2)

	second()

	recvpadding(r1)
	recvpadding(r2)

	third()

	recvpadding(r1)
	recvpadding(r2)

	fourth()

	recvpadding(r1)
	recvpadding(r2)

	fifth()

if __name__=='__main__':

	r1 = remote('01.linux.challenges.ctf.thefewchosen.com', PORT)
	r1.recvline()
	r2 = remote('01.linux.challenges.ctf.thefewchosen.com', PORT)

	try:
		main()
	except KeyboardInterrupt:
		pass
	finally:
		r1.close()
		r2.close()
```
