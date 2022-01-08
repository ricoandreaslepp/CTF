# readme
A cheatsheet for CTFs, that will eventually hopefully have everything that I know of.

https://www.exploit-db.com/

# Linux
id <user> -> list user and group information <br>
sudo -l -> show commands that can be run with sudo <br>
  -> check https://gtfobins.github.io/ if any programs can be used for privesc <br>
 
_wget_ and run _LinPeas.sh_
  
# Web
  run _dirbuster_
  run _nikto_
  
  always try default username:passwords combos
  
## Login
  _hydra_ for login brute-forcing

## Upload vulns
  
Cookies

XXS
XXE
  
SQL injections
  - cheatsheet

# pwn

# rev
_gdb_ 

# Misc
## images

  Varius 2D codes -> QR Code, MaxiCode, Aztec etc
  
  - https://www.photopea.com/
    -> online photoshop
  - https://stegonline.georgeom.net/upload
    -> bit plane browsing, extract data, show info and strings
  
  _strings_, _zsteg_, _xxd_, _binwalk_, _steghide_, _stegsolve_, _foremost_, _exiftool_, _stat_, 
  
 _imagemagick_ and _ffmpeg_
  <br>
  <code> ffmpeg -i video.mp4 -vf mpdecimate,setpts=N/FRAME_RATE/TB frames/frame_%3d.jpg # get frames from video </code><br>
  <code> convert frames/frame_*.jpg -compose Darken -layers Flatten result.jpg # join multiple images of frames together </code>
  
  
## audio
## videos
  - ffmpeg and imagemagick
    -> https://gist.github.com/sulram/0c8a95fc90f23e860b9a
## malware
* powerpoints and similar can be unzipped
* _vbaProject.bin_ contains macros
  
 _olevba_

  - Malware detection https://www.virustotal.com/gui/home/upload
  
## yeah
strings _filename_ | less -> for safety
