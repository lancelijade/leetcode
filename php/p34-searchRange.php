<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function searchRange($nums, $target) {
        $left = -1;
        $right = -1;

        $cnt = count($nums);

        for ($i=0; $i<$cnt; $i++) {
            if ($nums[$i] == $target) {
                $left = $i;
                break;
            }
        }

        for ($i=$cnt-1; $i>=0; $i--) {
            if ($nums[$i] == $target) {
                $right = $i;
                break;
            }
        }

        return [$left, $right];
    }
}

$nums = [5,7,7,8,8,10];
$target = 8;

$so = new Solution();
$r = $so->searchRange($nums, $target);
print_r($r);
