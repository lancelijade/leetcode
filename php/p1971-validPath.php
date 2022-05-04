<?php

class Solution {

    private $visited = [];
    private $stack = [];

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer $source
     * @param Integer $destination
     * @return Boolean
     */
    function validPath($n, &$edges, $source, $destination) {
        
        if ($n == 1 and $source == 0 and $destination == 0) return true;
        if (isset($this->visited[$source])) return false;

        $this->visited[$source] = 1;
        foreach ($edges as $e) {
            if ($e[0] == $source) {
                if ($e[1] == $destination) return true;
                $this->stack[] = $e[1];
            } elseif ($e[1] == $source) {
                if ($e[0] == $destination) return true;
                $this->stack[] = $e[0];
            }
        }

        while ($this->stack) {
            $v = array_pop($this->stack);
            $r = $this->validPath($n, $edges, $v, $destination);
            if ($r) return true;
        }

        return false;
    }


    function validPath_adjlist($n, $edges, $source, $destination) {

        $adjList = [];
        foreach ($edges as $e) {
            $adjList[$e[0]][] = $e[1];
            $adjList[$e[1]][] = $e[0];
        }

        $stack = [$source];
        $visited = array_fill(0, $n, false);

        while ($stack) {

            $v = array_pop($stack);

            if ($v == $destination) return true;

            if ($visited[$v]) continue;
            $visited[$v] = true;

            foreach ($adjList[$v] as $nv) {
                if ($nv == $destination) return true;
                $stack[] = $nv;
            }
        }

        return false;
    }
}

$n = 3; $edges = [[0,1],[1,2],[2,0]]; $source = 0; $destination = 2;
//$n = 6; $edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]; $source = 0; $destination = 5;
//$n = 1; $edges = []; $source = 0; $destination = 0;
$n = 10; $edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]; $source = 5; $destination = 9;
$n = 100000; $edges =
$source = 59612;
$destination = 79883;

$so = new Solution();
$r = $so->validPath_adjlist($n, $edges, $source, $destination);
print_r($r);