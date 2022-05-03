<?php

class UnionFind {       // union by rank, find path compression

    private $root = [];
    private $rank = [];
    private $size;
    private $count;

    public function __construct($size) {
        $this->root = range(0, $size-1);
        $this->rank = array_fill(0, $size, 1);
        $this->size = $size;
        $this->count = $size;
    }

    public function find($x) {
        if ($x == $this->root[$x]) return $x;
        return $this->root[$x] = $this->find($this->root[$x]);
    }

    public function union($x, $y) {
        $rootX = $this->find($x);
        $rootY = $this->find($y);
        if ($rootX != $rootY) {
            if ($this->rank[$rootX] > $this->rank[$rootY]) {
                $this->root[$rootY] = $rootX;
            } elseif ($this->rank[$rootX] < $this->rank[$rootY]) {
                $this->root[$rootX] = $rootY;
            } else {
                $this->root[$rootY] = $rootX;
                $this->rank[$rootX]++;
            }
            $this->count--;
        }
    }

    public function connected($x, $y) {
        return $this->find($x) == $this->find ($y);
    }

    public function getcount() {
        return $this->count;
    }    
}

class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Boolean
     */
    function validTree($n, $edges) {
        
        $uf = new UnionFind($n);
        foreach ($edges as $edge) {
            if (!$uf->connected($edge[0], $edge[1])) $uf->union($edge[0], $edge[1]);
            else return false;
        }
        return $uf->getcount()==1;
    }
}

$n = 5; $edges = [[0,1],[1,2],[2,3],[1,3],[1,4]];

$so = new Solution();
$r = $so->validTree($n, $edges);
print_r($r);