<?php

class Solution {

    /**
     * @param Integer $n
     * @return Integer[]
     */
    function countBits($n) {
        $r = [0];
        for ($i=1; $i<=$n; $i++) {
            $r[] = array_count_values(str_split(decbin($i), 1))['1'];
        }
        return $r;
    }
}

$n = 4;
$so = new Solution();
$r = $so->countBits($n);
print_r($r);