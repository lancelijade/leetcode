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


class UnionFind2 {       // quickUnion

    private $root = [];
    private $size = 0;

    public function __construct($size) {
        $this->root = range(0, $size-1);
        $this->size = $size;
    }

    public function find($x) {
        while ($x != $this->root[$x]) $x = $this->root[$x];
        return $x;
    }

    public function union($x, $y) {
        $rootX = $this->find($x);
        $rootY = $this->find($y);
        if ($rootX != $rootY) {
            $this->root[$rootY] = $rootX;
        }
    }

    public function connected($x, $y) {
        return $this->find($x) == $this->find ($y);
    }
}

class UnionFind1 {       // quick find

    private $root = [];
    private $size = 0;

    public function __construct($size) {
        $this->root = range(0, $size-1);
        $this->size = $size;
    }

    public function find($x) {
        return $this->root[$x];
    }

    public function union($x, $y) {
        $rootX = $this->find($x);
        $rootY = $this->find($y);
        if ($rootX != $rootY) {
            for ($i=0; $i<$this->size; $i++) {
                if ($this->root[$i] == $rootY) $this->root[$i] = $rootX;
            }
        }
    }

    public function connected($x, $y) {
        return $this->find($x) == $this->find ($y);
    }
}



$uf = new UnionFind(10);

$uf->union(1,2);
$uf->union(2,5);
$uf->union(5,6);
$uf->union(6,7);
$uf->union(3,8);
$uf->union(8,9);
print_r($uf);

var_dump($uf->connected(1,5));
var_dump($uf->connected(5,7));
var_dump($uf->connected(4,9));
$uf->union(9,4);
var_dump($uf->connected(4,9));
