<?php

class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function isSubsequence($s, $t) {

        if ($s == $t) return true;
        if (!$t) return false;

        $si = 0;
        $lens = strlen($s);
        $ti = -1;
        $lent = strlen($t);

        while ($si<$lens and $ti<$lent) {
            echo "si=$si s[i]={$s[$si]} ti=$ti".PHP_EOL;
            $tn = strpos($t, $s[$si], $ti+1);
            if ($tn===false) return false;

            $ti = $tn;
            $si++;
        }

        return true;
    }
}

$s = "abc";
$t = "ahbgdc";
$so = new Solution();
$r = $so->isSubsequence($s, $t);
print_r($r);