<?php

class Solution {

    /**
     * @param Integer[][] $matrix
     * @return NULL
     */
    function rotate(&$matrix) {
        
        $len = count($matrix);

        for ($i=0; $i<$len; $i++) {
            for ($j=0; $j<$len; $j++) {
                $x = $j;
                $y = $len - $i - 1;
                if (!is_array($matrix[$i][$j])) {
                    $matrix[$x][$y] = [$matrix[$x][$y], $matrix[$i][$j]];
                } else {
                    $matrix[$x][$y] = [$matrix[$x][$y], $matrix[$i][$j][0]];
                    $matrix[$i][$j] = $matrix[$i][$j][1];
                }

                //print_r($matrix);
                //exit;
            }
        }

        for ($i=0; $i<$len; $i++) {
            for ($j=0; $j<$len; $j++) {
                if (is_array($matrix[$i][$j])) $matrix[$i][$j] = $matrix[$i][$j][1];
            }
        }        
    }
    
}

$matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]];
$so = new Solution();
$r = $so->rotate($matrix);
print_r($matrix);