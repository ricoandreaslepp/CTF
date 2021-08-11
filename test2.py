# vulnerable text injection application
import os
import sys
text = sys.argv[1].replace("\"", "")
os.system(f"python3 test.py \"{text}\"")
