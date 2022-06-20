# readme
A cheatsheet for CTFs, that will eventually hopefully have everything that I know of.

General markdown for topics:
  1. Explanation
  2. Common vulns that I've learned
  3. Tools and how to use them

https://www.exploit-db.com/

# rev
_gdb_
_ghidra_
  
## images

  - Varius 2D codes -> QR Code, MaxiCode, Aztec etc
  - https://www.photopea.com/
    -> online photoshop
  - https://stegonline.georgeom.net/upload
    -> bit plane browsing, extract data, show info and strings
  - Python Pillow (PIL) for working with pixel data
  
  **exiftool**<br>
    * look at image size
    * either use hex editor (remember little endian) or <code>convert in.jpg -resize INTxINT out.jpg</code>
    * can alter some things, comments for example
  
 **imagemagick and ffmpeg**
  <br><code> ffmpeg -i video.mp4 -vf mpdecimate,setpts=N/FRAME_RATE/TB frames/frame_%3d.jpg # get frames from video </code><br>
  <code> convert frames/frame_*.jpg -compose Darken -layers Flatten result.jpg # join multiple images of frames together </code>
 
 ** Bitwise operations (code in scripts)
  
  Tools:
  _strings_, _zsteg_, _xxd_, _binwalk_, _steghide_, _stegsolve_, _foremost_, _stat_, 
  
## audio
  - audacity
    * audio spectrogram -> "a spectrogram is a visual representation of the spectrum of frequencies of sound, or other signals, as they vary with time." Basically, it is a method to visualize sound and signals. Can pretty much hide anything from messages to images and so on.
  
  - dtmf-decoder _dtmf_ on linux or https://unframework.github.io/dtmf-detect/

  - a butt load of decoders
    * https://www.reddit.com/r/RTLSDR/comments/1e37d0/linux_software_to_decode_digital_modes/
  
## videos
  - ffmpeg and imagemagick
    -> https://gist.github.com/sulram/0c8a95fc90f23e860b9a

# Misc
  
# External resources
  
* https://github.com/JohnHammond/ctf-katana

