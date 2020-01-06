proc int_rate {x} {
 for {set n 4} {$n<=$x} {incr n 0} {
exec "show clock"
exec "sh int e1/$n | b 'Load' | end RX | exclude Load | exclude RX | human | cut -b 15-26"
}
}

int_rate 4
