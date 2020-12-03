import sys
import socket
from tqdm import tqdm
import time

if len(sys.argv) <= 1:
    print("This script requires arguments to run.")
    exit()

ip = sys.argv[1]
port = int(sys.argv[2])
buffer = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

a = int.from_bytes(s.recv(1), "little")
filesize = int(s.recv(a).decode())
b = int.from_bytes(s.recv(1), "little")
filename = s.recv(b).decode()
f = open(filename, 'wb')
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

progress = tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

for _ in range(filesize):
    read = s.recv(buffer)
    progress.update(len(read))
    if not read:
        break
    f.write(read)
s.close()
