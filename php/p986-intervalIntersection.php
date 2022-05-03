<?php

class Solution {

    /**
     * @param Integer[][] $firstList
     * @param Integer[][] $secondList
     * @return Integer[][]
     */
    function intervalIntersection($firstList, $secondList) {

        $r = [];
        
        $sec1 = array_shift($firstList);
        $sec2 = array_shift($secondList);
    
        while ($sec1 and $sec2) {
            
            echo join(',', $sec1).' '.join(',', $sec2).PHP_EOL;
            
            if ($sec1[1]<$sec2[0]) {
                $sec1 = array_shift($firstList);
                continue;
            }

            if ($sec1[0]>$sec2[1]) {
                $sec2 = array_shift($secondList);
                continue;
            }
            
            echo join(',', $sec1).' -- '.join(',', $sec2).PHP_EOL;
            $r[] = [max($sec1[0], $sec2[0]), min($sec1[1], $sec2[1])];

            if ($sec1[1]<$sec2[1]) {
                $sec1 = array_shift($firstList);
            } elseif ($sec1[1]>$sec2[1]) {
                $sec2 = array_shift($secondList);
            } else {
                $sec1 = array_shift($firstList);
                $sec2 = array_shift($secondList);
            }
        }

        return $r;
    }
}

$firstList = [[0,2],[5,10],[13,23],[24,25]];
$secondList = [[1,5],[8,12],[15,24],[25,26]];
$firstList = [[1,3],[5,9]];
$secondList = [];
$so = new Solution();
$r = $so->intervalIntersection($firstList, $secondList);
print_r($r);