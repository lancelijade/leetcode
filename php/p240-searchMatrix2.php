<?php

class Solution {

    /**
     * @param Integer[][] $matrix
     * @param Integer $target
     * @return Boolean
     */
    function searchMatrix($matrix, $target) {
        
        $m = count($matrix);
        $n = count($matrix[0]);

        for ($i=0; $i<$m; $i++) {

            if ($matrix[$i][0]==$target) return true;
            elseif ($matrix[$i][0]>$target) return false;

            if ($matrix[$i][0]<=$target and end($matrix[$i])>=$target) {
                for ($j=0; $j<$n; $j++) {
                    if ($matrix[$i][$j]==$target) return true;
                }
            }
        }

        return false;
    }
}

$matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]];
$target = 20;
$matrix = [[-1,3]];
$target = 3;
$so = new Solution();
$r = $so->searchMatrix($matrix, $target);
var_dump($r);