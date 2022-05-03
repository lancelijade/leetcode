<?php

class Solution {

    private $prices;
    private $c = [];

    function dp($i, $holding) {
        
        if (!isset($this->prices[$i])) return 0;
        if (isset($this->c["$i-$holding"])) return $this->c["$i-$holding"];

        if ($holding == 2) {    // cooldowning
            $doNothing = $this->dp($i+1, 0);
        } else {
            $doNothing = $this->dp($i+1, $holding);
        }

        if ($holding == 1) {    // sell
            $doSomething = $this->prices[$i] + $this->dp($i+1, 2);
        } elseif ($holding == 0) {                // buy
            $doSomething = -$this->prices[$i] + $this->dp($i+1, 1);
        } else {
            $doSomething = 0;
        }

        $ma = max($doNothing, $doSomething);
        $this->c["$i-$holding"] = $ma;

        //print_r($this->c);

        return $ma;
    }
    
    
    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function maxProfit($prices) {
        
        $this->prices = $prices;
        return $this->dp(0, 0);
    }
}

$prices = [1,2,3,0,2];
//$prices = [1];
$so = new Solution();
$r = $so->maxProfit($prices);
print_r($r);