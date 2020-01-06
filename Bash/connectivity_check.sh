#!/bin/bash


PS3='

Choose an option between 1-2 to view VLAN info. Use Ctrl-c to exit the program:
'
echo "                                              "
echo "                                              "

OPTIONS="
VLAN10(192.168.1.0/24)
VLAN20(192.168.2.0/24)
"

select opt in $OPTIONS; do

        if [ "$opt" = "VLAN10(192.168.1.0/24)" ];
then echo "
VLAN10 is a /24 Network
This is the mgmt network
VLAN10(192.168.1.0/24)is inband built at the core"

for ip in 192.168.1.{1..254}; do
ping -c 1 -W 2 $ip | grep "64 bytes" &
done




echo "                                   "
echo "                                   "

PS3='Press Enter to view the list again or Ctrl-c to exit:'

        elif [ "$opt" = "VLAN20(192.168.2.0/24)" ];
then echo "
VLAN20 is a /24 Network
This is the DMZ network
192.168.2.0 255.255.255.0 is built in the firewall"

for ip in 192.168.2.{1..254}; do
ping -c 1 -W 2 $ip | grep "64 bytes" &
done




echo "                                   "
echo "                                   "

PS3='Press Enter to view the list again or Ctrl-c to exit:'

        else            clear
echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Incorrect entry, choose one option between 1 through 2 in order to view more information regarding a specific VLAN";

        fi
done

