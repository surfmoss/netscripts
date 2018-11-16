#!/bin/bash

for rate in $(seq -w 385 387);
do echo $rate;
cat ratefile.txt | grep "input rate $rate" | grep 'Mbps'
done
