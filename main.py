import socket
import time
from os import system, name

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

lastDataTime = 0
line = ''

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def printSubtitle(dataToPrint):
    """
    docstring
    """
    global line
    line += dataToPrint
    
    if (time.time() - lastDataTime) > 3: # Clear the buffer if there is 3 secs between words
        line = ''
    clear()
    print(line)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            while data:
                decodedData = data.decode()
                printSubtitle(decodedData)
                data = b''
                lastDataTime = time.time()
                
                