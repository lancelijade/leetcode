<?php

class Solution {

    private $prices;
    private $c = [];

    function dp($i, $transRemaining, $holding) {

        if ($i == count($this->prices) or $transRemaining == 0) return 0;
        if (isset($this->c["$i-$transRemaining-$holding"])) return $this->c["$i-$transRemaining-$holding"];

        $doNothing = $this->dp($i+1, $transRemaining, $holding);

        if ($holding == 1) {
            $sellStock = $this->prices[$i] + $this->dp($i+1, $transRemaining-1, 0);
            $d = $sellStock;
        } else {
            $buyStock = -$this->prices[$i] + $this->dp($i+1, $transRemaining, 1);
            $d = $buyStock;
        }

        $r = max($doNothing, $d);
        $this->c["$i-$transRemaining-$holding"] = $r;
        return $r;
    }


    /**
     * @param Integer $k
     * @param Integer[] $prices
     * @return Integer
     */
    function maxProfit($k, $prices) {
        
        $this->prices = $prices;
        return $this->dp(0, $k, 0);
    }

    function maxProfit3($k, $prices) {
        
        $dp = [];
        $n = count($prices);
        
        $dp["$n-"] = 0;
        $dp["-0-"] = 0;


    }    
}

echo 2??3;
exit;

$k = 2;
$prices = [2,4,1];
$k = 2;
$prices = [3,2,6,5,0,3];
$k = 7;
$prices = [48,12,60,93,97,42,25,64,17,56,85,93,9,48,52,42,58,85,81,84,69,36,1,54,23,15,72,15,11,94];

$so = new Solution();
$r = $so->maxProfit($k, $prices);
print_r($r);