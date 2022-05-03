<?php

class Solution {

    /**
     * @param Integer $numRows
     * @return Integer[][]
     */
    function generate($numRows) {
        
        $r = [[1]];
        for ($i=1; $i<$numRows; $i++) {
            $r[$i] = [];
            for ($j=0; $j<=$i; $j++) {
                $a = isset($r[$i-1][$j-1]) ? $r[$i-1][$j-1] : 0;
                $b = isset($r[$i-1][$j]) ? $r[$i-1][$j] : 0;
                $r[$i][$j] = $a + $b;
            }
        }

        return $r;
    }
}

$numRows = 5;
$so = new Solution();
$r = $so->generate($numRows);
print_r($r);