* Command to run the script

<pre>
python ping_sub.py
</pre>

* Source

<pre>
import subprocess
import os
with open(os.devnull, "wb") as limbo:
        for n in xrange(1, 255):
                ip="192.168.10.{0}".format(n)
                result=subprocess.Popen(["host", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print ip, "inactive"
                else:
                        print ip, "active"
</pre>

* output

<pre>
192.168.10..1 inactive
192.168.10..2 active
192.168.10..3 active
192.168.10..4 active
192.168.10..5 active
192.168.10..6 active
192.168.10..7 active
192.168.10..8 inactive
192.168.10..9 active
192.168.10..10 inactive
192.168.10..11 active
192.168.10..12 active
192.168.10..13 active
192.168.10..14 inactive
192.168.10..15 active
192.168.10..16 active
192.168.10..17 inactive
192.168.10..18 inactive
192.168.10..19 inactive
192.168.10..20 inactive
192.168.10..21 inactive
192.168.10..22 inactive
192.168.10..23 inactive
192.168.10..24 inactive
192.168.10..25 inactive
192.168.10..26 inactive
192.168.10..27 inactive
192.168.10..28 inactive
192.168.10..29 active
192.168.10..30 active
192.168.10..31 inactive
192.168.10..32 inactive
192.168.10..33 active
192.168.10..34 active
192.168.10..35 active
192.168.10..36 active
192.168.10..37 active
192.168.10..38 inactive
192.168.10..39 active
192.168.10..40 inactive
192.168.10..41 active
192.168.10..42 inactive
192.168.10..43 active
192.168.10..44 inactive
192.168.10..45 inactive
192.168.10..46 inactive
192.168.10..47 inactive
192.168.10..48 active
192.168.10..49 active
192.168.10..50 inactive
192.168.10..51 inactive
192.168.10..52 active
192.168.10..53 inactive
192.168.10..54 active
192.168.10..55 active
192.168.10..56 active
192.168.10..57 active
192.168.10..58 inactive



</pre>

Back to Network Documentation Home-->[[Main Page]]
