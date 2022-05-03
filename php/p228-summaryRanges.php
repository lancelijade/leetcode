<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return String[]
     */
    function summaryRanges($nums) {
        $cnt = count($nums);
        if ($cnt == 0) return [];
        if ($cnt == 1) return ["{$nums[0]}"];

        $left = 0;
        $right_last = $left;
        $right = 1;

        $r = [];
        while ($right<$cnt) {
            echo "$left $right".PHP_EOL;
            if ($nums[$right] - $nums[$right_last] > 1) {
                if ($right_last != $left) $r[] = "{$nums[$left]}->{$nums[$right_last]}";
                else $r[] = "{$nums[$left]}";
                $left = $right_last + 1;
            }
            $right_last = $right;
            $right++;
        }

        //if ($nums[$right] - $nums[$right_last] > 1) {
            if ($right_last != $left) $r[] = "{$nums[$left]}->{$nums[$right_last]}";
            else $r[] = "{$nums[$left]}";

        return $r;
    }
}

//$nums = [0,1,2,4,5,7];
$nums = [0,2,3,4,6,8,9];
$nums = [1,2];
$so = new Solution();
$r = $so->summaryRanges($nums);
print_r($r);