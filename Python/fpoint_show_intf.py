

* Run a script in order to apply a simple show command to 4 different forcepoint firewalls 


== Run the following command ==

* type the following command in a Linux directory containing the script:
<pre>
python fpoint_show_intf.py
</pre>

* You will be prompted for a password:
<pre>
[mbubu@lnxbox Py_labs]$ python fpoint_show_intf.py              
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
 
ip1 = '192.168.62.103'
ip2 = '192.168.133.101'
ip3 = '192.168.61.102'
ip4 = '192.168.15.10'
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

* The following output is received from 4 different firewalls:
<pre>
[mbubu@lnxbox Py_labs]$ python fpoint_show_intf.py              
Password: 
SSH connection established to 192.168.42.100
Interactive SSH session established
Last login: Wed Sep  6 23:51:30 2017 from 192.168.1.254

SecureOS firewall1.mb.net 8.3.2E136 SW_OPS64_SMP Thu Jun 15 13:17:37 CDT 2017 8.3.2E136-c313a  amd64

SW_OPS64_SMP Fri Dec  3 14:02:57 CST 2010 8.1.0-c_0

SW_OPS64_SMP Fri Dec  3 14:02:57 CST 2010 8.1.0-c_0


Welcome to Sidewinder!

$ srole
# cf interface status

                         Interface Status Information                        
                         ============================                        

           Standard           
           ========           
Name                IPaddress(es)    NIC    Status      Active Speed             
------------------- ---------------- ------ ----------- -------------------      
external_network    192.168.48.104   1-0    Conn/u      1000baseT full-duplex    
1-1 (NIC)                            1-1    Disc/d      autoselect               
1-2 (NIC)                            1-2    Disc/d      autoselect               
Heartbeat           10.4.101.1       1-3    Conn/u      1000baseT full-duplex    
1-4 (NIC)                            1-4    Disc/d      autoselect               
1-5 (NIC)                            1-5    Disc/d      autoselect               
1-6 (NIC)                            1-6    Disc/d      autoselect               
1-7 (NIC)                            1-7    Disc/d      autoselect               
3-0 (NIC)                            3-0    Disc/d      autoselect               
internal_network    192.168.62.104   3-2    Conn/u      10Gbase-SR full-duplex   
3-3 (NIC)                            3-3    Disc/d      autoselect               
3-4 (NIC)                            3-4    Disc/d      autoselect               
3-5 (NIC)                            3-5    Disc/d      autoselect               
mgr2 (NIC)                           mgr2   Disc/d      autoselect               

            VLANs             
            =====             
Name                IPAddress(es)    NIC    VLAN/id      Status Active Speed             
------------------- ---------------- ------ ------------ ------ -------------------      
dmz1       	192.168.79.7      3-1    vlan12/791   Conn/u 10Gbase-SR full-duplex   
dmz2 		192.168.45.130    3-1    vlan18/450   Conn/u 10Gbase-SR full-duplex   
dmz3            192.168.5.245     3-1    vlan1/5      Conn/u 10Gbase-SR full-duplex   
dmz4      	192.168.32.201    3-1    vlan0/632    Conn/u 10Gbase-SR full-duplex   
dmz5   		192.168.6.201     3-1    vlan5/666    Conn/u 10Gbase-SR full-duplex   
dmz6   		192.168.39.106    3-1    vlan3/39     Conn/u 10Gbase-SR full-duplex   
dmz7     	192.168.79.129    3-1    vlan13/792   Conn/u 10Gbase-SR full-duplex   
dmz8      	192.168.89.7      3-1    vlan6/891    Conn/u 10Gbase-SR full-duplex   
dmz9  		192.168.214.111   3-1    vlan4/214    Conn/u 10Gbase-SR full-duplex   
dmz10    	192.168.89.158    3-1    vlan7/892    Conn/u 10Gbase-SR full-duplex   
dmz11 		192.168.38.199    3-1    vlan11/38    Conn/u 10Gbase-SR full-duplex   
dmz12     	192.168.14.201    3-1    vlan2/614    Conn/u 10Gbase-SR full-duplex   
dmz13 		192.168.49.104    3-1    vlan8/449    Conn/u 10Gbase-SR full-duplex   
dmz14     	192.168.33.201    3-1    vlan9/633    Conn/u 10Gbase-SR full-duplex   
dmz15 		192.168.39.228    3-1    vlan15/399   Conn/u 10Gbase-SR full-duplex   
dmz16 		192.168.45.2      3-1    vlan17/45    Conn/u 10Gbase-SR full-duplex   
dmz17     	192.168.34.201    3-1    vlan10/634   Conn/u 10Gbase-SR full-duplex   
management      192.168.14.116    mgr1   vlan14/14    Conn/u 1000baseT full-duplex    
DMZ-loopback    10.1.2.3.57       3-1    vlan16/10    Conn/u 10Gbase-SR full-duplex   
# 
SSH connection established to 192.168.39.25
Interactive SSH session established
Last login: Wed Sep  6 23:51:35 2017 from 192.168.1.254

SecureOS firewallab.mb.net 8.3.2E136 SW_OPS64_SMP Thu Jun 15 13:17:37 CDT 2017 8.3.2E136-c313a  amd64

SW_OPS64_SMP Wed Jun  9 11:57:35 CDT 2010 FW800-d_0


Welcome to Sidewinder!


srole
firewallab:User {1} % srole
firewallab:Admn {1} % cf interface status

                         Interface Status Information                        
                         ============================                        

           Standard           
           ========           
Name                IPaddress(es)    NIC    Status      Active Speed             
------------------- ---------------- ------ ----------- -------------------      
2-3 (NIC)                            2-3    Disc/d      autoselect               
2-2 (NIC)                            2-2    Disc/d      autoselect               
V133-internal       192.168.45.96    2-1    Conn/u      10Gbase-SR full-duplex   
1-3 (NIC)                            1-3    Disc/d      autoselect               
1-2 (NIC)                            1-2    Disc/d      autoselect               
1-1 (NIC)                            1-1    Disc/d      autoselect               
1-0 (NIC)                            1-0    Disc/d      autoselect               
mgr1 (NIC)                           mgr1   Disc/d      autoselect               
mgr3 (NIC)                           mgr3   Disc/d      autoselect               
mgr4 (NIC)                           mgr4   Disc/d      autoselect               

            VLANs             
            =====             
Name                IPAddress(es)    NIC    VLAN/id      Status Active Speed             
------------------- ---------------- ------ ------------ ------ -------------------      
DMZ1      	192.168.148.101   mgr2   vlan9/148    Conn/u 1000baseT full-duplex    
DMZ2   		192.168.149.245   2-0    vlan7/149    Conn/u 10Gbase-SR full-duplex   
DMZ3  		192.168.249.245   2-0    vlan8/249    Conn/u 10Gbase-SR full-duplex   
DMZ4      	192.168.112.245   2-0    vlan1/112    Conn/u 10Gbase-SR full-duplex   
DMZ5 		192.168.232.245   2-0    vlan5/832    Conn/u 10Gbase-SR full-duplex   
DMZ6       	192.168.139.245   2-0    vlan6/139    Conn/u 10Gbase-SR full-duplex   
DMZ7   		192.168.114.245   2-0    vlan2/114    Conn/u 10Gbase-SR full-duplex   
DMZ8 		192.168.142.245   2-0    vlan4/743    Conn/u 10Gbase-SR full-duplex   
DMZ9  		192.168.132.245   2-0    vlan3/732    Conn/u 10Gbase-SR full-duplex   
Management      192.168.13.101    2-0    vlan12/13    Conn/u 10Gbase-SR full-duplex   
DMZ10   	192.168.115.245   2-0    vlan11/115   Conn/u 10Gbase-SR full-duplex   

firewallab:Admn {2} % 
SSH connection established to 192.168.25.28
Interactive SSH session established
Last login: Wed Sep  6 23:51:41 2017 from 192.168.1.254

SecureOS firewall3.mb.net 8.3.2E136 SW_OPS64_SMP Thu Jun 15 13:17:37 CDT 2017 8.3.2E136-c313a  amd64

SW_OPS64_SMP Tue Sep 13 20:34:08 CDT 2011 8.2.0-c_0


Welcome to Sidewinder!


$ srole
# cf interface status

                         Interface Status Information                        
                         ============================                        

           Standard           
           ========           
Name                IPaddress(es)    NIC    Status      Active Speed             
------------------- ---------------- ------ ----------- -------------------      
external_network    192.168.47.102   em0    Conn/u      1000baseT full-duplex    
heartbeat           10.4.101.4       em1    Conn/u      1000baseT full-duplex    
em2 (NIC)                            em2    Disc/d      autoselect               
em3 (NIC)                            em3    Disc/d      autoselect               
em4 (NIC)                            em4    Disc/d      autoselect               
em5 (NIC)                            em5    Disc/d      autoselect               
internal_network    192.168.32.33    ix0    Conn/u      10Gbase-SR full-duplex   
bce0 (NIC)                           bce0   None/d      autoselect               
bce1 (NIC)                           bce1   None/d      autoselect               
bce2 (NIC)                           bce2   None/d      autoselect               
bce3 (NIC)                           bce3   None/d      autoselect               

            VLANs             
            =====             
Name                IPAddress(es)    NIC    VLAN/id      Status Active Speed             
------------------- ---------------- ------ ------------ ------ -------------------      
management 	192.168.95.92    ix1    vlan1/613    Conn/u 10Gbase-SR full-duplex   
DMZ1        	192.168.75.75    ix1    vlan0/46     Conn/u 10Gbase-SR full-duplex   
DMZ2 		192.168.66.61    ix1    vlan2/628    Conn/u 10Gbase-SR full-duplex   
# 
SSH connection established to 192.168.15.10
Interactive SSH session established
Last login: Wed Sep  6 23:51:46 2017 from 192.168.1.254

SecureOS firewall4.mb.net 8.3.2E136 SW_OPS64_SMP Thu Jun 15 13:17:37 CDT 2017 8.3.2E136-c313a  amd64
$ srole
# cf interface status

                         Interface Status Information                        
                         ============================                        

           Standard           
           ========           
Name                IPaddress(es)    NIC    Status      Active Speed             
------------------- ---------------- ------ ----------- -------------------      
1-0 (NIC)                            1-0    Disc/d      autoselect               
1-1 (NIC)                            1-1    Disc/d      autoselect               
management 	        192.168.70.25    1-2    Conn/u      1000baseT full-duplex    
heartbeat           10.4.101.7       1-3    Conn/u      1000baseT full-duplex    
1-4 (NIC)                            1-4    Disc/d      autoselect               
1-5 (NIC)                            1-5    Disc/d      autoselect               
1-6 (NIC)                            1-6    Disc/d      autoselect               
1-7 (NIC)                            1-7    Disc/d      autoselect               
external_network    172.16.2.25      2-1    Conn/u      10Gbase-SR full-duplex                                                                             
2-3 (NIC)                            2-3    Disc/d      autoselect               
2-4 (NIC)                            2-4    Disc/d      autoselect               
2-5 (NIC)                            2-5    Disc/d      autoselect               
mgr1 (NIC)                           mgr1   Disc/d      autoselect               
mgr2 (NIC)                           mgr2   Disc/d      autoselect               

            VLANs             
            =====             
Name                IPAddress(es)    NIC    VLAN/id      Status Active Speed             
------------------- ---------------- ------ ------------ ------ -------------------      
internal_network    192.168.15.10    2-2    vlan1/902    Conn/u 10Gbase-SR full-duplex   
v901-EOM-DMZ        192.168.23.39    2-0    vlan0/901    Conn/u 10Gbase-SR full-duplex                                                                        
# 
ALL Done!
</pre>


-->[[Main Page]]

