<?php

class Solution {

    public $nums;

    function half($target, $s, $e) {

        echo "$s $e".PHP_EOL;
        $vs = $this->nums[$s];
        $ve = $this->nums[$e];

        if ($target == $vs) return $s;
        if ($target == $ve) return $e;
        
        if (($s == $e) or ($e - $s == 1)) {
            if ($target > $ve) return $e + 1;
            elseif ($target < $vs) return $s;
            else return $s + 1;
        }

        $mid = floor(($s + $e) / 2);
        if ($target == $this->nums[$mid]) {
            return $mid;
        } else {
            if ($target > $this->nums[$mid]) return $this->half($target, $mid+1, $e);
            else return $this->half($target, $s, $mid-1);
        }

    }

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function searchInsert($nums, $target) {
        $this->nums = $nums;
        $cnt = count($nums);
        $r = $this->half($target, 0, $cnt-1);
        return $r;
    }
}

$nums = [1];
$target = 2;

$so = new Solution();
$r = $so->searchInsert($nums, $target);
print_r($r);