* Command to run the script

<pre>
python arpsub.py |grep eth0
</pre>

* Source

<pre>
import subprocess

cmdarp = "arp 192.168.1."

for x in range (1,254):
    p = subprocess.Popen(cmdarp+str(x), shell=True, stderr=subprocess.PIPE)

    while True:
        out = p.stderr.read(1)
        if out == '' and p.poll() != None:
            break
        if out != '':
            sys.stdout.write(out)
            sys.stdout.flush()
</pre>

* output

<pre>
box6.mbnet   		        ether   18:03:73:34:4c:77   C                     eth0
box5.mbnet  		        ether   f8:b1:56:e4:20:ef   C                     eth0
box4.mbnet   		        ether   18:03:73:33:3b:2b   C                     eth0
box3.mbnet   		        ether   f8:b1:56:e3:ef:d1   C                     eth0
box2.mbnet      	      ether   18:03:73:33:3a:c8   C                     eth0
192.168.1.17                    (incomplete)                              eth0
192.168.1.18                    (incomplete)                              eth0
192.168.1.19                    (incomplete)                              eth0
192.168.1.20                    (incomplete)                              eth0
192.168.1.21                    (incomplete)                              eth0
192.168.1.22                    (incomplete)                              eth0
192.168.1.23                    (incomplete)                              eth0
box1.mbnet           		        (incomplete)                              eth0
192.168.1.25                    (incomplete)                              eth0
192.168.1.26                    (incomplete)                              eth0
192.168.1.27                    (incomplete)                              eth0
192.168.1.28                    (incomplete)                              eth0
box7.mbnet  		        ether   18:03:73:33:3c:b0   C                     eth0
192.168.1.31                    (incomplete)                              eth0
192.168.1.32                    (incomplete)                              eth0
box8.mbnet   		        ether   18:03:73:33:3a:55   C                     eth0
box9.mbnet      	      ether   f8:b1:56:e4:1f:43   C                     eth0
