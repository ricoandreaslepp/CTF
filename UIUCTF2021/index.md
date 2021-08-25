# UIUCTF 2021

## CEO

aircrack-ng with _rockyou.txt_ gives us the flag

<code>UIUCTF{nanotechnology}</code>

## Back to basics

Struggled with this quite a bit, cause the different datatypes and encoding seemed complex, but eventually I triumphed and the solution actually turned out to be rather simple. So it seems that the _main.py_ script just decodes the flag file with bases ranging from 2 to 36 an unknown number of times. So naturally I tried to decode by just writing a script that iterates the key length from 1 to inf and uses a try-except decoding scheme with every possible base. Since we know that the flag will start with 'uiuctf{' we can just end when we find that.

```python
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
```

Eventually we get the flag:

<code>uiuctf{r4DixAL}</code>

## dhke_intro

Another crypto challenge that was supposed to be simple, but gave me some trouble because of the different numeral systems. Eventually I realised that it's just an AES encryption and since I have the IV and the _generate_key_ function I can just brute force it. An elegant (brute-force...) solution for this challenge:

```python
def run():
    with open('output.txt', 'r') as f:
        flag = bytes.fromhex(f.read().strip())

    print("Running brute-force...")
    while True:
        try:
	    print("Found flag:", decrypt(generate_key(), flag))
            break
        except UnicodeDecodeError as e:
            continue
```
<code>uiuctf{omae_ha_mou_shindeiru_b9e5f9}</code>

## Baby_python(_fixed)

First of all we need to find a way to import os and run cat on a single line:

<code>__import__('os').system('cat flag.txt')</code>

After that we can convert the strings to int and then octal

<code>__𝘪𝘮𝘱𝘰𝘳𝘵__('\157\163').𝘴𝘺𝘴𝘵𝘦𝘮('\143\141\164\40\146\154\141\147\56\164\170\164')</code>

And last we just have to convert the whole thing to italics, since Python (for some reason) runs it the same way as a normal string. (I used this https://yaytext.com/bold-italic/)

Found the idea here:
http://jgeralnik.github.io/
https://irissec.xyz/articles/categories/other/2021-08-09/uiuctf-jails
