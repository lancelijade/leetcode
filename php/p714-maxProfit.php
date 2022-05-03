<?php

class Solution {

    /**
     * @param Integer[] $prices
     * @param Integer $fee
     * @return Integer
     */
    function maxProfit($prices, $fee) {
        
        $d[0][0] = 1;
        $d[0][1] = PHP_INT_MAX;

        $cnt = count($prices);
        $sum = 0;

        for ($i=1; $i<$cnt; $i++) {

            $d[$i][0] = $prices[$i] - $d[$i-1][1] - $fee;
            $d[$i][1] = min($d[$i-1][1], $prices[$i]);

            $sum += $d[$i][0];
        }

        return $sum;

    }
}

$prices = [1,3,2,8,4,9]; $fee = 2;

$so = new Solution();
$r = $so->maxProfit($prices, $fee);
print_r($r);