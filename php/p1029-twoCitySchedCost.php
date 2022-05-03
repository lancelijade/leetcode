<?php

class Solution {

    private $costs;
    private $cache;

    function c($pos, $n) {

        echo "pos=$pos n=$n".PHP_EOL;

        if ($n==0) {
            if ($pos>0) return $this->c($pos-1,0) + $this->costs[$pos][1];
            else return $this->costs[0][1];

        } elseif ($pos==0 and $n==1) {
            return $this->costs[0][0];

        } elseif ($pos==0 and $n>1) {
            return PHP_INT_MAX;
        }

        if (isset($this->cache[$pos][$n])) return $this->cache[$pos][$n];

        $c0 = $this->c($pos-1,$n) + $this->costs[$pos][1];
        $c1 = $this->c($pos-1,$n-1) + $this->costs[$pos][0];
        $m = min($c0, $c1);
        $this->cache[$pos][$n] = $m;

        return $m;
    }


    /**
     * @param Integer[][] $costs
     * @return Integer
     */
    function twoCitySchedCost($costs) {
        
        $this->costs = $costs;
        $cnt = count($costs);
        return $this->c($cnt-1, $cnt/2);
    }
}

$costs = [[10,20],[30,200],[400,50],[30,20]];
$costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]];
$costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]];
$so = new Solution();
$r = $so->twoCitySchedCost($costs);
print_r($r);