<?php

class Solution {

    /**
     * @param String $s
     * @return String[]
     */
    function letterCasePermutation($s) {
        
        $s = strtolower($s);
        $p = [];
        for ($i=0; $i<strlen($s); $i++) {
            if ($s[$i]>='a' and $s[$i]<='z') $p[] = $i;
        }

        $r = [];
        $c = count($p);
        //print_r($p);
        for ($n=0; $n<pow(2,$c); $n++) {
            $s1 = $s;
            $bit = 0;
            $n1 = $n;

            //echo $n.PHP_EOL;
            while ($n1) {
                //echo "$n1 $s1 $bit {$s1[$p[$bit]]}".PHP_EOL;
                if ($n1 & 1) $s1[$p[$bit]] = strtoupper($s1[$p[$bit]]);
                //echo $s1[$p[$bit]].PHP_EOL;
                $n1 = $n1 >> 1;
                $bit++;
                //echo "$n1 $s1 $bit ".PHP_EOL;
                //exit;
            }

            $r[] = $s1;
        }

        return $r;
    }
}


$s = "a1b2";
$so = new Solution();
$r = $so->letterCasePermutation($s);
print_r($r);