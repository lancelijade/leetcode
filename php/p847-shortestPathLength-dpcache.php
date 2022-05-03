<?php


class Solution {

    private $graph;
    private $endingMask;
    private $cache = [];
    
    function dp($node, $mask) {

        //echo "$node ".decbin($mask).PHP_EOL;
        if (isset($this->cache[$node][$mask])) {
            //echo $this->cache[$node][$mask].PHP_EOL;
            return $this->cache[$node][$mask];
        }

        if (($mask & ($mask-1)) == 0) {
            return 0;
        }

        $this->cache[$node][$mask] = PHP_INT_MAX;
        foreach ($this->graph[$node] as $neighbor) {
            if (($mask & (1 << $neighbor)) != 0) {
                $alreadyVisited = $this->dp($neighbor, $mask);
                $notVisited = $this->dp($neighbor, $mask ^ (1 << $node));
                $better = min($alreadyVisited, $notVisited);
                $this->cache[$node][$mask] = min($this->cache[$node][$mask], $better+1);
            }
        }

        return $this->cache[$node][$mask];
    }

    /**
     * @param Integer[][] $graph
     * @return Integer
     */
    function shortestPathLength($graph) {

        $this->graph = $graph;
        $n = count($graph);
        $this->endingMask = (1 << $n) - 1;

        $best = PHP_INT_MAX;

        for ($node=0; $node<$n; $node++) {
            $best = min($best, $this->dp($node, $this->endingMask));
            //print_r($this->cache);
        }
        return $best;
    }
}


$graph = [[1,2,3],[0],[0],[0]];
//$graph = [[1],[0,2,4],[1,3,4],[2],[1,2]];
//$graph = [[]];
//$graph = [[1,4],[0,3,4,7,9],[6,10],[1,10],[1,0],[6],[7,2,5],[6,1,8],[7],[1],[2,3]];
$graph = [[1,2,3,4,5,6,7,8,9],[0,2,3,4,5,6,7,8,9],[0,1,3,4,5,6,7,8,9],[0,1,2,4,5,6,7,8,9],[0,1,2,3,5,6,7,8,9],[0,1,2,3,4,6,7,8,9],[0,1,2,3,4,5,7,8,9],[0,1,2,3,4,5,6,8,9],[0,1,2,3,4,5,6,7,9,10],[0,1,2,3,4,5,6,7,8,11],[8],[9]];


$so = new Solution();
$r = $so->shortestPathLength($graph);
print_r($r);


