<?php

class Solution {

    /**
     * @param String $digits
     * @return String[]
     */
    function letterCombinations($digits) {

        if ($digits=="") return [];

        $map = [
            '2' => 'abc',
            '3' => 'def',
            '4' => 'ghi',
            '5' => 'jkl',
            '6' => 'mno',
            '7' => 'pqrs',
            '8' => 'tuv',
            '9' => 'wxyz',
        ];

        $re = str_split($map[$digits[0]]);

        $p = 1;
        while ($p<strlen($digits)) {
            $t = 0;
            //$t = array_shift($re);
            $re1 = [];
            while ($re[$t]) {
                for ($i=0; $i<strlen($map[$digits[$p]]); $i++)
                {
                    $re1[] = $re[$t].$map[$digits[$p]][$i];
                }
                $t++;
            }
            $re = $re1;

            //print_r($re);
            $p++;
        }
        
        return $re;
    }
}

$digits = "2";
$so = new Solution();
$r = $so->letterCombinations($digits);
print_r($r);