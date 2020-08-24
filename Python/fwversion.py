

* Run a python script from a Linux box and grep the OS of multiple firewalls
 The code is not clean and could be enhanced by making a function instead of repetitive lines of code as shown at the bottom of this page

== Run the following command ==

* type the following command in a Linux directory containing the script. You will be prompted for a password:
<pre>
[mbubu@lnxbox Py_labs]$ python fwversion.py | grep SecureOS
Password:
</pre>

* this is the code that is being executed:
<pre>
#import the neccessary modules

import time
import sys
import getpass
import paramiko

#setup the variables used in the script 
 
ip1 = '192.168.35.1'
ip2 = '192.168.35.2'
ip3 = '192.168.35.3'
ip4 = '192.168.35.4'
username = "mbubu"
password = getpass.getpass()

#Execute code for first Firewall
  
remote_conn_pre = paramiko.SSHClient()  
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip1 , username=username, password=password)
print "SSH connection established to %s" %ip1
remote_conn = remote_conn_pre.invoke_shell()
print "Interactive SSH session established"
output = remote_conn.recv(1000)
print output
remote_conn.send("srole\r")
time.sleep(2)
remote_conn.send("cf interface status\r")
time.sleep(3)
output2 = remote_conn.recv(5000)
print output2

#Execute code for second Firewall
remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip2 , username=username, password=password)
print "SSH connection established to %s" %ip2
remote_conn = remote_conn_pre.invoke_shell()
print "Interactive SSH session established"
output3 = remote_conn.recv(1000)
print output3
remote_conn.send("srole\r")
time.sleep(2)
remote_conn.send("cf interface status\r")
time.sleep(3)
output4 = remote_conn.recv(5000)
print output4

#Execute code for third Firewall
remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip3 , username=username, password=password)
print "SSH connection established to %s" %ip3
remote_conn = remote_conn_pre.invoke_shell()
print "Interactive SSH session established"
output5 = remote_conn.recv(1000)
print output5
remote_conn.send("srole\r")
time.sleep(2)
remote_conn.send("cf interface status\r")
time.sleep(3)
output6 = remote_conn.recv(5000)
print output6

#Execute code for fourth Firewall
remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip4 , username=username, password=password)
print "SSH connection established to %s" %ip4
remote_conn = remote_conn_pre.invoke_shell()
print "Interactive SSH session established"
output7 = remote_conn.recv(1000)
print output7
remote_conn.send("srole\r")
time.sleep(2)
remote_conn.send("cf interface status\r")
time.sleep(3)
output8 = remote_conn.recv(5000)
print output8

sys.exit("ALL Done!")
</pre>

== Output ==

* The following OS output is provided by using the Linux grep command:
<pre>
ALL Done!
SecureOS firewall1.mil 8.3.2E136 SW_OPS64_SMP Thu Jun 15 13:17:37 CDT 2017 8.3.2E136-c313a  amd64
SecureOS firewall2.mil 8.3.2E136 SW_OPS64_SMP Thu Jun 15 13:17:37 CDT 2017 8.3.2E136-c313a  amd64
SecureOS firewall3.mil 8.3.2E136 SW_OPS64_SMP Thu Jun 15 13:17:37 CDT 2017 8.3.2E136-c313a  amd64
SecureOS firewall4.mil 8.3.2E136 SW_OPS64_SMP Thu Jun 15 13:17:37 CDT 2017 8.3.2E136-c313a  amd64
</pre>

== Script as a function ==

* type the following command in a Linux directory containing the script. You will be prompted for a password:
<pre>
[mbubu@lnxbox Py_labs]$ python fwverfunc.py | grep SecureOS
Password:
</pre>

* this the python code without having to repeat the same lines for each IP, written as a function:
<pre>
#!/usr/bin/python

import time
import sys
import getpass
import paramiko

username = "mbubu"
password = getpass.getpass()
IPs = ['192.168.35.1', '192.168.35.2', '192.168.35.3', '192.168.35.4']


def connectToFW(ip):
         remote_conn_pre = paramiko.SSHClient()
         remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
         remote_conn_pre.connect(ip , username=username, password=password)
         print "SSH connection established to %s" %ip
         remote_conn = remote_conn_pre.invoke_shell()
         print "Interactive SSH session established"
         output = remote_conn.recv(1000)
         time.sleep(1)
         print output
         remote_conn.send("srole\r")
         output2 = remote_conn.recv(5000)
         print output2
        
for ip in IPs:
        connectToFW(ip)

sys.exit("ALL Done!")
</pre>

* this is your output:
<pre>
ALL Done!
SecureOS firewall1.mil 8.3.2E136 SW_OPS64_SMP Thu Jun 15 13:17:37 CDT 2017 8.3.2E136-c313a  amd64
SecureOS firewall2.mil 8.3.2E136 SW_OPS64_SMP Thu Jun 15 13:17:37 CDT 2017 8.3.2E136-c313a  amd64
SecureOS firewall3.mil 8.3.2E136 SW_OPS64_SMP Thu Jun 15 13:17:37 CDT 2017 8.3.2E136-c313a  amd64
SecureOS firewall4.mil 8.3.2E136 SW_OPS64_SMP Thu Jun 15 13:17:37 CDT 2017 8.3.2E136-c313a  amd64
</pre>



-->[[Main Page]]
