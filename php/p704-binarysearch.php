<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function search($nums, $target) {
        $left = 0;
        $right = count($nums) - 1;

        while ($left < $right) {

            if ($nums[$left] == $target) return $left;
            elseif ($nums[$right] == $target) return $right;

            $mid = floor(($left + $right) / 2);
            if ($nums[$mid] == $target) {
                return $mid;
            } elseif ($nums[$mid] > $target) {
                $right = $mid - 1;
            } else {
                $left = $mid + 1;
            }
        }

        if ($nums[$left] == $target) return $left;
        else return -1;
    }
}


$nums = [-1,0,3,5,9,12];
$target = 2;
$so = new Solution();
$r = $so->search($nums, $target);
print_r($r);