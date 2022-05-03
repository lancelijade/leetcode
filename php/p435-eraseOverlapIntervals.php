<?php

class Solution {

    /**
     * @param Integer[][] $intervals
     * @return Integer
     */
    function eraseOverlapIntervals($intervals) {
        
        sort($intervals);
        $cnt = count($intervals);
        print_r($intervals);

        $r = 0;

        $a0 = $intervals[0];
        $a1 = $intervals[1];
        $slow = 0;
        $fast = 1;

        while ($a1) {

            echo "{$a0[0]} {$a1[0]}".PHP_EOL;

            if ($a0[1]>$a1[0]) {

                $d0 = $a0[1] - $a0[0];
                $d1 = $a1[1] - $a1[0];

                $r++;
                if ($d0>$d1) {
                    unset($intervals[$slow++]);
                } else {
                    unset($intervals[$fast++]);
                    if ($fast == $cnt) break;
                }


            }

            {
                $r++;
                unset($intervals[$fast++]);
                if ($fast == $cnt) break;
                $a1 = $intervals[$fast];

            } elseif ($fast-$slow>1) {
                $slow++;
                while (!isset($intervals[$slow]) and $fast-$slow>=1) {
                    $slow++;
                }
                $a0 = $intervals[$slow];

                if ($slow == $fast) {
                    unset($intervals[$fast++]);
                    if ($fast == $cnt) break;
                    $a1 = $intervals[$fast];                        
                }

            } else {
                unset($intervals[$fast++]);
                if ($fast == $cnt) break;
                $a1 = $intervals[$fast];                
            }

        }

        return $r;

    }
}

$intervals = [[1,2],[2,3],[3,4],[1,3]];
//$intervals = [[1,2],[1,2],[1,2]];
//$intervals = [[1,2],[2,3]];
//$intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]];
$intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]];
$so = new Solution();
$r = $so->eraseOverlapIntervals($intervals);
print_r($r);