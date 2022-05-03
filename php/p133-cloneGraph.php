<?php

class Node {
    public $val = null;
    public $neighbors = null;
    function __construct($val = 0) {
        $this->val = $val;
        $this->neighbors = array();
    }
}

// list = [[2,4],[1,3],[2,4],[1,3]]
function createGraph($list) {

    $nodes = [];
    for ($i=0; $i<count($list); $i++) $nodes[$i+1] = new Node($i+1);

    foreach ($list as $i => $val) {
        $j = $i + 1;
        foreach ($val as $v) {
            $nodes[$j]->neighbors[] = $nodes[$v];
        }
    }

    return isset($nodes[1]) ? $nodes[1] : null;
}


class Solution {

    public $nodes;

    /**
     * @param Node $node
     * @return Node
     */
    function cloneGraph($node) {
        
        if (!$node) return null;

        if (!isset($this->nodes[$node->val])) {
            $nn = new Node($node->val);
            $this->nodes[$node->val] = $nn;
         
            foreach ($node->neighbors as $nb) {
                $nbn = $this->cloneGraph($nb);
                $nn->neighbors[] = $nbn;
            }            
        }
        return $this->nodes[$node->val];
    }
}

$adjList = [[2,4],[1,3],[2,4],[1,3]];
//$adjList = [];
$node = createGraph($adjList);
//print_r($node);

$so = new Solution();
$r = $so->cloneGraph($node);
print_r($r);