

* Run a script in order to show the interfaces of a switch and query the current interface rate of one interface

== Run the following command ==

* type the following command in a Linux directory containing the script:
<pre>
python sshnexus.py
</pre>

* You will be prompted for a password:
<pre>
[mbubu@lnxbox tested]$ python sshnexus_cmds.py 
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
 
ip = '192.168.1.1'
username = "mbubu"
password = getpass.getpass()

#Execute the main part of the code
  
remote_conn_pre = paramiko.SSHClient()  
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip , username=username, password=password)
print "SSH connection established to %s" %ip
remote_conn = remote_conn_pre.invoke_shell()
print "Interactive SSH session established"
output = remote_conn.recv(1000)
print output
remote_conn.send("terminal length 0\n")
remote_conn.send("show interface status\r")
time.sleep(1)
remote_conn.send("tclsh\r")
remote_conn.send("foreach var {40 40 40 40 40 40 40 40 40 40 40 40 40} {exec show interface e1/$var | i rate}\r")
time.sleep(6)
output2 = remote_conn.recv(10000)
print output2
#remote_conn.send("end\r")
#remote_conn.send("disable\r")
#remote_conn.close()

sys.exit("ALL Done!")</pre>

== Output ==

* The following output is received from 1 nexus switch:
<pre>
[mbubu@lnxbox tested]$ python sshnexus.py 
Password: 
SSH connection established to 192.168.1.1
Interactive SSH session established
Cisco Nexus Operating System (NX-OS) Software
TAC support: http://www.cisco.com/tac
Copyright (c) 2002-2016, Cisco Systems, Inc. All rights reserved.
The copyrights to certain works contained in this software are
owned by other third parties and used and distributed under
license. Certain components of this software are licensed under
the GNU General Public License (GPL) version 2.0 or the GNU
Lesser General Public License (LGPL) Version 2.1. A copy of each
such license is available at
http://www.opensource.org/licenses/gpl-2.0.php and
http://www.opensource.org/licenses/lgpl-2.1.php

terminal length 0
show interface status
NexusSW2# terminal length 0
NexusSW2# show interface status

--------------------------------------------------------------------------------
Port          Name               Status    Vlan      Duplex  Speed   Type
--------------------------------------------------------------------------------
Eth1/1        server1          	sfpAbsent 220       full    10G     --         
Eth1/2        HA lnk 		sfpAbsent trunk     full    10G     --         
Eth1/3        server2           sfpAbsent 220       full    1000    --         
Eth1/4        server3          	sfpAbsent 220       full    10G     --         
Eth1/5        server4        	sfpAbsent 332       full    1000    --         
Eth1/6        ESxi1          	sfpAbsent trunk     full    10G     --         
Eth1/7        ESXi2         	sfpAbsent trunk     full    10G     --         
Eth1/8        ESXi3         	sfpAbsent trunk     full    10G     --         
Eth1/9        ESXi4          	connected trunk     full    10G     SFP-H10GB-C
Eth1/10       ESXi5          	connected trunk     full    10G     SFP-H10GB-C
Eth1/11       Esxi6          	connected trunk     full    10G     SFP-H10GB-C
Eth1/12       ESXi7          	connected trunk     full    10G     SFP-H10GB-C
Eth1/13       ESXi8          	connected trunk     full    10G     SFP-H10GB-C
Eth1/14       ESXi9          	connected trunk     full    10G     SFP-H10GB-C
Eth1/15       ESXi10          	connected trunk     full    10G     SFP-H10GB-C
Eth1/16       ESXi11          	connected trunk     full    10G     SFP-H10GB-C
Eth1/17       server5      	sfpAbsent 332       full    10G     --         
Eth1/18       server6          	sfpAbsent 220       full    10G     --         
Eth1/19       ESXi12    	sfpAbsent trunk     full    10G     --         
Eth1/20       server7           sfpAbsent 150       full    10G     --         
Eth1/21       server8           sfpAbsent 150       full    10G     --         
Eth1/22       server9           sfpAbsent 150       full    10G     --         
Eth1/23       server10          sfpAbsent 150       full    10G     --         
Eth1/24       server11          sfpAbsent 220       full    10G     --         
Eth1/25       ESXi12            connected trunk     full    10G     SFP-H10GB-C
Eth1/26       ESXi13            connected trunk     full    10G     SFP-H10GB-C
Eth1/27       ESXi14            connected trunk     full    10G     SFP-H10GB-C
Eth1/28       ESXi15            sfpAbsent trunk     full    10G     --         
Eth1/29       ESXi16            sfpAbsent trunk     full    10G     --         
Eth1/30       ESXi17            sfpAbsent trunk     full    10G     --         
Eth1/31       ESXi18            sfpAbsent trunk     full    10G     --         
Eth1/32       ESXi19            sfpAbsent trunk     full    10G     --         
Eth1/33       server12          sfpAbsent 994       full    10G     --         
Eth1/34       server13          sfpAbsent 994       full    10G     --         
Eth1/35       server14          sfpAbsent 994       full    10G     --         
Eth1/36       server15          sfpAbsent 994       full    10G     --         
Eth1/37       server16          sfpAbsent 220       full    10G     --         
Eth1/38       server17          sfpAbsent 220       full    10G     --         
Eth1/39       server18          sfpAbsent 220       full    10G     --         
Eth1/40       server19          connected trunk     full    10G     10Gbase-SR 
mgmt0         OOB / connected   routed    full    a-1000  --         

NexusSW2# tclsh
foreach var {40 40 40 40 40 40 40 40 40 40 40 40 40} {exec show interface e1/$var | i rate}
NexusSW2-tcl# foreach var {40 40 40 40 40 40 40 40 40 40 40 40 40} {exec show interface e1/$var | i rate}
  30 seconds input rate 3794112 bits/sec, 1272 packets/sec
  30 seconds output rate 4012696 bits/sec, 1322 packets/sec
    input rate 52.54 Mbps, 7.76 Kpps; output rate 46.26 Mbps, 6.70 Kpps

  30 seconds input rate 3794112 bits/sec, 1272 packets/sec
  30 seconds output rate 4012696 bits/sec, 1322 packets/sec
    input rate 52.54 Mbps, 7.76 Kpps; output rate 46.26 Mbps, 6.70 Kpps

  30 seconds input rate 3794112 bits/sec, 1272 packets/sec
  30 seconds output rate 4012696 bits/sec, 1322 packets/sec
    input rate 52.54 Mbps, 7.76 Kpps; output rate 46.26 Mbps, 6.70 Kpps

  30 seconds input rate 3794112 bits/sec, 1272 packets/sec
  30 seconds output rate 4012696 bits/sec, 1322 packets/sec
    input rate 52.54 Mbps, 7.76 Kpps; output rate 46.26 Mbps, 6.70 Kpps

  30 seconds input rate 3794112 bits/sec, 1272 packets/sec
  30 seconds output rate 4012696 bits/sec, 1322 packets/sec
    input rate 52.54 Mbps, 7.76 Kpps; output rate 46.26 Mbps, 6.70 Kpps

  30 seconds input rate 3794112 bits/sec, 1272 packets/sec
  30 seconds output rate 4012696 bits/sec, 1322 packets/sec
    input rate 52.54 Mbps, 7.76 Kpps; output rate 46.26 Mbps, 6.70 Kpps

  30 seconds input rate 3794112 bits/sec, 1272 packets/sec
  30 seconds output rate 4012696 bits/sec, 1322 packets/sec
    input rate 52.54 Mbps, 7.76 Kpps; output rate 46.26 Mbps, 6.70 Kpps

  30 seconds input rate 3794112 bits/sec, 1272 packets/sec
  30 seconds output rate 4012696 bits/sec, 1322 packets/sec
    input rate 52.54 Mbps, 7.76 Kpps; output rate 46.26 Mbps, 6.70 Kpps

  ½0 seconds input rate 3794112 bits/sec, 1272 packets/sec
  30 seconds output rate 4012696 bits/sec, 1322 packets/sec
    input rate 52.54 Mbps, 7.76 Kpps; output rate 46.26 Mbps, 6.70 Kpps

  30 seconds input rate 3794112 bits/sec, 1272 packets/sec
  30 seconds output rate 4012696 bits/sec, 1322 packets/sec
    input rate 52.54 Mbps, 7.76 Kpps; output rate 46.26 Mbps, 6.70 Kpps

  30 seconds input rate 3794112 bits/sec, 1272 packets/sec
  30 seconds output rate 4012696 bits/sec, 1322 packets/sec
    input rate 52.54 Mbps, 7.76 Kpps; output rate 46.26 Mbps, 6.70 Kpps

  30 seconds input rate 3794112 bits/sec, 1272 packets/sec
  30 seconds output rate 4012696 bits/sec, 1322 packets/sec
    input rate 52.54 Mbps, 7.76 Kpps; output rate 46.26 Mbps, 6.70 Kpps

  30 seconds input rate 3794112 bits/sec, 1272 packets/sec
  30 seconds output rate 4012696 bits/sec, 1322 packets/sec
    input rate 52.54 Mbps, 7.76 Kpps; output rate 46.26 Mbps, 6.70 Kpps
NexusSW2-tcl# 
ALL Done!
</pre>

-->[[Main Page]]

