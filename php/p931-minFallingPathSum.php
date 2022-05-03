<?php

class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function minFallingPathSum($matrix) {
        
        $d = [];
        $rcnt = count($matrix);
        $ccnt = count($matrix[0]);

        for ($j=0; $j<$ccnt; $j++) $d[0][$j] = $matrix[0][$j];

        for ($i=1; $i<$rcnt; $i++) {
            for ($j=0; $j<$ccnt; $j++) {
                if ($j>0) 
                    $d[$i][$j] = min($d[$i-1][$j-1], $d[$i-1][$j]);
                else
                    $d[$i][$j] = $d[$i-1][$j];
                if ($j<$ccnt-1) $d[$i][$j] = min($d[$i][$j], $d[$i-1][$j+1]);

                $d[$i][$j] += $matrix[$i][$j];
            }
        }

        return min($d[$rcnt-1]);
    }
}

$matrix = [[2,1,3],[6,5,4],[7,8,9]];
$matrix = [[-19,57],[-40,-5]];

$so = new Solution();
$r = $so->minFallingPathSum($matrix);
print_r($r);