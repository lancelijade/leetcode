<?php

class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Float
     */
    function findMedianSortedArrays($nums1, $nums2) {
        
        $p1 = 0;
        $p2 = 0;
        $m = count($nums1);
        $n = count($nums2);
        $cnt = 0;

        if (($m + $n) % 2 <> 0) {

            $t = ($m + $n)/2 - 0.5;
            //echo "t=$t\n";
            while ($cnt < $t+1) {
                
                //echo "$cnt $t | $p1 $p2 | {$nums1[$p1]} {$nums2[$p2]}\n";
                if (!array_key_exists($p1, $nums1)) {// no numbers left in $nums1
                    $p2 += $t - $cnt;
                    return $nums2[$p2];
                } 
                elseif (!array_key_exists($p2, $nums2)) {// no numbers left in $nums2
                    $p1 += $t - $cnt;
                    return $nums1[$p1];
                } 
                else {
                    if ($nums1[$p1]>=$nums2[$p2]) {
                        $cnt++;
                        if ($cnt==$t+1) return $nums2[$p2];
                        else $p2++;
                    } else {
                        $cnt++;
                        if ($cnt==$t+1) return $nums1[$p1];
                        else $p1++;
                    }
                    
                }
                //echo "$cnt $t | $p1 $p2 | {$nums1[$p1]} {$nums2[$p2]}\n=====\n";
            }


        } else {
            $t = ($m + $n)/2 - 1;
            $r0 = 0;
            //echo "t=$t\n";
            while ($cnt < $t+1) {
                
                if (!array_key_exists($p1, $nums1)) {// no numbers left in $nums1
                    $p2 += $t - $cnt;
                    return ($nums2[$p2+1]+$nums2[$p2])/2;
                    
                } 
                elseif (!array_key_exists($p2, $nums2)) {// no numbers left in $nums2
                    $p1 += $t - $cnt;
                    return ($nums1[$p1+1]+$nums1[$p1])/2;
                } 
                else {
                    if ($nums1[$p1]>=$nums2[$p2]) {
                        $cnt++;
                        if ($cnt==$t+1) $r0 = $nums2[$p2];
                        $p2++;
                    } else {
                        $cnt++;
                        if ($cnt==$t+1) $r0 = $nums1[$p1];
                        $p1++;
                    }
                    
                }
                //echo "$cnt $t | $p1 $p2 | {$nums1[$p1]} {$nums2[$p2]}\n";
            }

            if (!array_key_exists($p1, $nums1)) {// no numbers left in $nums1
                $p2 += $t - $cnt;
                return ($nums2[$p2+1]+$r0)/2;
                
            } 
            elseif (!array_key_exists($p2, $nums2)) {// no numbers left in $nums2
                $p1 += $t - $cnt;
                return ($nums1[$p1+1]+$r0)/2;
            } 
            
            if ($nums1[$p1]>=$nums2[$p2]) {
                return ($nums2[$p2]+$r0)/2;
            } else {
                return ($nums1[$p1]+$r0)/2;
            }
                

        }
    }
}

$nums1 = array(1,2,12);
$nums2 = array(4);

$so = new Solution();
$r = $so->findMedianSortedArrays($nums1, $nums2);
print_r($r);