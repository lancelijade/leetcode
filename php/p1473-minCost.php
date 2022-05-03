<?php

class Solution {

    private $houses;
    private $cost;
    private $n;
    private $target;
    private $cache = [];

    private $cnt;

    function dp($i, $color, $neighborhood) {

        //echo "i=$i color=$color neighbor=$neighborhood".PHP_EOL;
        //if ($this->cnt++==100) exit;

        if ($neighborhood<=0) return PHP_INT_MAX;

        if ($i==0) {
            if ($neighborhood != 1) {
                return PHP_INT_MAX;
            } elseif (!$this->houses[$i]) {
                return $this->cost[$i][$color-1];
            } else {
                if ($this->houses[$i] == $color) return 0;
                else return PHP_INT_MAX;
            }
        }

        if (isset($this->cache[$i][$color][$neighborhood])) return $this->cache[$i][$color][$neighborhood];

        if ($this->houses[$i]) {
            if ($this->houses[$i] == $color) {
                $r = PHP_INT_MAX;
                for ($c=1; $c<=$this->n; $c++) {
                    if ($c==$color) $r = min($r, $this->dp($i-1, $c, $neighborhood));
                    else $r = min($r, $this->dp($i-1, $c, $neighborhood-1));
                }

            } else {
                return PHP_INT_MAX;
            }

        } else {
            $r = PHP_INT_MAX;
            for ($c=1; $c<=$this->n; $c++) {
                if ($c==$color) $r = min($r, $this->dp($i-1, $c, $neighborhood) + $this->cost[$i][$color-1]);
                else $r = min($r, $this->dp($i-1, $c, $neighborhood-1) + $this->cost[$i][$color-1]);
            }            
        }

        $this->cache[$i][$color][$neighborhood] = $r;
        return $r;        
    }


    /**
     * @param Integer[] $houses
     * @param Integer[][] $cost
     * @param Integer $m
     * @param Integer $n
     * @param Integer $target
     * @return Integer
     */
    function minCost($houses, $cost, $m, $n, $target) {
        
        $this->houses = $houses;
        $this->cost = $cost;
        $this->n = $n;
        $this->target = $target;

        $r = PHP_INT_MAX;
        for ($i=1; $i<=$n; $i++) {
            $r = min($r, $this->dp($m-1, $i, $target));
        }

        //print_r($this->cache);
        if ($r == PHP_INT_MAX) return -1;
        else return $r;
    }
}

$houses = [0,0,0,0,0]; $cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]; $m = 5; $n = 2; $target = 3;
$houses = [0,2,1,2,0]; $cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]; $m = 5; $n = 2; $target = 3;
$houses = [3,1,2,3]; $cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]; $m = 4; $n = 3; $target = 3;
$houses = [0,0,0,1]; $cost = [[1,5],[4,1],[1,3],[4,4]]; $m = 4; $n = 2; $target = 4;

$so = new Solution();
$r = $so->minCost($houses, $cost, $m, $n, $target);
print_r($r);