proc ping_net {x} {
 for {set n 1} {$n<=$x} {incr n 1} {
    exec "ping 10.1.1.$n"
 }
}
