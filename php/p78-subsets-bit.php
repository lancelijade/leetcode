<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function subsets($nums) {
        $ans = [ [] ];
        
        foreach ($nums as $n) {
            foreach ($ans as $a) {
                $ans[] = array_merge($a, [$n]);
            }
            print_r($ans);
        }
        
        return $ans;
    }
}

$nums = [1,2,3];

$so = new Solution();
$r = $so->subsets($nums);
print_r($r);