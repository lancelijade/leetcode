<?php

class Solution {

    function fill(&$grid, $x, $y) {
        
        for ($i=0; $i<count($grid); $i++) {
            //if ($i==$x or $i==$y) continue;
            if ($grid[$i][$y] == 1 and $grid[$x][$i] != 1) {
                $grid[$x][$i] = 1;
                $this->fill($grid, $x, $i);
            }
            if ($grid[$x][$i] == 1 and $grid[$i][$y] != 1) {
                $grid[$i][$y] = 1;
                $this->fill($grid, $i, $y);
            }
        }
        return true;
    }

    /**
     * @param String[][] $grid
     * @return Integer
     */
    function findCircleNum($isConnected) {
        
        $grid = $isConnected;
        $m = count($grid);
        //$this->show($grid, $m, $m);

        $n = $m;

        $q = [];
        $vt = [];

        $r = 0;

        for ($i=0; $i<$m; $i++) {
            for ($j=0; $j<$n; $j++) {

                if (!isset($vt[$i][$j]) and $grid[$i][$j]==1) {
                    $q[] = [$i, $j];
                    $r++;
                }

                while ($q) {

                    //print_r($q);
                    $c = array_shift($q);
                    $vt[$c[0]][$c[1]] = 1;
                    //$this->show($vt, $m, $n);

                    for ($x=0; $x<$m; $x++) {
                        if ($x==$i) continue;
                        if (!isset($vt[$x][$c[1]]) and $grid[$x][$c[1]]==1) {
                            $vt[$x][$c[1]] = 1; 
                            $q[] = [$x, $c[1]];
                        }
                    }

                    for ($y=0; $y<$n; $y++) {
                        if ($y==$j) continue;
                        if (!isset($vt[$c[0]][$y]) and $grid[$c[0]][$y]==1) {
                            $vt[$c[0]][$y] = 1; 
                            $q[] = [$c[0], $y];
                        }
                    }
                }                
            }
        }
        return $r;

    }

    function show($g, $m, $n) {
        for ($i=0; $i<$m; $i++) {
            for ($j=0; $j<$n; $j++) {
                echo $g[$i][$j] ?? 0;
            }
            echo PHP_EOL;
        }
        echo PHP_EOL;
    }
}


$isConnected = [
    [1,0,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,1,1]];    
$isConnected = [[1,1,0],[1,1,0],[0,0,1]];  
$isConnected = [[1,0,0],[0,1,0],[0,0,1]];  
$isConnected = [
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
    [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]];
$so = new Solution();
$r = $so->findCircleNum($isConnected);
print_r($r);