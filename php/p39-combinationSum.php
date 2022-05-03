<?php

class Solution {

    /**
     * @param Integer[] $candidates
     * @param Integer $target
     * @return Integer[][]
     */
    function combinationSum($candidates, $target) {

        $ta = [];
        $re = [];
        foreach ($candidates as $ca)
        {
            if ($ca != $target)
                $ta[] = [$ca, $ca, [$ca]];
            else
                $re[] = [$ca];
        }


        $t = array_shift($ta);
        while ($t) {
            //print_r($t);
            foreach ($candidates as $ca) {
                if ($ca<$t[1]) continue;
                $r = $t[0] + $ca;
                if ($r == $target) {
                    $tt = $t[2];
                    $tt[] = $ca;
                    //sort($tt);
                    //$k = join('.', $tt);
                    //$re[$k] = $tt;
                    $re[] = $tt;
                } elseif ($r<$target) {
                    $tt = $t[2];
                    $tt[] = $ca;
                    $ta[] = [$r, $ca, $tt];
                } else {
                    continue;
                }
                //print_r($ta);
            }
            $t = array_shift($ta);
        }

        //return array_values($re);
        return $re;
    }
}

$candidates = [2,3,5];
$target = 8;


$so = new Solution();
$r = $so->combinationSum($candidates, $target);
print_r($r);

