# Really Awesome CTF 2021

## Call&Response

## blue

To be fair then this challenge was quite a guessing roulette and only after consulting with the author of the challenge did I manage to get the flag. We are given an image that to the human eye looks just like a big blob of blue. After analysing the image with <code>pngcheck -vtp7f blue.png</code> we find that there are 22 pixels that differ from the rest. Usually the data is hidden in the LSB after XORing or subtracting the differing pixel RGBA values from the usual ones. At this point it was just purely guessing and testing and after XORing the values and taking R[2:1], G[2:0], B[2:0], A[0] (verilog notation for bits) we get the unusual flag. Script in the repo.

<code>ractf{54kkijARv3n_Po!kK4}</code>

## Shouty

I really want to make a script for it.
