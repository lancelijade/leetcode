<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function rob($nums) {
        
        $cnt = count($nums);

        $c[0] = $nums[0];
        $c[1] = max($nums[0], $nums[1]);
        
        for ($i=2; $i<$cnt; $i++) {
            $c[$i] = max($c[$i-1], $c[$i-2]+$nums[$i]);
        }
        return $c[$cnt-1];
    }
}

$nums = [1,2,3,1];
$so = new Solution();
$r = $so->rob($nums);
print_r($r);