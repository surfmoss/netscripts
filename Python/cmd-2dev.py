#Python and Paramiko
# Accessing and modifying two Cisco routers

import paramiko
import sys
import time
import getpass

ip1 = "10.0.0.74"
ip2 = "10.0.0.75"

ip_list = [ip1,ip2]

conf = "configure terminal"
termlength = "terminal length 0"
password = getpass.getpass()
username = "admin"
### SSH to a session and configure the hostname and exit the session ###

def Session1(name, ipaddr):
        remote_conn_pre = paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(ipaddr, username=username, password=password, look_for_keys= False, allow_agent= False)
        print "SSH connection established to %s" % ipaddr
        remote_conn = remote_conn_pre.invoke_shell()
        print "Interactive SSH session established"
        output = remote_conn.recv(1000)
        print output
        remote_conn.send(termlength + "\r")
        remote_conn.send(password + "\r")
        remote_conn.send(conf + "\r")
        time.sleep(2)
        remote_conn.send(name + "\r")
        remote_conn.close()
### login to sessions and pass on different variables ###
Session1('hostname PY-R1', ip_list[0])
Session1('hostname PY-R2', ip_list[1])

sys.exit("operation completed")
