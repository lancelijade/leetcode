<?php

class Solution {

    /**
     * @param Integer $amount
     * @param Integer[] $coins
     * @return Integer
     */
    function change($amount, $coins) {
        
    }
}

$amount = 5;
$coins = [1,2,5];
$so = new Solution();
$r = $so->change($amount, $coins);
print_r($r);