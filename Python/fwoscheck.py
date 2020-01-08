

* Run a python script from a Linux box to see if the OS on a firewall needs to be updated.
  In this example we are running a script to login to four firewalls.  Once logged in there will
  be a query made to the output after logging in to search for devices running 8.3.2E137.  If they are not
  running that OS, a comment will be made for that specific device to be upgraded

== Run the following command ==

* type the following command in a Linux directory containing the script. You will be prompted for a password:
<pre>
[mbubu@lnxbox Py_labs]$ python fwoscheck.py    
Password:
</pre>

* this is the code that is being executed:
<pre>
#!/usr/bin/python

import time
import sys
import getpass
import paramiko
import re

username = "mbubu"
password = getpass.getpass()
IPs = ['192.168.62.103', '192.168.133.101', '192.168.61.102', '192.168.20.10']


def connectToFW(ip):
         remote_conn_pre = paramiko.SSHClient()
         remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
         remote_conn_pre.connect(ip , username=username, password=password)
         print "SSH connection established to %s" %ip
         remote_conn = remote_conn_pre.invoke_shell()
         output = remote_conn.recv(1000)
         time.sleep(1)
         remote_conn.send("srole\r")
         output2 = remote_conn.recv(5000)
         test2 = re.findall(r'(8.3.2E136)\D', output2)
         if '8.3.2E136' in test2:
              print 'The OS does not need to be updated for %s' %ip
         else:
              print 'The OS for %s needs to be updated' %ip


for ip in IPs:
        connectToFW(ip)

sys.exit("operation completed")
</pre>

== Output ==

* The following output is delivered if the OS needs to be updated to the required/designated OS in the script:
<pre>
SSH connection established to 192.168.62.103
The OS for 192.168.62.103 needs to be updated
SSH connection established to 192.168.133.101
The OS for 192.168.133.101 needs to be updated
SSH connection established to 192.168.61.102
The OS for 192.168.61.102 needs to be updated
SSH connection established to 192.168.20.10
The OS for 192.168.20.10 needs to be updated
operation completed
</pre>


* If the query was looking for OS 8.3.2E136 and the firewall was running 8.3.2E136 then the output would look like this:
<pre>
SSH connection established to 192.168.62.103
The OS does not need to be updated for 192.168.62.103
SSH connection established to 192.168.133.101
The OS does not need to be updated for 192.168.133.101
SSH connection established to 192.168.61.102
The OS does not need to be updated for 192.168.61.102
SSH connection established to 192.168.20.10
The OS does not need to be updated for 192.168.20.10
operation completed</pre>



-->[[Main Page]]
