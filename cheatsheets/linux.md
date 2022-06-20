# Linux
id <user> -> list user and group information <br>
sudo -l -> show commands that can be run with sudo <br>
  -> check https://gtfobins.github.io/ if any programs can be used for privesc <br>

watch
sed
seq
uniq
netstat

## Shell stabilisation
  1) If Python is installed <code>python -c 'import pty;pty.spawn("/bin/bash")'</code>, spawns a better featured bash shell
  2) <code>export TERM=xterm-256color</code> gives access to term commands (clear etc)
  3) background CTRL+Z, <code>stty raw -echo; fg</code> (turn off our own terminal echo - gives tab autocompletes, arrow keys and CTRL+C kills procs, then foregrounds the spawned shell).

a lot of interesting files to check (RTFM book)
 run _LinPeas.sh_
