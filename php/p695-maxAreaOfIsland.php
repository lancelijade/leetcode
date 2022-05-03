<?php

class Solution {

    private $grid;
    private $m;
    private $n;
    private $acc = [];


    function dfs($i, $j) {

        //echo "$i $j".PHP_EOL;

        if ($i>=$this->m or $i<0) return 0;
        if ($j>=$this->n or $j<0) return 0;
        if (isset($this->acc[$i][$j])) return 0;
        if ($this->grid[$i][$j] == 0) return 0;

        $this->acc[$i][$j] = 1;

        $r = 1 + $this->dfs($i+1,$j)
               + $this->dfs($i,$j+1)
               + $this->dfs($i-1,$j)
               + $this->dfs($i,$j-1);

        //echo "$r".PHP_EOL;
        return $r;
    }

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxAreaOfIsland($grid) {
        
        $this->grid = $grid;
        $this->m = count($grid);
        $this->n = count($grid[0]);

        $max = 0;

        for ($i=0; $i<$this->m; $i++) {
            for ($j=0; $j<$this->n; $j++) {
                $max = max($max, $this->dfs($i, $j));
            }
        }

        return $max;
    }
}

$grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]];
//$grid = [[0,0,0,0,0,0,0,0]];
$grid = [[1,1,0,1,1], [1,0,0,0,0], [0,0,0,0,1], [1,1,0,1,1]];
$so = new Solution();
$r = $so->maxAreaOfIsland($grid);
var_dump($r);