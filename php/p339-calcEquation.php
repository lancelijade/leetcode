<?php

class UnionFind {       // union by rank, find path compression

    private $weight = [];

    public function __construct() {
    }

    public function find($x) {

        if (!isset($this->weight[$x])) $this->weight[$x] = [$x, 1];
        list($group_id, $node_weight) = $this->weight[$x];

        if ($group_id != $x) {
            list($ngid, $group_weight) = $this->find($group_id);
            $this->weight[$x] = [$ngid, $node_weight*$group_weight];
        }

        return $this->weight[$x];
    }

    public function union($x, $y, $val) {

        list($x_gid, $x_weight) = $this->find($x);
        list($y_gid, $y_weight) = $this->find($y);

        if ($x_gid != $y_gid) {
            $this->weight[$x_gid] = [$y_gid, $y_weight * $val / $x_weight];
        }
    }

    public function connected($x, $y) {
        return $this->find($x) == $this->find($y);
    }

    public function in($x) {
        return isset($this->weight[$x]);
    }

}

class Solution {

    /**
     * @param String[][] $equations
     * @param Float[] $values
     * @param String[][] $queries
     * @return Float[]
     */
    function calcEquation($equations, $values, $queries) {
        
        $uf = new unionFind();

        foreach ($equations as $k => $e) {
            $uf->union($e[0], $e[1], $values[$k]);
        }

        print_r($uf);

        $r = [];
        foreach ($queries as $query) {
            if (!$uf->in($query[0]) or !$uf->in($query[1])) {
                $r[] = -1;

            } else {

                list($x_gid, $x_weight) = $uf->find($query[0]);
                list($y_gid, $y_weight) = $uf->find($query[1]);
                echo "$x_gid $x_weight $y_gid $y_weight".PHP_EOL;
                if ($x_gid != $y_gid) {
                    $r[] = -1;
                } else {
                    $r[] = $x_weight / $y_weight;
                }
            }
        }

        return $r;
    }
}

$equations = [["a","b"],["b","c"]]; $values = [2.0,3.0]; $queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]];
//$equations = [["a","b"],["b","c"],["bc","cd"]]; $values = [1.5,2.5,5.0]; $queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]];
//$equations = [["a","b"]]; $values = [0.5]; $queries = [["a","b"],["b","a"],["a","c"],["x","y"]];
//$equations = [["a","b"],["e","f"],["b","e"]]; $values = [3.4,1.4,2.3]; $queries = [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]];
$equations = [["a","c"],["b","e"],["c","d"],["e","d"]]; $values = [2.0,3.0,0.5,5.0]; $queries = [["a","b"]];
$equations = [["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]]; $values = [3.0,0.5,3.4,5.6]; $queries = [["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]];


$so = new Solution();
$r = $so->calcEquation($equations, $values, $queries);
print_r($r);