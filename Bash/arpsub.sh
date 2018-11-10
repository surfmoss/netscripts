
#!/bin/sh

COUNTER=1

while [ $COUNTER -lt 255 ]

do
   arp 10.0.0.$COUNTER & 
   COUNTER=$(( $COUNTER + 1 ))

done
