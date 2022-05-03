<?php


class Solution {

    public $graph;
    //public $visited = [];
    public $cnt;
    public $ret = [];
    public $retlen = PHP_INT_MAX;
    public $tt = 0;
    public $finish = false;
    
    function dfs($i, $from, $visited, $path, $repeatNumAllowed) {

        $visited[$i] = isset($visited[$i]) ? $visited[$i] + 1 : 1;
        $pa = "$from-$i";
        $path[$pa] = 1;
        //echo "$from -> $i ";
        //foreach ($visited as $k => $num) echo "$k($num) ";
        //echo count(array_keys($visited))." ".$this->retlen." ".$this->cnt;
        //echo PHP_EOL;
        //if ($this->tt++>1000) return;

        if (count(array_keys($visited)) == $this->cnt) {
            //print_r($visited);
            $this->ret[] = $visited;
            $len = array_sum($visited) - 1;
            if ($len < $this->retlen) $this->retlen = $len;
            if ($this->retlen == $this->cnt) $this->finish = true;
            return true;
        }
        
        foreach ($this->graph[$i] as $j) {
            $pa = "$i-$j";;
            //$pathcnt = array_count_values($path);
            if (!isset($path[$pa])) {
                if (!isset($visited[$j]) or $visited[$j]+1<=$repeatNumAllowed) {
                    $this->dfs($j, $i, $visited, $path, $repeatNumAllowed);
                    //var_dump($this->finish);
                    if ($this->retlen == $this->cnt-1) return true;
                }
            }
        }
    }

    /**
     * @param Integer[][] $graph
     * @return Integer
     */
    function shortestPathLength($graph) {
        $this->graph = $graph;
        $this->cnt = count($graph);
        $repeat = 1;

        $graphcnt = [];
        foreach ($graph as $k => $g) $graphcnt[$k] = count($g);
        asort($graphcnt);
        //print_r($graphcnt);
        //exit;

        while ($this->retlen == PHP_INT_MAX) {
            foreach ($graphcnt as $i => $v) {
                $r = $this->dfs($i, -1, [], [], $repeat);
                if ($this->retlen == $this->cnt - 1) return $this->retlen;
            }
            $repeat++;
        }
        return $this->retlen;
    }
}


$graph = [[1,2,3],[0],[0],[0]];
$graph = [[1],[0,2,4],[1,3,4],[2],[1,2]];
//$graph = [[]];
//$graph = [[1,4],[0,3,4,7,9],[6,10],[1,10],[1,0],[6],[7,2,5],[6,1,8],[7],[1],[2,3]];
$graph = [[1,2,3,4,5,6,7,8,9],[0,2,3,4,5,6,7,8,9],[0,1,3,4,5,6,7,8,9],[0,1,2,4,5,6,7,8,9],[0,1,2,3,5,6,7,8,9],[0,1,2,3,4,6,7,8,9],[0,1,2,3,4,5,7,8,9],[0,1,2,3,4,5,6,8,9],[0,1,2,3,4,5,6,7,9,10],[0,1,2,3,4,5,6,7,8,11],[8],[9]];


$so = new Solution();
$r = $so->shortestPathLength($graph);
print_r($r);


