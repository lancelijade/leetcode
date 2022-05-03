<?php


class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function myAtoi($s) {
        if (strpos($s, 'e')!==false) {
            $parts = explode('e', $s, 2);
            if ($parts) $s = $parts[0];
        }
        $r = (int)$s;
        if ($r>2147483647) return 2147483647;
        elseif ($r<-2147483648) return -2147483648;
        else return $r;
    }
}

$s = "   -115579378e25";

$so = new Solution();
$r = $so->myAtoi($s);
print_r($r);