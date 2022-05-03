<?php

class Solution {

    /**
     * @param Integer $poured
     * @param Integer $query_row
     * @param Integer $query_glass
     * @return Float
     */
    function champagneTower($poured, $query_row, $query_glass) {

        $a = [];
        for ($i=0; $i<=$query_row; $i++) {
            $a[$i] = array_fill(0, $query_row+1, 0);
        }

        $a[0][0] = $poured;
        for ($row=0; $row<$query_row; $row++) {
            for ($c=0; $c<=$row; $c++) {
                $q = ($a[$row][$c] - 1)/2;
                if ($q > 0) {
                    $a[$row+1][$c] += $q;
                    $a[$row+1][$c+1] += $q;
                }
            }
        }

        return min(1, $a[$query_row][$query_glass]);
    }
}

$poured = 2;
$query_row = 1;
$query_glass = 1;
$so = new Solution();
$r = $so->champagneTower($poured, $query_row, $query_glass);
print_r($r);