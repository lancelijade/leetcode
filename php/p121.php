<?php

class Solution {

    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function maxProfit($prices) {
        $max = 0;
        $b = PHP_INT_MAX;
        foreach ($prices as $pr) {
            if ($pr>$b) {
                $d = $pr - $b;
                if ($d>$max) $max = $d;
            } else {
                $b = $pr;
            }
        }
        return $max;
    }
}

$prices = [7,1,5,3,6,4];
$so = new Solution();
$r = $so->maxProfit($prices);
print_r($r);