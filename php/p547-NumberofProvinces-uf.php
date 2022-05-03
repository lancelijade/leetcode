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
     * @param String[][] $grid
     * @return Integer
     */
    function findCircleNum($isConnected) {
        
        $size = count($isConnected);
        $provinces = new UnionFind($size);

        for ($i=0; $i<$size; $i++) {
            for ($j=$i+1; $j<$size; $j++) {
                if ($isConnected[$i][$j]) $provinces->union($i, $j);
            }
        }

//        print_r($provinces);
        return $provinces->getcount();
    }
}


$isConnected = [
    [1,0,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,1,1]];    
$isConnected = [[1,0,0],[0,1,0],[0,0,1]];  
$isConnected = [
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
    [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]];
$isConnected = [[1,1,0],[1,1,0],[0,0,1]];  
$isConnected = [
    [1,0,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,1,1]];
   
$so = new Solution();
$r = $so->findCircleNum($isConnected);
print_r($r);