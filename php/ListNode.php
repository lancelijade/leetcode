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

