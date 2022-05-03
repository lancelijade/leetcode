<?php

class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $wells
     * @param Integer[][] $pipes
     * @return Integer
     */
    function minCostToSupplyWater($n, $wells, $pipes) {
        
        // min heap to maintain the order of edges to be visited.
        $edgesHeap = new SplMinHeap();

        // representation of graph in adjacency list
        $graph = array_fill(0, $n+1, []);

        // add a virtual vertex indexed with 0,
        //   then add an edge to each of the house weighted by the cost        
        for ($i=0; $i<count($wells); $i++) {
            $virtualEdge = [$wells[$i], $i+1];
            $graph[0][] = $virtualEdge;
            $edgesHeap->insert($virtualEdge);
        }

        // add the bidirectional edges to the graph
        for ($i=0; $i<count($pipes); $i++) {
            list($house1, $house2, $cost) = $pipes[$i];
            $graph[$house1][] = [$cost, $house2];
            $graph[$house2][] = [$cost, $house1];
        }

        // kick off the exploration from the virtual vertex 0
        $mstSet = [0];

        $totalCost = 0;
        while (count($mstSet) < $n+1) {
            list($cost, $nextHouse) = $edgesHeap->extract();
            if (in_array($nextHouse, $mstSet)) continue;

            // adding the new vertex into the set
            $mstSet[] = $nextHouse;
            $totalCost += $cost;

            // expanding the candidates of edge to choose from in the next round
            foreach ($graph[$nextHouse] as $neighborEdge) {
                if (!in_array($neighborEdge[1], $mstSet)) $edgesHeap->insert($neighborEdge);
            }
        }

        return $totalCost;
    }
}

$n = 3; $wells = [1,2,2]; $pipes = [[1,2,1],[2,3,1]];
$n = 2; $wells = [1,1]; $pipes = [[1,2,1],[1,2,2]];

$so = new Solution();
$r = $so->minCostToSupplyWater($n, $wells, $pipes);
print_r($r);