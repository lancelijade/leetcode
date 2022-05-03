<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function subsets($nums) {
        
        $len = count($nums);

        $r = array($nums, []);
        $i = array();

        if ($len>9) 
            for ($i[0]=0; $i[0]<$len; $i[0]++) 
                for ($i[1]=$i[0]+1; $i[1]<$len; $i[1]++) 
                    for ($i[2]=$i[1]+1; $i[2]<$len; $i[2]++) 
                        for ($i[3]=$i[2]+1; $i[3]<$len; $i[3]++) 
                            for ($i[4]=$i[3]+1; $i[4]<$len; $i[4]++) 
                                for ($i[5]=$i[4]+1; $i[5]<$len; $i[5]++) 
                                    for ($i[6]=$i[5]+1; $i[6]<$len; $i[6]++) 
                                        for ($i[7]=$i[6]+1; $i[7]<$len; $i[7]++) 
                                            for ($i[8]=$i[7]+1; $i[8]<$len; $i[8]++) 
                                                $r[] = [$nums[$i[0]], $nums[$i[1]], $nums[$i[2]], $nums[$i[3]], $nums[$i[4]], $nums[$i[5]], $nums[$i[6]], $nums[$i[7]], $nums[$i[8]]];


        if ($len>8) 
            for ($i[0]=0; $i[0]<$len; $i[0]++) 
                for ($i[1]=$i[0]+1; $i[1]<$len; $i[1]++) 
                    for ($i[2]=$i[1]+1; $i[2]<$len; $i[2]++) 
                        for ($i[3]=$i[2]+1; $i[3]<$len; $i[3]++) 
                            for ($i[4]=$i[3]+1; $i[4]<$len; $i[4]++) 
                                for ($i[5]=$i[4]+1; $i[5]<$len; $i[5]++) 
                                    for ($i[6]=$i[5]+1; $i[6]<$len; $i[6]++) 
                                        for ($i[7]=$i[6]+1; $i[7]<$len; $i[7]++) 
                                            $r[] = [$nums[$i[0]], $nums[$i[1]], $nums[$i[2]], $nums[$i[3]], $nums[$i[4]], $nums[$i[5]], $nums[$i[6]], $nums[$i[7]]];

        if ($len>7) 
            for ($i[0]=0; $i[0]<$len; $i[0]++) 
                for ($i[1]=$i[0]+1; $i[1]<$len; $i[1]++) 
                    for ($i[2]=$i[1]+1; $i[2]<$len; $i[2]++) 
                        for ($i[3]=$i[2]+1; $i[3]<$len; $i[3]++) 
                            for ($i[4]=$i[3]+1; $i[4]<$len; $i[4]++) 
                                for ($i[5]=$i[4]+1; $i[5]<$len; $i[5]++) 
                                    for ($i[6]=$i[5]+1; $i[6]<$len; $i[6]++) 
                                        $r[] = [$nums[$i[0]], $nums[$i[1]], $nums[$i[2]], $nums[$i[3]], $nums[$i[4]], $nums[$i[5]], $nums[$i[6]]];

        if ($len>6) 
            for ($i[0]=0; $i[0]<$len; $i[0]++) 
                for ($i[1]=$i[0]+1; $i[1]<$len; $i[1]++) 
                    for ($i[2]=$i[1]+1; $i[2]<$len; $i[2]++) 
                        for ($i[3]=$i[2]+1; $i[3]<$len; $i[3]++) 
                            for ($i[4]=$i[3]+1; $i[4]<$len; $i[4]++) 
                                for ($i[5]=$i[4]+1; $i[5]<$len; $i[5]++) 
                                    $r[] = [$nums[$i[0]], $nums[$i[1]], $nums[$i[2]], $nums[$i[3]], $nums[$i[4]], $nums[$i[5]]];

        if ($len>5) {
            for ($i[0]=0; $i[0]<$len; $i[0]++) {
                for ($i[1]=$i[0]+1; $i[1]<$len; $i[1]++) {
                    for ($i[2]=$i[1]+1; $i[2]<$len; $i[2]++) {
                        for ($i[3]=$i[2]+1; $i[3]<$len; $i[3]++) {
                            for ($i[4]=$i[3]+1; $i[4]<$len; $i[4]++) {
                                $r[] = [$nums[$i[0]], $nums[$i[1]], $nums[$i[2]], $nums[$i[3]], $nums[$i[4]]];
                            }
                        }
                    }
                }
            }
        }
        
        if ($len>4) {
            for ($i[0]=0; $i[0]<$len; $i[0]++) {
                for ($i[1]=$i[0]+1; $i[1]<$len; $i[1]++) {
                    for ($i[2]=$i[1]+1; $i[2]<$len; $i[2]++) {
                        for ($i[3]=$i[2]+1; $i[3]<$len; $i[3]++) {
                            $r[] = [$nums[$i[0]], $nums[$i[1]], $nums[$i[2]], $nums[$i[3]]];
                        }
                    }
                }
            }
        }
        
        if ($len>3) {
            for ($i[0]=0; $i[0]<$len; $i[0]++) {
                for ($i[1]=$i[0]+1; $i[1]<$len; $i[1]++) {
                    for ($i[2]=$i[1]+1; $i[2]<$len; $i[2]++) {
                        $r[] = [$nums[$i[0]], $nums[$i[1]], $nums[$i[2]]];
                    }
                }
            }
        }

        if ($len>2) {
            for ($i[0]=0; $i[0]<$len; $i[0]++) {
                for ($i[1]=$i[0]+1; $i[1]<$len; $i[1]++) {
                    $r[] = [$nums[$i[0]], $nums[$i[1]]];
                }
            }
        }

        if ($len>1) 
            for ($i[0]=0; $i[0]<$len; $i[0]++) 
                $r[] = [$nums[$i[0]]];

        return $r;
    }
}


$nums = [0];

$so = new Solution();
$r = $so->subsets($nums);
print_r($r);