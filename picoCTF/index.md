## Easy Peaasy


## Cookies

<code>Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:64944/</code>

A really fun challenge. After opening the page in Burp Suite and examining the HTTP requests we find that a value _name_ is passed with each query:

![Capture](https://user-images.githubusercontent.com/52963102/125533318-157b8dfc-d34a-48c6-aec6-76227eede20c.PNG)

Now originally I changed the value by hand till I reached _name=18_ and that gives us the flag, but I wanted to try and simulate requests with as well.

It really didn't take long, I just had to fill the header with the data needed:
<code> headers = { 
	'Referer' : 'http://mercury.picoctf.net:64944/',
	'Cookie' : 'name='+str(i),
	'Connection' : 'close'
}
</code>

And then loop from -1 to 100 till we find _pico_ in _response.text_. Full code here:
https://github.com/ricoandreaslepp/CTF/blob/main/cookies.py

<code>picoCTF{3v3ry1_l0v3s_c00k135_cc9110ba}</code>

## Wireshark doo dooo do doo...

<code>Can you find the flag? </code>

After following the TCP streams and reaching _tcp.stream eq 5_ we find a suspicious looking _GET_ request that gets a response from the server with some encrypted data.

![http_request](https://user-images.githubusercontent.com/52963102/126046587-c91c4cdf-d4fb-471f-b49a-6dbc77c33d57.PNG)

I suspected it was ROT13 so I made a quick implementation in Python and ended up with:

![flag](https://user-images.githubusercontent.com/52963102/126046615-6cb70e2f-9513-421d-942f-7bca23a31194.PNG)

The code can of course be found at https://github.com/ricoandreaslepp/ciphers/blob/main/ROT13.py

<code>The flag is picoCTF{p33kab00_1_s33_u_deadbeef}</code>

## Shop

to-do

## login

<code>My dog-sitter's brother made this website but I can't get in; can you help?</code>

After opening the website we find that it uses a file called _index.js_ to check the credentials. Then opening it and running it through a JavaScript prettifier we end up with the following:

![Capture](https://user-images.githubusercontent.com/52963102/126078478-6a97954b-74e1-4681-a268-081d21a9e8d8.PNG)

I'm not too familiar with JavaScript but the code isn't too difficult and after looking at the _return_ part of the function and googling what _btoa()_ does we end up with just _base64_ decoding the given strings, thus our username is _admin_ and password is the flag.

<code>picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}</code>
