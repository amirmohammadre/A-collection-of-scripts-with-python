import re
import time as tm
import os

try:
    fin = open("/var/log/auth.log", "r")    	#Debian based systems
except:
    fin = open("/var/log/secure", "r")		    #Red Hat based systems

counter_fail = 0
counter_acce = 0

for line in fin:
    try:
        if  re.findall("Failed password", line):
            tm.sleep(1)
            print(line.strip())
            counter_fail += 1

        elif re.findall("Accepted password", line):
            tm.sleep(1)
            print(line.strip())
            counter_acce += 1
    except:
        print("Not found log success and failure login !!")
        exit()

print("[x] Number of failed logins:", counter_fail)
print("[x] Number of accepted logins:", counter_acce)





