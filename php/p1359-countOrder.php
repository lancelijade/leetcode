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
            //$x = (1+2*$i-1) * (2*$i-1) / 2;
            $x = $i * (2*$i-1);
            $c[$i] = bcmul($c[$i-1], $x);
        }

        if (bccomp($c[$n], pow(10,9)+7)==1) $c[$n] = bcmod($c[$n], pow(10,9)+7);
        return (int)$c[$n];
    }
}

$n = 4;
$so = new Solution();
$r = $so->countOrders($n);
var_dump($r);
