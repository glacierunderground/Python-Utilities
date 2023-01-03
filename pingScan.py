import os
import time
import platform
import subprocess
import threading

scanList = []
liveAddressList = []

def isValidOctet(octect):
    if int(octect) >= 0 and int(octect) <=255:
        return True
    else:
        return False

def ping(host):
    pingCommand = ['ping', '-c', '1', host]
    response = subprocess.call(pingCommand,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    if response == 0:
        print(host,":", "Alive")
        return True
    else:
        return False



scanParam = input("Please provide an IPV4 address space to scan (* for wildcard):\n")

scanParamList = scanParam.split('.')

starter = 0
end = 255
for starter in range(255):
    host = "10.0.60."
    host += str(starter)
    x = threading.Thread(target=ping, args=(host,))
    x.start()
    #print()
    #alive = ping(host)
    #print(host,":", alive)


#print(scanParamList[0])




