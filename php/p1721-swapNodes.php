<?php

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

function makeList($ary) {
    $head = new ListNode($ary[0]);
    $h = $head;
    for ($i=1; $i<count($ary); $i++) {
        $h->next = new ListNode($ary[$i]);
        $h = $h->next;
    }
    return $head;
}


class Solution {

    /**
     * @param ListNode $head
     * @param Integer $k
     * @return ListNode
     */
    function swapNodes($head, $k) {

        $a = [];
        $h = $head;
        while ($h) {
            $a[] = $h;
            $h = $h->next;
        }

        $cnt = count($a);
        if ($cnt==1) return $head;

        if ($cnt==2) {
            $t = $head;
            $head = $a[1];
            $a[1] = $t;
            $a[1]->next = null;
            $head->next = $a[1];
            return $head;
        }

        if ($k==1 or $k==$cnt) {
            $t = $head;
            $head = $a[$cnt-1];
            $head->next = $t->next;
            $a[$cnt-2]->next = $t;
            $t->next = null;
            return $head;
        }
        
        $a[$k-2]->next = $a[$cnt-$k];
        $t = $a[$k-1];
        $a[$k-1] = $a[$cnt-$k];
        $a[$k-1]->next = $a[$k];
        
        $a[$cnt-$k] = $t;
        $a[$cnt-$k-1]->next = $a[$cnt-$k];
        $a[$cnt-$k]->next = $a[$cnt-$k+1];

        return $head;
        
    }
}

$head = [1,2,3,4,5]; $k = 2;
$head = [7,9,6,6,7,8,3,0,9,5]; $k = 5;
//$head = [1]; $k=1;
$head = [1,2]; $k=2;
$head = [80,46,66,35,64]; $k = 1;



$list = makeList($head);
$so = new Solution();
$r = $so->swapNodes($list, $k);
print_r($r);