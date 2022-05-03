<?php

class Solution {

    private $nvs;
    private $cache = [];
    private $debug = 1;

    function maxP($n) {
        if ($n == 0) return 0;
        if (isset($this->cache[$n])) return $this->cache[$n];
        $a = isset($this->nvs[$n]) ? $this->nvs[$n] : 0;
        $t = max($this->maxP($n-1), $this->maxP($n-2) + $a);
        $this->cache[$n] = $t;
        return $t;
    }

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function deleteAndEarn($nums) {
        
        $nvs = array_count_values($nums);
        foreach ($nvs as $n => &$v) $v = $n * $v;
        if (!isset($nvs[1])) {
            $this->cache[1] = 0;
        } else {
            $this->cache[1] = $nvs[1];
        }
        //krsort($nvs);
        $this->nvs = $nvs;

        if ($this->debug) {
            echo "nvs=";
            print_r($this->nvs); 
        }

        $this->maxP(max(array_keys($nvs)));

        if ($this->debug) print_r($this->cache);

        return max($this->cache);
    }
}

$nums = [4,10,10,8,1,4,10,9,7,6];
//$nums = [2,2,3,3,3,4];
//$nums = [1];
//$nums = [8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4];
//$nums = [8,7,3,8,1,4,10,10,10,2];
$nums = [1,2,3,15,16,17,18];
$so = new Solution();
$r = $so->deleteAndEarn($nums);
print_r($r);