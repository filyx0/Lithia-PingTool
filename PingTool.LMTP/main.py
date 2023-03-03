import socket
import os
import time

f = open("./PingTool.LMTP/logs.log", "a")

inp = input("\033[91m\033[1mHostname ->\033[0m ")

try:
    ip = socket.gethostbyname(str(inp))
except:
    os.system("cls")
    time.sleep(1)
    print("\033[91mERROR: HostName not valid!")
    os.system("cls")

print("\033[91mIP: \033[0m" + ip)

print("\n\033[0mSaving data...")

time.sleep(1)

f.write(f"HOSTNAME: {str(inp)}, IP: {ip}\n")
f = open("./PingTool.LMTP/logs.log", "w")

os.system("cls")