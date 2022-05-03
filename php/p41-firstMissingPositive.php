<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function firstMissingPositive($nums) {

        sort($nums);
        $cnt = count($nums);

        $k = array_search(1, $nums);
        if ($k === false) return 1;

        $v1 = 0;
        while ($k < $cnt-1) {
            $k++;
            echo "k=$k {$nums[$k-1]} {$nums[$k]}".PHP_EOL;
            $v0 = $nums[$k-1];
            $v1 = $nums[$k];
            if ($v1 - $v0 > 1) return $v0 + 1;
        }

        if ($v1) return $v1+1;
        else return 2;
    }
}

$nums = [1];
$so = new Solution();
$r = $so->firstMissingPositive($nums);
print_r($r);
