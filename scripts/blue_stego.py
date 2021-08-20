from PIL import Image
import numpy
import sys

def xor(default_pix, pix_arr):
    values = []
    #print(default_pix, pix_arr)
    for rgba in pix_arr:
        for i, pix in enumerate(rgba):
            #print(i, pix)
            values.append(default_pix[i]^pix)
    return values
    
def find(val):

    ans = ""
    result = "0"
    for i, v in enumerate(val, start=1):

        if not i%4:
            result += bin(v)[-1]
        elif v == 0:
            result += "00"
        elif v == 1:
            result += "01"
        elif i%4==1:
            result += bin(v)[-3:-1]
        else:
            result += bin(v)[-2:]

        if not i%4:
            ans += chr(int(result, 2))
            result = "0"
    return ans

def main():
    
    im = Image.open('./blue.png').convert('RGBA')
    pix = list(im.getdata())
    #print(pix)

    default_pix = (64, 77, 205, 255)
    special_pix = []
    for tup in pix:
        if tup!=default_pix:
            special_pix.append(tup)

    values = xor(default_pix, special_pix)
    #print(values)
    ans = find(values)
    
    print(ans)

main()
