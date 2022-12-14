import socket
import pickle
#import email

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())#get ip address auto
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!CONNNECT'
ADDR = (SERVER,PORT)

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.rcv(2048)).decode()
    
send('\n\nHello World\n\n')
send(DISCONNECT_MESSAGE)