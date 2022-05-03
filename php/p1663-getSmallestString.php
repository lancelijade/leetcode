<?php

class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return String
     */
    function getSmallestString($n, $k) {
        
        $c = floor($k / 26);
        $a = $k % 26;

        echo "a=$c c=$c".PHP_EOL;

        $s = '';
        if ($a+$c == $n) {
            $r = str_repeat('a', $a).str_repeat('z', $c);
            return $r;

        } elseif ($a+$c < $n) {
            $x = ceil(($n - $a - $c) / 25);
            $c -= $x;

        }

        $a = $n - $c - 1;
        $b = $k - $c*26 - $a - 1;
        $s = chr(ord('a') + $b);

        $r = str_repeat('a', $a).$s.str_repeat('z', $c);
        return $r;
    }
}

$n = 3; $k = 27;
$n = 5; $k = 73;
$n = 2; $k = 28;
$n = 24; $k= 552;
$n = 5; $k = 130;
//$n = 80; $k = 576;
//$n = 23100; $k=567226;


$so = new Solution();
$r = $so->getSmallestString($n, $k);
print_r($r);