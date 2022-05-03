<?php

class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countOrders($n) {
        
        $c = [];
        $c[1] = 1;
        $c[2] = 6;

        for ($i=3; $i<=$n; $i++) {
            $c[$i] = $c[$i-1] * $i * (2*$i-1);
            $c[$i] %= 1000000007;
        }

        return $c[$n];
    }
}

$n = 13;
$so = new Solution();
$r = $so->countOrders($n);
var_dump($r);
