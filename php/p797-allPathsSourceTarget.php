<?php

class Solution {

    /**
     * @param Integer[][] $graph
     * @return Integer[][]
     */
    function allPathsSourceTarget($graph) {

        $end = count($graph) - 1;
        $path = [];
        $seen = array_fill(0, $end+1, false);
        
        $stack = [];
        foreach ($graph[0] as $v) $stack[] = [0, $v];

        while ($stack) {

            //print_r($stack);
            $edge = array_pop($stack);

            $ev = end($edge);
            $seen[$ev] = true;

            if ($ev == $end) {
                $path[] = $edge;
                $seen[$ev] = false;
                continue;
            }

            foreach ($graph[$ev] as $nv) {
                if (!$seen[$nv]) $stack[] = array_merge($edge, [$nv]);
            }

            $seen[$ev] = false;
        }

        return $path;
    }
}

$graph = [[1,2],[3],[3],[]];
$graph = [[4,3,1],[3,2,4],[3],[4],[]];
$graph = [[1,2,3],[2],[3],[]];

$so = new Solution();
$r = $so->allPathsSourceTarget($graph);
print_r($r);