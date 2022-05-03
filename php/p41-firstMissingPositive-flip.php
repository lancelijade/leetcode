<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function firstMissingPositive($nums) {

        $nums = array_flip($nums);
        
        $f = 1;
        
        while(isset($nums[$f++])) {
        }
        
        return $f-1;
    }
}

$nums = [1];
$so = new Solution();
$r = $so->firstMissingPositive($nums);
print_r($r);
