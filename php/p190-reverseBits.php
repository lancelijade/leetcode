<?php

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function reverseBits2($n) {
        
        $o = 0;
        for ($i=0; $i<31; $i++) {
            if ($n & 1) $o = $o | 1;
            //echo decbin($o).PHP_EOL;
            $n = $n >> 1;
            $o = $o << 1;
        }
        if ($n & 1) $o = $o | 1;
        return $o;
    }

    function reverseBits($n) {

        $s = sprintf("%032b", $n);
        $r = strrev($s);
        return bindec($r);
    }
}

$n = bindec("00000010100101000001111010011100");
$so = new Solution();
$r = $so->reverseBits($n);
echo decbin($r);