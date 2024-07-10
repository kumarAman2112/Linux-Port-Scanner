#!/bin/python3


import sys
import socket
from datetime import datetime

# Define out target

if len(sys.argv) == 2 : 
          target = socket.gethostbyname(sys.argv[1]) # translate host into ipv4
else :
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")

# ADD Pretty Banner

print("-" * 50)
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("_" * 50)
try:
      for port in range(50,85):
             s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
             socket.setdefaulttimeout(1)
             result=s.connect_ex((target,port))
             if result == 0 :
                    print(f"Port {port} is open")
             s.close()
except KeyboardInterrupt:
           print("\n Exiting program.")
           sys.exit()
except socket.gaierror:
            print("Host could not be resolved")
            sys.exit()
except socket.error:
            print("Could not connect to server")
            sys.exit()

