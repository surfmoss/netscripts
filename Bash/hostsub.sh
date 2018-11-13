#!/bin/sh

COUNTER=1

while [ $COUNTER -lt 254 ]

do


   host 216.228.5.$COUNTER & 
   COUNTER=$(( $COUNTER + 1 ))


done

















