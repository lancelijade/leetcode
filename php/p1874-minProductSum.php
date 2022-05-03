<?php

class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function minProductSum($nums1, $nums2) {
        
        sort($nums1);
        rsort($nums2);

        $r = 0;
        for ($i=0; $i<count($nums1); $i++) {
            $r += $nums1[$i] * $nums2[$i];
        }

        return $r;
    }
}

$nums1 = [5,3,4,2]; $nums2 = [4,2,2,5];
$nums1 = [2,1,4,5,7]; $nums2 = [3,2,4,8,6];

$so = new Solution();
$r = $so->minProductSum($nums1, $nums2);
print_r($r);