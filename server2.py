import socket
import os
import threading
s=socket.socket(socket.SOCK_DGRAM,socket.AF_INET)
IP="192.168.43.112"
Port=1111
s.bind((IP,Port))
print("\t\t\t\t Welcome to Chat App!!")
print()

def Receive():
  while True:
    os.system("tput setaf 2")
    Input=s.recvfrom(1024)
    Client=Input[1][0]
    Msg=Input[0]
    print("\t\t\t\t" +  Msg.decode())
    if (Msg.decode()=="exit"):
      exit(0)

def Send():
  while True:
    os.system("tput setaf 2")
    Msg=input()
    s.sendto(Msg.encode(),("192.168.43.131",1111))
    if (Msg.encode()=="exit"):
      exit(0)

T1=threading.Thread(target=Receive)
T2=threading.Thread(target=Send)

T1.start()
T2.start()
