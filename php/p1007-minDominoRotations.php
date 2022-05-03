<?php

class Solution {

    /**
     * @param Integer[] $tops
     * @param Integer[] $bottoms
     * @return Integer
     */
    function minDominoRotations($tops, $bottoms) {
        
        $va = array_count_values($tops);
        $vb = array_count_values($bottoms);
        $cnt = count($tops);
        
        arsort($va);
        arsort($vb);

        foreach ($va as $k1 => $n1) break;
        foreach ($vb as $k2 => $n2) break;

        $r1 = 0;
        $r2 = 0;
        for ($i=0; $i<$cnt; $i++) {
            //echo "$i {$tops[$i]} {$bottoms[$i]} $k1 $r1".PHP_EOL;
            if ($tops[$i]!==$k1) {
                if ($bottoms[$i]===$k1) {
                    $r1++;
                } else {
                    $r1 = PHP_INT_MAX;
                    break;
                }
            }
        }

        for ($i=0; $i<$cnt; $i++) {
            if ($bottoms[$i]!==$k2) {
                if ($tops[$i]===$k2) {
                    $r2++;
                } else {
                    $r2 = PHP_INT_MAX;
                    break;
                }
            }
        }        

        $r = min($r1, $r2);
        return $r == PHP_INT_MAX ? -1 : $r;
    }
}

$tops = [2,1,2,4,2,2];
$bottoms = [5,2,6,2,3,2];
$tops = [3,5,1,2,3];
$bottoms = [3,6,3,3,4];
$so = new Solution();
$r = $so->minDominoRotations($tops, $bottoms);
print_r($r);