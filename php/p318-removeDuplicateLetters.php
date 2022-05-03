<?php

class Solution {

    /**
     * @param String $s
     * @return String
     */
    function removeDuplicateLetters($s) {
        
        $last_occurrence = [];
        for ($i=0; $i<strlen($s); $i++) {
            $last_occurrence[$s[$i]] = $i;
        }
        //print_r($last_occurrence);

        $r = [];
        $seen = [];
        for ($i=0; $i<strlen($s); $i++) {
            $c = $s[$i];
            //echo join('', $r).PHP_EOL;
            //echo $c.PHP_EOL.PHP_EOL;
            if (!isset($seen[$c])) {
                while ($r and $c<end($r) and $last_occurrence[end($r)] > $i) {
                    //echo join('', $r).PHP_EOL;
                    $t = array_pop($r);
                    unset($seen[$t]);
                }
                $seen[$c] = 1;
                $r[] = $c;
            }
        }

        return join('', $r);
    }
}



$s = "ecbacba";
$so = new Solution();
$r = $so->removeDuplicateLetters($s);
print_r($r);