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
  
  * DON't FORGET THAT SERVERS HOST WEBSITES (aka run nmap)
  
  always try default username:passwords combos
  
## Login
  _hydra_ for login brute-forcing

## Upload vulns
  
Cookies

XXS
XXE

# pwn

# rev
_gdb_
  
  
## Android APKs
  1) APK decompiler https://www.decompiler.com/ or use installed _jadx_ app
  2) Look into _/Resources/AndroidManifest.xml_ and then search _/sources_ for _MainActivity.java_ and work on from there. _R.java_ could also be of use.
  
  Reversing guide and exercises: https://www.ragingrock.com/AndroidAppRE/

# Misc

## wireshark
- file extraction: https://www.sneakymonkey.net/2017/03/03/pcap-file-extraction/
  
## images

  Varius 2D codes -> QR Code, MaxiCode, Aztec etc
  
  - https://www.photopea.com/
    -> online photoshop
  - https://stegonline.georgeom.net/upload
    -> bit plane browsing, extract data, show info and strings
  
  _strings_, _zsteg_, _xxd_, _binwalk_, _steghide_, _stegsolve_, _foremost_, _stat_, 
  
  **exiftool**<br>
    * look at image size
    * either use hex editor (remember little endian) or <code>convert in.jpg -resize INTxINT out.jpg</code>
  
 **imagemagick and ffmpeg**
  <br><code> ffmpeg -i video.mp4 -vf mpdecimate,setpts=N/FRAME_RATE/TB frames/frame_%3d.jpg # get frames from video </code><br>
  <code> convert frames/frame_*.jpg -compose Darken -layers Flatten result.jpg # join multiple images of frames together </code>
  
  
## audio
  - audacity
    * audio spectrogram -> "a spectrogram is a visual representation of the spectrum of frequencies of sound, or other signals, as they vary with time." Basically, it is a method to visualize sound and signals. Can pretty much hide anything from messages to images and so on.
  
  - dtmf-decoder _dtmf_ on linux or https://unframework.github.io/dtmf-detect/
  
  - a butt load of decoders
    * https://www.reddit.com/r/RTLSDR/comments/1e37d0/linux_software_to_decode_digital_modes/
  
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
