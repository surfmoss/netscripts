proc int_rate {x} {
 for {set n 1} {$n<=$x} {incr n 0} {
    exec "show interface e1/$n | i rate"
    exec "show clock"
 }
}
