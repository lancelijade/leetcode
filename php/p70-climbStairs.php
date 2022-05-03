<?php

class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function climbStairs($n) {
        
        $j1 = 1;
        $j2 = 2;
        for ($i=3; $i<=$n; $i++) {
            $j3 = $j1 + $j2;
            $j1 = $j2;
            $j2 = $j3;
        }
        return $j3;
    }
}

$n = 45;
$so = new Solution();
$r = $so->climbStairs($n);
print_r($r);