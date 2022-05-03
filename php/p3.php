<?php

class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function lengthOfLongestSubstring($s) {
        $map = array();
        $p = 0;
        $len = 0;

        for ($i=0; $i<strlen($s); $i++)
        {
            $c = ord($s[$i]);
            if (array_key_exists($c, $map) and $map[$c]>=$p) {
                $p = $map[$c] + 1;
                $map[$c] = $i;
                
            } else {
                $map[$c] = $i;
                $len_new = $i - $p + 1;
                if ($len_new > $len) $len = $len_new;
            }
            //echo $p." ".$len."\n";
            //print_r($map);
        }

        return $len;
    }
}

$s = "abcabcbb";

$so = new Solution();
$r = $so->lengthOfLongestSubstring($s);
print_r($r);