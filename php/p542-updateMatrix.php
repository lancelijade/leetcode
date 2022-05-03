<?php

class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer[][]
     */
    function updateMatrix($mat) {
        
        $m = count($mat);
        $n = count($mat[0]);
        $r = [];

        for ($i=0; $i<$m; $i++) {
            for ($j=0; $j<$n; $j++) {
                if ($mat[$i][$j] == 0) {
                    $r[$i][$j] = 0;
                } else {
                    if (!isset($r[$i][$j])) $r[$i][$j] = 99999999;
                    if ($i>0) $r[$i][$j] = min($r[$i][$j], $r[$i-1][$j]+1);
                    if ($j>0) $r[$i][$j] = min($r[$i][$j], $r[$i][$j-1]+1);
                }
            }
        }

        for ($i=$m-1; $i>=0; $i--) {
            for ($j=$n-1; $j>=0; $j--) {
                if ($mat[$i][$j] == 0) {
                    $r[$i][$j] = 0;
                } else {
                    if ($i<$m-1) $r[$i][$j] = min($r[$i][$j], $r[$i+1][$j]+1);
                    if ($j<$n-1) $r[$i][$j] = min($r[$i][$j], $r[$i][$j+1]+1);
                }
            }
        }

        return $r;
    }
}

$mat = [[0,0,0],[0,1,0],[1,1,1]];

$so = new Solution();
$r = $so->updateMatrix($mat);
print_r($r);