<?php

class Solution {


    /**
     * @param Integer[] $coins
     * @param Integer $amount
     * @return Integer
     */
    function coinChange($coins, $amount) {
        
        if ($amount == 0) return 0;

        $dp = [];
        foreach ($coins as $coin) $dp[$coin] = 1;

        for ($i=1; $i<=$amount; $i++) {
            
            if (isset($dp[$i])) continue;

            $mm = PHP_INT_MAX;
            foreach ($coins as $coin) {
                if ($i>$coin and isset($dp[$i-$coin])) {
                    $a = $dp[$i-$coin];
                    $mm = min($mm, $a+1);
                }
            }
            $dp[$i] = $mm;
        }

        return ($dp[$amount] == PHP_INT_MAX) ? -1 : $dp[$amount];
    }
}

$coins = [1,2,5];
$amount = 100;
$so = new Solution();
$r = $so->coinChange($coins, $amount);
print_r($r);