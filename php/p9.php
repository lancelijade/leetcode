<?php

class Solution {

    /**
     * @param Integer $x
     * @return Boolean
     */
    function isPalindrome($x) {
        if ((int)strrev($x) == $x) return true;
        else return false;
    }
}

$x = 10;

$so = new Solution();
$r = $so->isPalindrome($x);
print_r($r);