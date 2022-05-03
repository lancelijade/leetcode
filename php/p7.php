<?php

class Solution {

    /**
     * @param Integer $x
     * @return Integer
     */
    function reverse($x) {
        $n = pow(2,31);
        if ($x>0) {
            $r = (int)strrev($x);
            if ($r > $n-1) return 0;
            else return $r;
        }
        else {
            $r = -(int)strrev($x);
            if ($r < -$n) return 0;
            else return $r;
        }
    }
}

$x = 1563847412;

$so = new Solution();
$r = $so->reverse($x);
print_r($r);