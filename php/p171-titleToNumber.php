<?php

class Solution {

    /**
     * @param String $columnTitle
     * @return Integer
     */
    function titleToNumber($columnTitle) {
        $len = strlen($columnTitle);
        $sum = 0;
        for ($i=$len-1; $i>=0; $i--) {
            //echo "{$columnTitle[$i]}\n";
            $sum += (ord($columnTitle[$i])-ord('A')+1) * pow(26, $len-$i-1);
        }
        return $sum;
    }
}

$columnTitle = "FXSHRXW";
$so = new Solution();
$r = $so->titleToNumber($columnTitle);
print_r($r);