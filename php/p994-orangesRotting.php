<?php

class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function orangesRotting($grid) {
        
        $m = count($grid);
        $n = count($grid[0]);
        $q = [];
        $r = [];

        for ($i=0; $i<$m; $i++) {
            for ($j=0; $j<$n; $j++) {
                if ($grid[$i][$j] == 2) {
                    $r[$i][$j] = 0;
                    $q[] = [$i, $j];
                } elseif ($grid[$i][$j] == 1) {
                    $r[$i][$j] = PHP_INT_MAX;
                } else {
                    $r[$i][$j] = PHP_INT_MIN;
                }
            }
        }

        while ($q) {
            list($x, $y) = array_shift($q);
            //echo "$x $y".PHP_EOL;
            $dirs = [[-1,0],[0,-1],[1,0],[0,1]];
            foreach ($dirs as $dir) {
                $x1 = $x + $dir[0];
                $y1 = $y + $dir[1];
                if ($x1>=0 and $x1<$m and $y1>=0 and $y1<$n) {
                    if ($r[$x1][$y1] > $r[$x][$y]+1) {
                        $r[$x1][$y1] = $r[$x][$y]+1;
                        $q[] = [$x1, $y1];
                    }
                }
            }
        }

        $max = 0;
        for ($i=0; $i<$m; $i++) {
            for ($j=0; $j<$n; $j++) {
                $max = max($max, $r[$i][$j]);
                if ($max == PHP_INT_MAX) return -1;
            }
        }

        //print_r($r);
        return $max;
    }
}

$grid = [[0,2]];
$so = new Solution();
$r = $so->orangesRotting($grid);
print_r($r);