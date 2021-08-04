# CTF write ups
Just a webpage for various CTF challenges I've solved.

<code>WARNING! There will be spoilers ahead</code>

# TryHackMe

## Overpass



# picoCTF

## Cookies

<code>Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:64944/</code>

A really fun challenge. After opening the page in Burp Suite and examining the HTTP requests we find that a value _name_ is passed with each query:

![Capture](https://user-images.githubusercontent.com/52963102/125533318-157b8dfc-d34a-48c6-aec6-76227eede20c.PNG)

Now originally I changed the value by hand till I reached _name=18_ and that gives us the flag, but I wanted to try and simulate requests with Python as well.

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

# CTFLearn

## Wikipedia
<code>Not much to go off here, but it’s all you need: Wikipedia and 128.125.52.138.</code>

In Wikipedia you can search for edits that were made but not accepted. So all you got to do in this challenge is to go to https://wikipedia.com and paste the given Ipv4 address <code>128.125.52.138</code>.

A warning box pops up that says _This is an old revision of this page, as edited by 128.125.52.138 (talk) at 17:13, 17 August 2015 (add another type of flag). The present address (URL) is a permanent link to this revision, which may differ significantly from the current revision._ So after that it's easy enough to just CTRL+F and type in <code>CTF</code> after that we see that here was a previous section called _Competitions_ and there's the flag:

<code>In a certain CTF competition, the flag to a certain problem is "cNi76bV2IVERlh97hP".</code>

<code>CTFLearn{cNi76bV2IVERlh97h}</code>

## Morse Code
<code>..-. .-.. .- --. ... .- -- ..- . .-.. -- --- .-. ... . .. ... -.-. --- --- .-.. -... -.-- - .... . .-- .- -.-- .. .-.. .. -.- . -.-. .... . . ...</code>

Just a simple morse code challenge. Fire up https://icyberchef.com, paste the code and translate from morse.

We get the flag <code>CTFLearn{FLAGSAMUELMORSEISCOOLBYTHEWAYILIKECHEES}</code>

## WOW.... So Meta
<code>This photo was taken by our target. See what you can find out about him from it. https://mega.nz/#!ifA2QAwQ!WF-S-MtWHugj8lx1QanGG7V91R-S1ng7dDRSV25iFbk</code>

So obviously from the context we're dealing with image metadata. A couple of tools that can be used for that:
  * imagemagick
  * file
  * exiftool
  * binwalk

First rename the downloaded picture to _image.jpg_ for easier usage. Starting off with _imagemagick_ from <code>man imagemagick</code> we see that we can use <code>man identify</code> and that gives us <code>identify -verbose image.jpg | grep -i "flag"</code> the output of that code is _MicrosoftPhoto:CameraSerialNumber: flag{EEe_x_I_FFf}_ thus our flag is:
<code>CTFLearn{EEe_x_I_FFf}</code>

## Reverse Polarity
<code>I got a new hard drive just to hold my flag, but I'm afraid that it rotted. What do I do? The only thing I could get off of it was this: 01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101</code>

Another very simple challenge, just go to https://icyberchef.com and translate from binary.

<code>CTF{Bit_Flippin}</code>

## Vigenère Cipher
<code>The vignere cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers based on the letters of a keyword.<br />
I’m not sure what this means, but it was left lying around: blorpy
gwox{RgqssihYspOntqpxs}
</code>

We're given the key <code>blorpy</code> and the encoded flag <code>gwox{RgqssihYspOntqpxs}</code> and we just got to perform a simple decipher.

Another challenge that's very simple to solve using CyberChef, but I decided to try and implement a Vigenère decipher in Python by hand.

First you need the Vigenère square, since there are lower and uppercase letters in the cipher I decided to have both lower and uppercase squares as well.

After creating the squares just work it back from the given key and cipher. Essentially you should end up with something like this: <br>
<code>col = sq[0].index(key[i])</code><br>
<code>letter = sq[0][sq[col].index(cipher[i])]</code><br>
Where i is just the current position that we're working with

I also had to do a little work on the cipher and key itself. First of all, because the key contained brackets so after removing then we end up with:<br>
**cipher:** <code>gwoxRgqssihYspOntqpxs</code><br>
And now we need the key to match the length of the cipher as well so we just repeat the key thrice and attach 3 more letters to match the key's length of 21 characters. <br>
**key:** <code>blorpyblorpyblorpyblo</code>

The code I used can be found here: https://github.com/ricoandreaslepp/ciphers/blob/main/dVigenere.py

Eventually we end up with <code>flag{CiphersAreAwesome}</code>

## Git Is Good
<code>The flag used to be there. But then I redacted it. Good Luck. https://mega.nz/#!3CwDFZpJ!Jjr55hfJQJ5-jspnyrnVtqBkMHGJrd6Nn_QqM7iXEuc</code><br>

A little more complicated this time around, even though it's still an easy challenge.

So from the name of the challenge and the downloaded file we can conclude that it's some sort of git repository. In the folder itself we find a _flag.txt_ file that has been redacted. By moving into the _gitIsGood_ folder and running <code>git show</code> on Kali we get the flag from the _logs_.

<code>flag{protect_your_git}</code>

## Don't Bump Your Head(er)
<code>Try to bypass my security measure on this site! http://165.227.106.113/header.php</code>

Personally really enjoyed this one, helped me understand more about how HTTP requests and the web in general works.

So we start off with the website we're given and on it, it says that our user agent isn't valid.

After inspecting the page that we land on we find a HTML comment <code>Sup3rS3cr3tAg3nt</code>

Then modifying our request with BurpSuite we can change our User-Agent to the given one. 

After that we land on a different page that says, that we didn't come from 'awesomesauce.com'. After a bit of research I found the header _Referer_ and set it to awesomesauce.com. Here's the description of the header:

![Capture](https://user-images.githubusercontent.com/52963102/125333226-a7faff80-e352-11eb-9563-56c5d10db876.PNG)

And here's a picture of the whole GET request on BurpSuite:

![Capture](https://user-images.githubusercontent.com/52963102/125332966-56eb0b80-e352-11eb-8b82-ff76305d3496.PNG)

After that we get the flag: <code>flag{did_this_m3ss_with_y0ur_h34d}</code>

## POST Practice

<code>This website requires authentication, via POST. However, it seems as if someone has defaced our site. Maybe there is still some way to authenticate? http://165.227.106.113/post.php</code>

A typical GET request gives us this response:

![Capture](https://user-images.githubusercontent.com/52963102/125333791-53a44f80-e353-11eb-9c89-a17815415688.PNG)

From there we just shift the GET request to a POST and add the lines:

![Capture](https://user-images.githubusercontent.com/52963102/125338453-e4315e80-e358-11eb-89a3-c8d48ebc5591.PNG)

Where _Content-Length_ is just the length of the metadata string:

![Capture](https://user-images.githubusercontent.com/52963102/125338854-628e0080-e359-11eb-8307-b3ebd473d055.PNG)

PS. One thing to keep in mind is that the username and password have to be in the body part of the request, so the breakline is a must, otherwise the request will not get a response. Took me a good few minutes till I figured that out.

And the response gives us the flag <code>flag{p0st_d4t4_4ll_d4y}</code>

## 07601

<code>https://mega.nz/#!CXYXBQAK!6eLJSXvAfGnemqWpNbLQtOHBvtkCzA7-zycVjhHPYQQ I think I lost my flag in there. Hopefully, it won't get attacked...</code>

Definitely a harder one this time. Dealing with images the need to know tools are:
  * imagemagick
  * file
  * exiftool
  * binwalk
  * strings
<br>(There's definitely around 1 million additional tools, but these are the ones that I know and use)

Tried messing around with different tools just to see if something pops up, but nothing really did. Then I got to _binwalk_ and found out that there are quite a few hidden files in the innocent looking _PNG_ file. Extracted those into a directory called _walk_ and after extracting all the _I Warned You.jpeg_ files and running <code>strings | grep "{"</code> one of the files gave a suspicious looking line <code>ABCTF{Du$t1nS_D0jo}1r</code> and from there our real flag was:

<code>ABCTF{Du$t1nS_D0jo}</code>

## A CAPture of a Flag

<code>This isn't what I had in mind, when I asked someone to capture a flag... can you help? You should check out WireShark. https://mega.nz/#!3WhAWKwR!1T9cw2srN2CeOQWeuCm0ZVXgwk-E2v-TrPsZ4HUQ_f4</code>

Another interesting challenge. Opening the file up on WireShark and looking through _tcp.stream eq_ we find that at _eq 5_ there's a _GET_ request:

![Capture](https://user-images.githubusercontent.com/52963102/125420395-1389ddf6-d8f4-4bc3-abdf-ae5d5bcd0bc7.PNG)

After base64 decode we get the flag:

![Capture](https://user-images.githubusercontent.com/52963102/125420534-b3773b29-78d1-4fb7-9f2f-61dc9a3f1999.PNG)


<code>flag{AFlagInPCAP}</code>

## RSA Noob

<code>These numbers were scratched out on a prison wall. Can you help me decode them? https://mega.nz/#!al8iDSYB!s5olEDK5zZmYdx1LZU8s4CmYqnynvU_aOUvdQojJPJQ</code>

A super simple RSA challenge. The tool I mostly find success with is RsaCtfTool on GitHub:

![Capture](https://user-images.githubusercontent.com/52963102/125422351-ad555aa7-adc1-4990-af62-49a6e9dde1f5.PNG)

<code>abctf{b3tter_up_y0ur_e}</code>

## RSA Beginner

<code>I found this scribbled on a piece of paper. Can you make sense of it? https://mega.nz/#!zD4wDYiC!iLB3pMJElgWZy6Bv97FF8SJz1KEk9lWsgBSw62mtxQg</code>

And for the sake of it here's one more:
![Capture](https://user-images.githubusercontent.com/52963102/125422778-1f6c35ad-dff6-43c4-ad90-18ef698bc901.PNG)

<code>abctf{rs4_is_aw3s0m3}</code>

## BruXOR

<code>There is a technique called bruteforce. Message: q{vpln'bH_varHuebcrqxetrHOXEj No key! Just brute .. brute .. brute ... :D</code>

