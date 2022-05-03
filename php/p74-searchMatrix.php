<?php

class Solution {

    /**
     * @param Integer[][] $matrix
     * @param Integer $target
     * @return Boolean
     */
    function searchMatrix($matrix, $target) {
        
        $cur = 0;
        for ($i=0; $i<count($matrix); $i++) {
            if ($target > $matrix[$i][0]) $cur = $i;
            elseif ($target == $matrix[$i][0]) return true;
            else break;
        }

        $t = array_search($target, $matrix[$cur]);
        if ($t === false) return $t;
        else return true;
    }
}

$matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]];
$target = 13;

$so = new Solution();
$r = $so->searchMatrix($matrix, $target);
var_dump($r);