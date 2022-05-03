<?php

class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function isValid($s) {
        $map = [
            "(" => ")",
            "{" => "}",
            "[" => "]",
        ];

        $next = [];
        for ($i=0; $i<strlen($s); $i++) {
            if (isset($map[$s[$i]])) 
                array_unshift($next, $map[$s[$i]]);
            elseif ($s[$i] != array_shift($next)) {
                return false;
            }
        }
        if ($next) return false;
        return true;
    }
}

$s = "()[]";
$so = new Solution();
$r = $so->isValid($s);
print_r($r);