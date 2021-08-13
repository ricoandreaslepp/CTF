import random
from Crypto.Cipher import AES

def generate_key():
    # generate key
    gpList = [ [13, 19], [7, 17], [3, 31], [13, 19], [17, 23], [2, 29] ]
    g, p = random.choice(gpList)
    a = random.randint(1, p)
    b = random.randint(1, p)
    k = pow(g, a * b, p) # pow(base, exp, mod)
    # some integer in range 1 to 31, cause (mod p)
    k = str(k)

    # print("Diffie-Hellman key exchange outputs")
    # print("Public key: ", g, p)
    # print("Jotaro sends: ", aNum)
    # print("Dio sends: ", bNum)
    # print()

    # pad key to 16 bytes (128bit)
    key = ""
    i = 0
    padding = "uiuctf2021uiuctf2021"
    # len(k) is 1 or 2
    # key will be len of 15 or 14
    while (16 - len(key) != len(k)):
        key = key + padding[i] # prepend padding
        i += 1
    key = key + k
    key = bytes(key, encoding='ascii')
    return key

iv = bytes("kono DIO daaaaaa", encoding = 'ascii')

def decrypt(key, flag):
    global iv, found
    cipher = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = cipher.decrypt(flag).decode()

    return ciphertext

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

run()            
"""
with open('flag.txt', 'rb') as f:
    flag = f.read()

iv = bytes("kono DIO daaaaaa", encoding = 'ascii') # got the iv
cipher = AES.new(key, AES.MODE_CFB, iv)
ciphertext = cipher.encrypt(flag)

print(ciphertext.hex())
"""