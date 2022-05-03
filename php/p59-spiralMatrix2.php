<?php

class Solution {

    /**
     * @param Integer $n
     * @return Integer[][]
     */
    function generateMatrix($n) {
        
        $m = [[1]];
        $i = 0;
        $j = 0;
        $di = 0;
        $dj = 1;
        $c = 1;
        $to = $n * $n;
        
        while ($c<$to) {

            $i += $di;
            $j += $dj;
            if (isset($m[$i][$j]) or $i<0 or $j<0 or $i==$n or $j==$n) {
                $i -= $di;
                $j -= $dj;
                if ($di==0) {
                    $di = $dj;
                    $dj = 0;
                } else {
                    $dj = -$di;
                    $di = 0;
                }
                echo "di=$di dj=$dj".PHP_EOL;
                $i += $di;
                $j += $dj;                
            }
            $m[$i][$j] = ++$c;

            print_r($m);
            //exit;
        }

        for ($i=0; $i<$n; $i++) ksort($m[$i]);

        return $m;
    }
}

$n = 3;
$so = new Solution();
$r = $so->generateMatrix($n);
print_r($r);