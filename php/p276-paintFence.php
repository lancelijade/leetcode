<?php

class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function numWays($n, $k) {
        
        $dp[1] = $k;
        $dp[2] = $k * $k;

        for ($i=3; $i<=$n; $i++) {
            $dp[$i] = ($k-1) * $dp[$i-1] + ($k-1) * $dp[$i-2];
        }

        return $dp[$n];
    }
}

$n = 7;
$k = 2;
$so = new Solution();
$r = $so->numWays($n, $k);
print_r($r);