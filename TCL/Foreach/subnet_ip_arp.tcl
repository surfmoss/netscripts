* The purpose of this script is to ping IP's from 192.168.10.134-192.168.10.147 then run a show ip arp command on the same range in order to verify the IP's on the network:

'''ping range script and ip arp range script separated by a semi-colon:'''

<pre>
foreach subnet { 10 } { for {set i 134} {$i < 148} {incr i} { ping 192.168.$subnet.$i re 1 ti 1 } } ; 
foreach subnet { 10 } { for {set i 134} {$i < 148} {incr i} { show ip arp | i 192.168.$subnet.$i } } 
</pre>

'''output'''
<pre> 
CoreSW1(tcl)#          
Type escape sequence to abort.
Sending 1, 100-byte ICMP Echos to 192.168.10.134, timeout is 1 seconds:
!
Success rate is 100 percent (1/1), round-trip min/avg/max = 1/1/1 ms
Type escape sequence to abort.
Sending 1, 100-byte ICMP Echos to 192.168.10.135, timeout is 1 seconds:
!
Success rate is 100 percent (1/1), round-trip min/avg/max = 1/1/1 ms
Type escape sequence to abort.
Sending 1, 100-byte ICMP Echos to 192.168.10.136, timeout is 1 seconds:
!
Success rate is 100 percent (1/1), round-trip min/avg/max = 1/1/1 ms
Type escape sequence to abort.
Sending 1, 100-byte ICMP Echos to 192.168.10.137, timeout is 1 seconds:
!
Success rate is 100 percent (1/1), round-trip min/avg/max = 1/1/1 ms
Type escape sequence to abort.
Sending 1, 100-byte ICMP Echos to 192.168.10.138, timeout is 1 seconds:
!
Success rate is 100 percent (1/1), round-trip min/avg/max = 1/1/1 ms
Type escape sequence to abort.
Sending 1, 100-byte ICMP Echos to 192.168.10.139, timeout is 1 seconds:
!
Success rate is 100 percent (1/1), round-trip min/avg/max = 1/1/1 ms
Type escape sequence to abort.
Sending 1, 100-byte ICMP Echos to 192.168.10.140, timeout is 1 seconds:
!
Success rate is 100 percent (1/1), round-trip min/avg/max = 1/1/1 ms
Type escape sequence to abort.
Sending 1, 100-byte ICMP Echos to 192.168.10.141, timeout is 1 seconds:
.
Success rate is 0 percent (0/1)
Type escape sequence to abort.
Sending 1, 100-byte ICMP Echos to 192.168.10.142, timeout is 1 seconds:
!
Success rate is 100 percent (1/1), round-trip min/avg/max = 1/1/1 ms
Type escape sequence to abort.
Sending 1, 100-byte ICMP Echos to 192.168.10.143, timeout is 1 seconds:
!
Success rate is 100 percent (1/1), round-trip min/avg/max = 1/1/1 ms
Type escape sequence to abort.
Sending 1, 100-byte ICMP Echos to 192.168.10.144, timeout is 1 seconds:
!
Success rate is 100 percent (1/1), round-trip min/avg/max = 1/1/1 ms
Type escape sequence to abort.
Sending 1, 100-byte ICMP Echos to 192.168.10.145, timeout is 1 seconds:
!
Success rate is 100 percent (1/1), round-trip min/avg/max = 1/1/1 ms
Type escape sequence to abort.
Sending 1, 100-byte ICMP Echos to 192.168.10.146, timeout is 1 seconds:
!
Success rate is 100 percent (1/1), round-trip min/avg/max = 1/1/1 ms
Type escape sequence to abort.
Sending 1, 100-byte ICMP Echos to 192.168.10.147, timeout is 1 seconds:
!
Success rate is 100 percent (1/1), round-trip min/avg/max = 1/1/1 msInternet  192.168.10.134         117   70db.98fe.5a46  ARPA   Vlan10
Internet  192.168.10.135          54   00a3.8e03.5a46  ARPA   Vlan10
Internet  192.168.10.136          76   00a3.8e0a.ae46  ARPA   Vlan10
Internet  192.168.10.137         117   00a3.8e14.b3c6  ARPA   Vlan10
Internet  192.168.10.138          91   00a3.8e0a.b4c6  ARPA   Vlan10
Internet  192.168.10.139         157   70db.98fe.64c6  ARPA   Vlan10
Internet  192.168.10.140         107   70db.98fe.5bc6  ARPA   Vlan10
Internet  192.168.10.141           0   Incomplete      ARPA   
Internet  192.168.10.142          87   00a3.8e0a.a746  ARPA   Vlan10
Internet  192.168.10.143          84   00a3.8e14.bac6  ARPA   Vlan10
Internet  192.168.10.144         140   00a3.8e0a.a646  ARPA   Vlan10
Internet  192.168.10.145         147   00a3.8e14.b246  ARPA   Vlan10
Internet  192.168.10.146          87   70db.987a.4346  ARPA   Vlan10
Internet  192.168.10.147         208   00a3.8e61.6846  ARPA   Vlan10
</pre>
