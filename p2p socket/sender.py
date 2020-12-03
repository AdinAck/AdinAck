import sys
import os
import socket
from tqdm import tqdm

if len(sys.argv) <= 1:
    print("This script requires arguments to run.")
    exit()

filename = sys.argv[1]
port = int(sys.argv[2])
buffer = 1024

f = open(filename, 'rb')
filesize = int(os.path.getsize(filename))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', port))
s.listen()

sock, addr = s.accept()

sock.send(bytearray([len(str(filesize))]))
sock.send(str(filesize).encode())
sock.send(bytearray([len(filename.split("\\")[-1])]))
sock.send(filename.split("\\")[-1].encode())
sock.close()

sock, addr = s.accept()

progress = tqdm(range(filesize), f"Transfering {filename.split("\\")[-1]}", unit="B", unit_scale=True, unit_divisor=1024)
for _ in range(filesize):
    read = f.read(buffer)
    progress.update(len(read))
    if not read:
        break
    sock.sendall(read)
sock.close()
