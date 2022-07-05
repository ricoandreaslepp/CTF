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
  _strings_, _zsteg_, _xxd_, _binwalk_, _steghide_, _stegsolve_, , _stegcracker_, _foremost_, _stat_, 
  
