<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function sortedSquares($nums) {
        $r = [];
        foreach ($nums as $num) $r[] = $num * $num;
        sort($r);
        return $r;
    }
}

$nums = [-7,-3,2,3,11];
$so = new Solution();
$r = $so->sortedSquares($nums);
print_r($r);