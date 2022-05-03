<?php

class Solution {

    /**
     * @param String $s
     * @param String $p
     * @return Boolean
     */
    function isMatch($s, $p) {
        $pat = '/^'.$p.'$/';
        return preg_match($pat, $s);
    }
}

$s = "aa";
$p = ".*";

$so = new Solution();
$r = $so->isMatch($s, $p);
print_r($r);