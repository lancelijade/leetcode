<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function searchRange($nums, $target) {

        $left = array_search($target, $nums);
        if ($left === false) {
            return [-1, -1];
        }

        $cnt = count($nums);
        $nums = array_reverse($nums);
        //print_r($nums);
        $right = array_search($target, $nums);

        return [$left, $cnt - $right - 1];
    }
}

$nums = [1];
$target = 1;

$so = new Solution();
$r = $so->searchRange($nums, $target);
print_r($r);
