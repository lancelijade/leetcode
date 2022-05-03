<?php

class Solution {

    /**
     * @param Integer[][] $intervals
     * @return Integer
     */
    function removeCoveredIntervals($intervals) {
        $ivs = [];
        foreach ($intervals as $ints) {
            $e = $ints[1] - $ints[0];
            $ivs[$e][] = $ints[0];
        }
        ksort($ivs);
        $ivsr = $ivs;
        krsort($ivsr);

        //print_r($ivs);

        $r = [];
        foreach ($ivs as $k1=>$v1) {
            foreach ($ivsr as $k2=>$v2) {
                $e = $k2 - $k1;
                //echo "e=$e\n";
                if ($e<=0) continue;
                foreach ($v1 as $v1n) {
                    //echo "v1n=$v1n k1=$k1\n";
                    foreach ($v2 as $v2n) {
                        //echo "v2n=$v2n k2=$k2\n";
                        if ($v1n>=$v2n and $v1n+$k1<=$v2n+$k2) {
                            $r[$v1n.'-'.$k1] = "$v1n, $k1, $v2n, $k2";
                            //print_r($r);
                            continue 2;
                        }
                    }
                }
            }
        }

        return count($intervals)-count($r);
    }
}

//$intervals = [[34335,39239],[15875,91969],[29673,66453],[53548,69161],[40618,93111]];
$intervals = [[1,2],[0,4],[3,4]];

$so = new Solution();
$r = $so->removeCoveredIntervals($intervals);
print_r($r);