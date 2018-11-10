-----------------------------------------------------
Create a file, edit the file, execute the file within the IOS CLI

== Enter TCL cli==

<pre>
Switch1#tclsh
</pre>

* output
<pre>
Switch1(tcl)#
</pre>

== Create a file ==

* Type the following command to create a unique file in the disk0: directory:
<pre>
open disk0:ping.tcl WRONLY
</pre>

* bootflash syntax:
<pre>
open bootflash:ping.tcl  w
</pre>



* output
<pre>
Switch1(tcl)#open disk0:ping.tcl WRONLY
file0
</pre>

* You can see the channel file0 has been created.  You will edit the newly created file via this channel.

== Edit file previously named ping.tcl==

* Type the following commands to put the script into the newly created file:
<pre>
puts file0 foreach subnet {
</pre>

<pre>
1 } {
</pre>

<pre>
for {set i 1} {$i < 255} {incr i} {
</pre>

<pre>
ping 192.168.$subnet.$i re 2 ti 0
</pre>

<pre>
}
</pre>

<pre>
}
</pre>

Then hit Enter on the keyboard

== Verify ==

* Check the disk0: directory:
<pre>
Switch1(tcl)#dir 
</pre>

* output
<pre>
Directory of disk0:/

    1  -rw-   118706532  Jul 19 2013 17:57:24 +00:00  s72033-adventerprisek9_wan-mz.122-33.SXI11.bin
   32  -rw-          98   Oct 5 2016 22:42:18 +00:00  ping.tcl

</pre>

== View the contents of the file ==

<pre>
Switch1(tcl)#more disk0:ping.tcl
</pre>

* output
<pre>
foreach subnet {
1 } {
for {set i 1} {$i < 255} {incr i} {
ping 192.168.$subnet.$i re 2 ti 0
}
}
</pre>

== Execute the file ==

<pre>
tclsh disk0:ping.tcl
</pre>

* output
<pre>

Switch1#tclsh disk0:ping.tcl


Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 192.168.1.1, timeout is 0 seconds:
..
Success rate is 0 percent (0/2)
Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 192.168.1.2, timeout is 0 seconds:
..
Success rate is 0 percent (0/2)
Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 192.168.1.3, timeout is 0 seconds:
..
Success rate is 0 percent (0/2)
Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 192.168.1.4, timeout is 0 seconds:
..
Success rate is 0 percent (0/2)
Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 192.168.1.5, timeout is 0 seconds:
..
Success rate is 0 percent (0/2)
Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 192.168.1.6, timeout is 0 seconds:
..
Success rate is 0 percent (0/2)
Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 192.168.1.7, timeout is 0 seconds:
..
Success rate is 0 percent (0/2)
Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 192.168.1.8, timeout is 0 seconds:
..
Success rate is 0 percent (0/2)
Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 192.168.1.9, timeout is 0 seconds:
..
Success rate is 0 percent (0/2)
Type escape sequence to abort.
Sending 2, 100-byte ICMP Echos to 192.168.1.10, timeout is 0 seconds:
....
</pre>

<pre>
In summary, a file named ping.tcl was 
created in the disk0: directory.  The 
file was modified to contain a ping 
sweep tcl script.  The script was 
executed from its file location.
</pre>
