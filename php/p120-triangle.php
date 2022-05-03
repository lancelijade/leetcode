<?php

class Solution {

    /**
     * @param Integer[][] $triangle
     * @return Integer
     */
    function minimumTotal($triangle) {
        
        $dp[0][0] = $triangle[0][0];
        $dp[1][0] = $triangle[1][0] + $triangle[0][0];
        $dp[1][1] = $triangle[1][1] + $triangle[0][0];

        $lvls = count($triangle);
        //print_r($dp);
        for ($lvl=2; $lvl<$lvls; $lvl++) {
            for ($i=0; $i<$lvl+1; $i++) {
                if ($i==0) {
                    $dp[$lvl][0] = $dp[$lvl-1][0] + $triangle[$lvl][0];
                } else {
                    $a = $dp[$lvl-1][$i-1];
                    $b = isset($dp[$lvl-1][$i]) ? $dp[$lvl-1][$i] : PHP_INT_MAX;
                    $dp[$lvl][$i] = min($a, $b) + $triangle[$lvl][$i];
                }
            }
            //print_r($dp);
        }

        return min($dp[$lvls-1]);
    }
}

$triangle = [[2],[3,4],[6,5,7],[4,1,8,3]];
$so = new Solution();
$r = $so->minimumTotal($triangle);
print_r($r);