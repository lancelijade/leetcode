<?php

class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function scoreOfParentheses($s) {
        
        $q = [];
        $score = [];
        
        for ($i=0; $i<strlen($s); $i++) {
            
            if ($s[$i]=='(') {
                $q[] = $i;
                continue;
                
            } else {
                $pos = array_pop($q);

                if ($i-$pos == 1) {
                    $score[$pos] = 1;

                } else {
                    $sum = 0;
                    for ($j=$pos+1; $j<$i; $j++) {
                        $sum += $score[$j] ?? 0;
                        unset($score[$j]);
                    }
                    $score[$pos] = $sum * 2;
                }
            }

            //echo "q=";
            //print_r($q);
            //echo "score=";
            //print_r($score);
        }
        
        return array_sum($score);
    }
}

$s = "((()(())))";
$so = new Solution();
$r = $so->scoreOfParentheses($s);
var_dump($r);