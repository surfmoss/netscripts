== TCL script that sends one command to multiple interfaces ==
<pre>
Switch(tcl)#foreach var {37 38} {
</pre>

* TCL line that configures the previously set interfaces:
<pre>
ios_config exec "configure terminal" "interface Gi1/0/$var" "description foo"}
</pre>

* Entire TCL line should look like this in order for it to work without errors:
<pre>
Switch(tcl)#foreach var {37 38} {
ios_config exec "configure terminal" "interface Gi1/0/$var" "description foo"}
</pre>

* Show command to verify the change was made:
<pre>
Switch(tcl)#sh int status
</pre>

* Verify change was made:
<pre>
Port      Name               Status       Vlan       Duplex  Speed Type 
Gi1/0/1   --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/2   --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/3   --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/4   --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/5   --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/6   --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/7   --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/8   --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/9   --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/10  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/11  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/12  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/13  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/14  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/15  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/16  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/17  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/18  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/19  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/20  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/21  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/22  --------           notconnect   100          auto   auto 10/100/1000BaseTX
          
Port      Name               Status       Vlan       Duplex  Speed Type 
Gi1/0/23  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/24  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/25  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/26  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/27  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/28  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/29  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/30  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/31  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/32  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/33  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/34  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/35  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/36  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/37  foo                notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/38  foo                notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/39  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/40  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/41  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/42  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/43  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/44  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/45  --------           notconnect   100          auto   auto 10/100/1000BaseTX
Gi1/0/46  --------           notconnect   100          auto   auto 10/100/1000BaseTX
          </pre>

== TCL script that sends multiple commands to multiple interfaces ==

* 
<pre>
cli "conf t ; int e1/11 ; description abc" ; cli "conf t ; int e1/12 ; description def"
</pre>

<pre>
Nexus3548Switch1(config-if-tcl)# sh int status

------------------------------------------------------------------------------------
Port          Name               Status    Vlan      Duplex  Speed   Type
------------------------------------------------------------------------------------
Eth1/1        peer keepalive     connected 3000      full    10G     SFP-H10GB-ACU10M     
 
Eth1/2        peerlink           connected trunk     full    10G     10Gbase-SR           
 
Eth1/3        peerlink           connected trunk     full    10G     10Gbase-SR           
 
Eth1/4        vpc to DIST        connected trunk     full    10G     10Gbase-SR           
 
Eth1/5        vpc to DIST        connected trunk     full    10G     10Gbase-SR           
 
Eth1/6        server1		 connected 314       full    1000    1000base-T           
 
Eth1/7        server2		 connected 314       full    10G     10Gbase-SR           
 
Eth1/8        --------		 disabled  332       full    10G     10Gbase-SR           
 
Eth1/9        --------           sfpAbsent 999       full    10G     --                   
 
Eth1/10       --------           sfpAbsent 999       full    10G     --                   
 
Eth1/11       abc                sfpAbsent 999       full    10G     --                   
 
Eth1/12       def                sfpAbsent 999       full    10G     --                   
 
Eth1/13       --------           sfpAbsent 999       full    10G     --        
</pre>
