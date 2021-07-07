# CTF write ups
Just a webpage for various CTF challenges I've solved.

<code>WARNING! There will be spoilers ahead</code>

# picoCTF

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

First rename the downloaded picture to _image.jpg_ for easier usage. Starting off with _imagemagick_ from <code>man imagemagick</code> we see that we can use <code>identify -verbose image.jpg | grep -i "flag"</code> the output of that code is _MicrosoftPhoto:CameraSerialNumber: flag{EEe_x_I_FFf}_ thus our flag is:
<code>CTFLearn{EEe_x_I_FFf}</code>

## Reverse Polarity
<code>I got a new hard drive just to hold my flag, but I'm afraid that it rotted. What do I do? The only thing I could get off of it was this: 01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101</code>

Another very simple challenge, just go to https://icyberchef.com and translate from binary.

<code>CTF{Bit_Flippin}</code>

## **Vigenère Cipher**
We're given the key <code>blorpy</code> and the encoded flag <code>gwox{RgqssihYspOntqpxs}</code> and we just got to perform a simple decipher.

Another challenge that's very simple to solve using CyberChef, but I decided to try and implement a Vigenère decipher in Python by hand.

First you need the Vigenère square, since there are lower and uppercase letters in the cipher I decided to have both lower and uppercase squares as well.

After creating the squares just work it back from the given key and cipher. Essentially you should end up with something like this: <br>
<code>col = sq[0].index(key[i]) <br>
			letter = sq[0][sq[col].index(cipher[i])]</code><br>


The code I used can be found here: https://github.com/ricoandreaslepp/ciphers/blob/main/dVigenere.py

Eventually we end up with <code>flag{CiphersAreAwesome}</code>



