<?php

class Solution {

    /**
     * @param String $s
     * @return String[]
     */
    function expand($s) {
        
        $a = [];
        $i = 0;
        while ($i<strlen($s)) {

            if ($s[$i]!='{') {
                $a[] = $s[$i++];

            } else {
                $j = $i+1;
                while ($s[$j]!='}') $j++;
                $strb = substr($s, $i+1, $j-$i-1);
                $b = explode(',', $strb);
                //sort($b);
                $a[] = $b;
                $i = $j+1;
            }
        }

        //print_r($a);

        if (is_array($a[0])) $out = $a[0];
        else $out = [$a[0]];
        unset($a[0]);
        //echo "o0=";
        //print_r($out);

        foreach ($a as $l) {
            if (is_array($l)) {
                //echo "o2=";
                //print_r($out);
                foreach ($out as $k=>$o) {
                    //echo "o3=";
                    //print_r($out);
                    foreach ($l as $le) $out[] = $o.$le;
                    unset($out[$k]);
                }

            } else {
                foreach ($out as $k=>$o) {
                    $out[$k] .= $l;
                }
            }

            //echo "o1=";
            //print_r($out);
        }

        sort($out);
        return $out;
    }
}

$s = "{a,b}c{d,e}f";
$s = "abcd";
$so = new Solution();
$r = $so->expand($s);
print_r($r);