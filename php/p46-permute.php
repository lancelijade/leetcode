<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function permute($nums) {
        
        $c[0] = [[0]];
        $c[1] = [[0,1], [1,0]];
        for ($i=2; $i<count($nums); $i++) {
            $c[$i] = [];

            foreach ($c[$i-1] as $cc) {
                $c[$i][] = array_merge([$i], $cc);
                for ($j=1; $j<$i; $j++) {
                    $c[$i][] = array_merge(array_slice($cc, 0, $j), [$i], array_slice($cc, $j));
                }
                $c[$i][] = array_merge($cc, [$i]);
            }
        }

        $r = [];
        foreach ($c[count($nums)-1] as $n) {
            $t = [];
            foreach ($n as $nn) {
                $t[] = $nums[$nn];
            }
            $r[] = $t;
        }

        return $r;
    }
}

$nums = [1,2,3];
$so = new Solution();
$r = $so->permute($nums);
print_r($r);