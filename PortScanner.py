#!/bin/python3

import sys
import socket
from datetime import datetime


#Define your target:
if len(sys.argv) == 2:  #sys.argv == user input | Also, 2 parameters because the name of the program is counted as one
	target = socket.gethostbyname(sys.argv[1])  # Translates a host name to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip/domain>")

#Add a pretty banner:
print("-"*50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-"*50)

#Try-Statement (if it can't do, it has an exception):
try:
	for port in range(50,85):  #from port 50 to 84, since it stops at 85
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)  # waits 1 second before timing out
		result = s.connect_ex((target,port))  #returns an error indicator (0 if the port is open, error is 1)
		if result == 0:
			print("Port {} is open.".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting program...")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Couldn't connect to sever.")
	sys.exit()
