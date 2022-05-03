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
     * @param Integer[][] $logs
     * @param Integer $n
     * @return Integer
     */
    function earliestAcq($logs, $n) {
        
        sort($logs);
        $uf = new UnionFind($n);
        foreach ($logs as $log) {
            $uf->union($log[1], $log[2]);
            if ($uf->getcount()==1) return $log[0];
        }
        return -1;
    }
}

$logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]; $n = 6;
$logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]]; $n = 4;
$logs = [[9,3,0],[0,2,1],[8,0,1],[1,3,2],[2,2,0],[3,3,1]]; $n = 4;


$so = new Solution();
$r = $so->earliestAcq($logs, $n);
print_r($r);