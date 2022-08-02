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
