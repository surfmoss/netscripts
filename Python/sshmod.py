#import the neccessary modules

import time
import sys
import getpass
import paramiko

#setup the variables used in the script

ip = '10.0.0.100'
username = "admin"
password = getpass.getpass()

#establish an SSH session using local authentication to a cisco switch

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip, username=username, password=password, look_for_keys= False, allow_agent=False)
print "Interactive SSH session established to %s" %ip
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print output

#check current settings on interface

remote_conn.send("terminal length 0\n")
remote_conn.send("show run int g0/1\r")
time.sleep(1)

#display the old port config

output = remote_conn.recv(1000)
print "-------------------BEFORE-----------------------"
print output

#use tcl shell on cisco switch to apply several commands to interface GigabitEthernet0/1
remote_conn.send("tclsh\r")
remote_conn.send('ios_config "int g0/1" "des LINK" "switchport mode access" "switc acce vla 375" "spanning-tree portf" "no shut" \r')
remote_conn.send("show run int g0/1\r")
time.sleep(2)

#display the updated port config
output = remote_conn.recv(3000)
print "-------------------AFTER-----------------------"
print output

#close out ssh session

sys.exit("ALL Done!")
