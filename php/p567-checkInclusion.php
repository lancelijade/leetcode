<?php

class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @return Boolean
     */
    function checkInclusion($s1, $s2) {
        
        $a1 = array_count_values(str_split($s1,1));
        $len = strlen($s1);
        $len2 = strlen($s2);

        $s2s = substr($s2, 0, $len);
        $a2 = array_count_values(str_split($s2s,1));
        $p0 = 0;
        $p1 = $len-1;
        while ($p1 < $len2) {
            
            //print_r($a2);
            if ($a1 == $a2) return true;

            if ($p1 < $len2-1) {
                $a2[$s2[$p0]]--;
                if (!$a2[$s2[$p0]]) unset($a2[$s2[$p0]]);
                $p0++;
                if (!isset($a2[$s2[$p1+1]])) $a2[$s2[$p1+1]] = 1;
                else $a2[$s2[$p1+1]]++;
                $p1++;
            } else {
                break;
            }
        }

        return false;
    }
}

$s1 = "ab";
$s2 = "eidboaooo";

$so = new Solution();
$r = $so->checkInclusion($s1, $s2);
var_dump($r);