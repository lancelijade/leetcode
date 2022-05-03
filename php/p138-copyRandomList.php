<?php

class Node {
    public $val = null;
    public $next = null;
    public $random = null;
    function __construct($val = 0) {
        $this->val = $val;
        $this->next = null;
        $this->random = null;
    }
}


function buildList($head) {

    $h = new Node(0);
    $t = $h;
    $ta = [];
    foreach ($head as $na) {
        $node = new Node($na[0]);
        $t->next = $node;
        $ta[] = $node;
        $t = $t->next;
    }

    $t = $h->next;
    foreach ($head as $na) {
        if ($na[1]!==null) $t->random = $ta[$na[1]];
        $t = $t->next;
    }

    return $h->next;
}


class Solution {
    /**
     * @param Node $head
     * @return Node
     */
    function copyRandomList($head) {
        
        $h = $head;
        while ($h) {
            //echo $h->val.' '.$this->hash($h).PHP_EOL;
            $t = new Node($h->val);
            $t->next = $h->next;
            $h->next = $t;
            $h = $h->next->next;
            //echo $t->val.' '.$this->hash($t).PHP_EOL;
        }
        //return $head;
        
        $h = $head;
        $n = $head->next;
        while ($h) {
            if ($h->random) $n->random = $h->random->next;
            $h = $h->next->next;
            if ($h) $n = $h->next;
        }
        //return $head;
        
        $n = $head->next;
        while ($n) {
            if ($n->next) $n->next = $n->next->next;
            $n = $n->next;
        }

        return $head->next;
    }
 
}


$head = [[7,null],[13,0],[11,4],[10,2],[1,0]];
$head = [[1,0]];

$list = buildList($head);
//print_r($list);

$so = new Solution();
$r = $so->copyRandomList($list);
print_r($r);

$i = 0;
while ($r) {
    //print_r($r);
    echo "$i:{$r->val} ".PHP_EOL;
    echo "$i:{$r->random->val} ".spl_object_id($r).PHP_EOL;
    $r = $r->next;
    $i++;
}