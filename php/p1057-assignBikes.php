<?php

class Solution {

    /**
     * @param Integer[][] $workers
     * @param Integer[][] $bikes
     * @return Integer[]
     */
    function assignBikes($workers, $bikes) {
        
        $cntw = count($workers);
        $cntb = count($bikes);
        $md = [];

        for ($i=0; $i<$cntw; $i++) {
            for ($j=0; $j<$cntb; $j++) {
                $dis = abs($workers[$i][0]-$bikes[$j][0]) + abs($workers[$i][1]-$bikes[$j][1]);
                $md["$i-$j"] = $dis;
                $wo[$i] = [$dis, $j];
                $bi[$j] = [$dis, $i];
            }
        }
        asort($md);
        //print_r($md);

        $used_wo = [];
        $used_bi = [];
        $r = [];
        foreach ($md as $k => $v) {

            list($wo, $bi) = explode('-', $k);
            if (!isset($r[$wo]) and !isset($used_bi[$bi])) {
                $r[$wo] = $bi;
                $used_bi[$bi] = 1;
            }
        }

        ksort($r);
        return $r;
    }
}

$workers = [[0,0],[2,1]];
$bikes = [[1,2],[3,3]];

//$workers = [[0,0],[1,1],[2,0]];
//$bikes = [[1,0],[2,2],[2,1]];

$so = new Solution();
$r = $so->assignBikes($workers, $bikes);
print_r($r);