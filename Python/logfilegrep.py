* Command to run the script

<pre>
python logfilegrep.py
</pre>

* Source

<pre>
print "Enter the source or destination IP that is in question:",

ip = raw_input ()

import os

os.system ("cat messages | grep %s | more" % ip)
</pre>

* output

<pre>
Enter the source or destination IP that is in question: 192.168.1.1
</pre>

<pre>
id=firewall time="2016-01-14 03:10:09" fw=sledge2.fnmoc.navy.mil pri=6 rule="loopback zone
 2 to DNS severs" proto=kernel sent=134 rcvd=40 src=127.2.0.1 srcname= dst=192.168.1.1 dst
name= user= msg="Network Traffic Event"
id=firewall time="2016-01-14 05:11:15" fw=firewall.mil pri=3 proto=110/tcp 
src=192.168.39.45 srcname= dst=192.168.1.1 dstname= msg="Netprobe event detected."
id=firewall time="2016-01-14 09:30:41" fw=fw=firewall.mil pri=3 proto=25/tcp 
src=192.168.25.31 srcname= dst=192.168.1.1 dstname= msg="Netprobe event detected."
id=firewall time="2016-01-14 09:30:41" fw=fw=firewall.mil pri=3 proto=60000/tcp 
src=192.168.25.31 srcname= dst=192.168.1.1 dstname= msg="Netprobe event detected."
</pre>

'''The logfile named messages needs to be in the same directory in which the script is also located in'''

Back to Network Documentation Home-->[[Main Page]]
