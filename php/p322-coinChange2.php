<?php

class Solution {

    private $coins;
    private $amount;
    private $cache = [];

    function dp($i) {

        //echo $i.PHP_EOL;

        if (in_array($i, $this->coins)) return 1;
        if (isset($this->cache[$i])) return $this->cache[$i];

        $mm = PHP_INT_MAX;
        foreach ($this->coins as $coin) {
            if ($i>$coin) {
                $a = $this->dp($i - $coin);
                $mm = min($mm, $a+1);
            }
        }
        $this->cache[$i] = $mm;
        return $mm;
    }


    /**
     * @param Integer[] $coins
     * @param Integer $amount
     * @return Integer
     */
    function coinChange($coins, $amount) {
        
        if ($amount == 0) return 0;

        rsort($coins);
        if ($coins[count($coins)-1] > $amount) return -1;

        $this->coins = $coins;
        $this->amount = $amount;

        $r = $this->dp($amount);
        return ($r == PHP_INT_MAX) ? -1 : $r;
    }
}

$coins = [1,2,5];
$amount = 100;
$so = new Solution();
$r = $so->coinChange($coins, $amount);
print_r($r);