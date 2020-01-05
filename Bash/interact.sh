#!/bin/bash

echo "Choose an option to login to a device"

OPTIONS="switch1 switch2 "

select opt in $OPTIONS;
 do     if [ "$opt" = "switch1" ];

then echo "Logging into 10.0.0.100 "
        ssh 10.0.0.100

exit
        elif [ "$opt" = "switch2" ];
then echo "Logging into 10.0.0.101"
        ssh 10.0.0.101

exit
        else            clear
echo "Click option 1 or option 2 only. Hit Enter to see options again"

        fi
done

