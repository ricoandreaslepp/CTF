# RCTS CERT 2021

## Knock knock

Tried to make it as detailed as possible for future reference on _ova_ files in CTFs.

First I imported the file into Oracle VM and before booting I had to setup the network so I went to Settings->Network->Adapter 1->Bridged Adapter->My WIFI. After that it was all bridged so I could access it through my computer's terminal. Opening the VM itself we get a login prompt with a username and a password, but after trying at it for a while I gave up and tried something else.

I could ping it from my WSL2 Kali (the ip of the VM was shown on the screen when it was booting, but could also be found by nmap on the WSL2 for internal addresses) and I decided to run an nmap scan which showed this:

![image](https://user-images.githubusercontent.com/52963102/129182805-05c0e1b2-2afe-46cc-afb7-a72549c33ba9.png)

After connecting to the VM through ftp, using anonymous as the username and any password and then setting passive mode with ```pass``` we find a _flag.txt_ file with ls, but after doing ```get flag.txt``` and opening the file, it's just a bait flag that tells us to look at another door (referring to ports I assumed). Now our first nmap scan only showed port 21 as open, so this baffeled me for a bit, but when we connected to the VM through ftp it gave us 3 "doors" to actually examine with ports 7000, 8000, 9000. Since the name of the challenge is "knock knock" I googled port knocking and found a whole wikipedia page about the topic. So after using netcat to try and connect to each of the ports and running nmap again on the VM we find that port 22 with ssh has opened up.

At the start of the challenge we were given an _id_rsa_ file aswell so trying to connect to the VM with ```ssh -i id_rsa <VM_IP>``` was an idea that proved to be unsuccessful. So I tried generating a public key from the private key file and with that we got a username and trying to log in now with the private key file proved to be successful:

![image](https://user-images.githubusercontent.com/52963102/129180670-2babbf1a-4915-45cc-bcfc-01015ce2e614.png)

<code>flag{kn0ck1ng_0n_d00rs_1s_p0l1t3}</code>

This was most probably my favorite challenge of all time, I learned a lot and had tons of fun figuring out what to do next.

Lessons? Well the VM network bridging was super cool, definitely a lot to learn from that and more to experiment with. The OpenSSH RSA private key and public key, I'm getting an idea of what they are and how they work, but in order for me to adequately explain it to someone else, it will take a little more time and understanding. I did learn though, that usually when generating public/private key pair, their both generated in the private key FILE not just private key, so that's why you can extract the public key from there. Port knocking was an interesting concept that I hadn't really looked into before.

## Decrypting the payload

We are told that the network was compromised using a phishing scam with an excel file that was sent to some employees' email accounts. Deciding by the name of the challenge we need to find the used payload and decrypt it to get our flag.

Downloading it on windows our firewall already pops up with the trojan in the file and immediately quarantines and deletes the file so I had to use WSL2 Kali Linux just to even view the file. (I wanted to use a VM, but my computer's RAM wasn't having it that day so since it was a CTF I assumed it was safe to go with WSL2)

Since I've never done anything like this before I did it completely from scratch. I first extracted files from the _Account_report.xlsm_ file with binwalk and got a whole folder of files. From there I looked through them for a while to find anything suspicious. I managed to even find the name of the person who made the file, that would've been a cool flag aswell. I still don't know if it was intentional or not, but hey in a real-world scenario, I got you. Anyhow, I eventually ended up with the _vbaProject.bin_ file and with little googling I realized that _Excel_ files can have macros that will autoexecute when you open the file, which was exactly how the scam was built up.

![Capture](https://user-images.githubusercontent.com/52963102/129171219-3767671e-9e25-4d4b-9291-b734f99ca586.PNG)

From there I found _oletools_ as a way of analyzing and extracting macros from _Composite Document Files_ and with ```olevba -a vbaProject.bin``` I got the full VBA macro in base64. Here's a screenshot of a (very) small part of the output:

![Capture](https://user-images.githubusercontent.com/52963102/129171549-6ba72810-0f06-4c14-84c6-2a1de2f4c9e1.PNG)

After cleaning the output up and decoding with base64 we get 2 parts of the flag and after combining and reversing we end up with the flag. Honestly the cleaning part turned out to be rather tedious, because I found no way to actually extract the hex strings and copying doesn't help us either. Eventually though I remembered, that _Sublime Text 3_ is an amazing editor and ended up editing all the 353 lines of output at once to get the hex strings and then a quick python script to join all the lines, the output of which I piped right into decode. The command looked like this: ```python3 join.py | base64 -d > out.txt```

<code>flag{m4cr0_3n4bl3d_d0cs_4r3_d4ng3r0us}</code>

Real-world lessons? -> Don't ever open suspicious files sent to you by emails or any other forms of communication, they can not just get a reverse shell on your private network and read your data, but also compromise a whole LAN. Phishing scams are getting more advanced just as every other field of IT, so we must learn and adapt.
