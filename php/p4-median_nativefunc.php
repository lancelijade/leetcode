<?php

class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Float
     */
    function findMedianSortedArrays($nums1, $nums2) {
        
        $a = array_merge($nums1, $nums2);
        sort($a);
        $n = count($a);
        if ($n%2==0)
            return ($a[$n/2-1]+$a[$n/2])/2;
        else
            return $a[$n/2-0.5];
    }
}

$nums1 = array(1,2,12);
$nums2 = array(15);

$so = new Solution();
$r = $so->findMedianSortedArrays($nums1, $nums2);
print_r($r);