<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[][]
     */
    function fourSum($nums, $target) {

        $nums2 = array_count_values($nums);

        //print_r($nums2);


        $keys2 = array_keys($nums2);
        $len = count($keys2);
        $sum2 = [];
        for ($i=0; $i<$len; $i++) {
            for ($j=$i; $j<$len; $j++) {
                $s = $keys2[$i] + $keys2[$j];
                $sum2[$s][] = [$keys2[$i], $keys2[$j]];
            }
        }
        //print_r($sum2);


        $re = [];
        foreach ($sum2 as $s2 => $s2v) {
            $t = $target - $s2;
            if (isset($sum2[$t])) {
                $aa = $s2v;
                $bb = $sum2[$t];
                foreach ($aa as $a) {
                    foreach ($bb as $b) {
                        //if ($a == $b) continue;
                        $tt = array_merge($a, $b);
                        $ttc = array_count_values($tt);
                        $can = true;
                        foreach ($ttc as $k => $v) {
                            if ($nums2[$k]<$v) {
                                $can = false;
                                break;
                            }
                        }

                        if ($can) {
                            sort($tt);
                            $k = join('.', $tt);
                            $re[$k] = $tt;
                               
                        }
                    }
                }                                
            }
        }

        return array_values($re);
    }
}

//$nums = [2,2,2,2,2];
//$target = 8;
$nums = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90];
$target = 200;
$nums = [1,0,-1,0,-2,2];
$target = 0;
$so = new Solution();
$r = $so->fourSum($nums, $target);
print_r($r);