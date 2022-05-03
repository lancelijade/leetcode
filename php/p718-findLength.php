<?php

class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function findLength($nums1, $nums2) {
        
        $r = 0;
        $dp = [];

        for ($i=count($nums1)-1; $i>=0; $i--) {
            for ($j=count($nums2)-1; $j>=0; $j--) {
                if ($nums1[$i]==$nums2[$j]) {
                    $dp[$i][$j] = ($dp[$i+1][$j+1] ?? 0) + 1;
                    $r = max($r, $dp[$i][$j]);
                }
            }
        }

        return $r;
    }
}

$nums1 = [1,2,3,2,1]; $nums2 = [3,2,1,4,7];
$nums1 = [0,0,0,0,0]; $nums2 = [0,0,0,0,0];
$nums1 = [70,39,25,40,7]; $nums2 = [52,20,67,5,31];

$so = new Solution();
$r = $so->findLength($nums1, $nums2);
print_r($r);