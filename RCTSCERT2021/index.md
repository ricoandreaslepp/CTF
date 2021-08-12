# RCTS CERT 2021

## Knock knock


## Decrypting the payload

We are told that the network was compromised using a phishing scam with an excel file that was sent to some employees' email accounts. Deciding by the name of the challenge we need to find the used payload and decrypt it to get our flag.

Downloading it on windows our firewall already pops up with the trojan in the file and immediately quarantines and deletes the file so I had to use WSL2 Kali Linux just to even view the file. (I wanted to use a VM, but my computer's RAM wasn't having it that day so since it was a CTF I assumed it was safe to go with WSL2)

Since I've never done anything like this before I did it completely from scratch. I first extracted files from the _Account_report.xlsm_ file with binwalk and got a whole folder of files. From there I looked through them for a while to find anything suspicious. I managed to even find the name of the person who made the file, that would've been a cool flag aswell. I still don't know if it was intentional or not, but hey in a real-world scenario, I got you. Anyhow, I eventually ended up with the _vbaProject.bin_ file and with little googling I realized that _Excel_ files can have macros that will autoexecute when you open the file, which was exactly how the scam was built up.

![Capture](https://user-images.githubusercontent.com/52963102/129171219-3767671e-9e25-4d4b-9291-b734f99ca586.PNG)

From there I found _oletools_ as a way of analyzing and extracting macros from _Composite Document Files_ and with ```bash olevba -a vbaProject.bin``` I got the full VBA macro in base64. Here's a screenshot of a (very) small part of the output:

![Capture](https://user-images.githubusercontent.com/52963102/129171549-6ba72810-0f06-4c14-84c6-2a1de2f4c9e1.PNG)

After cleaning the output up and decoding with base64 we get 2 parts of the flag and after combining and reversing we end up with the flag. Honestly the cleaning part turned out to be rather tedious, because I found no way to actually extract the hex strings and copying doesn't help us either. Eventually though I remembered, that _Sublime Text 3_ is an amazing editor and ended up editing all the 353 lines of output at once to get the hex strings and then a quick python script to join all the lines, the output of which I piped right into decode. The command looked like this: ```bash python3 join.py | base64 -d > out.txt```

<code>flag{m4cr0_3n4bl3d_d0cs_4r3_d4ng3r0us}</code>
