* Command to run the script

<pre>
python hostsub.py | grep pointer |awk '{ print $1,$5 }'
</pre>

* Source

<pre>
import subprocess

cmdarp = "host 192.168.9."

for x in range (1,254):
    p = subprocess.Popen(cmdhost+str(x), shell=True, stderr=subprocess.PIPE)

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
2.9.168.192.in-addr.arpa room114.mbnet
16.9.168.192.in-addr.arpa room211-CR.mbnet
36.9.168.192.in-addr.arpa 702cr.mbnet
108.9.168.192.in-addr.arpa CAD2.mbnet
173.9.168.192.in-addr.arpa room208-SCAN.mbnet
175.9.168.192.in-addr.arpa room208.mbnet
177.9.168.192.in-addr.arpa room204.mbnet
178.9.168.192.in-addr.arpa room201A.mbnet
180.9.168.192.in-addr.arpa room202.mbnet
182.9.168.192.in-addr.arpa room266.mbnet
183.9.168.192.in-addr.arpa room203.mbnet
186.9.168.192.in-addr.arpa room256.mbnet
187.9.168.192.in-addr.arpa room268.mbnet
189.9.168.192.in-addr.arpa room266.mbnet
190.9.168.192.in-addr.arpa pcnetlab.mbnet
191.9.168.192.in-addr.arpa room269.mbnet
</pre>

Back to Network Documentation Home-->[[Main Page]]
