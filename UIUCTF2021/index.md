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

## Baby_python(_fixed)
italics and bold

Ref:
http://jgeralnik.github.io/
https://irissec.xyz/articles/categories/other/2021-08-09/uiuctf-jails
