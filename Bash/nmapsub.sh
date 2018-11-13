#!/bin/sh
# while loop to run nmap port scan on a subnet
COUNTER=1

while [ $COUNTER -lt 255 ]

do
   nmap -p 8080  10.0.0.$COUNTER &
   COUNTER=$(( $COUNTER + 1 ))

done
