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

    public function getparts() {
        $parts = [];
        foreach ($this->root as $k => $v) {
            $parts[$v][$k] = $v;
        }
        return $parts;
    }
}

class Solution {

    /**
     * @param String $s
     * @param Integer[][] $pairs
     * @return String
     */
    function smallestStringWithSwaps($s, $pairs) {
        
        $len = strlen($s);
        $sa = str_split($s);

        $uf = new UnionFind($len);
        foreach ($pairs as $pair) $uf->union($pair[0], $pair[1]);

        if ($uf->getcount()==1) {   // one region only, return sorted directly
            sort($sa);
            return join('', $sa);
        }

        for ($i=0; $i<$len; $i++) $uf->find($i);    // path compression

        $parts = $uf->getparts();
        //print_r($parts);

        $r = [];
        foreach ($parts as $n => &$part) {
            foreach ($part as $k => $v) $parts[$n][$k] = $s[$k];
            $keys = array_keys($part);
            sort($part);
            foreach ($part as $i => $v) {
                $r[$keys[$i]] = $v;
            }
        }
        ksort($r);
        return join('', $r);
    }
}

$s = "dcab"; $pairs = [[0,3],[1,2]];
//$s = "dcab"; $pairs = [[0,3],[1,2],[0,2]];

$so = new Solution();
$r = $so->smallestStringWithSwaps($s, $pairs);
print_r($r);