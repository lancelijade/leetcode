<?php

/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
class Solution {

    /**
     * @param ListNode $head
     * @param Integer $n
     * @return ListNode
     */
    function removeNthFromEnd($head, $n) {
        $cnt = 1;
        $hn = $head;
        while ($hn->next) {
            $hn = $hn->next;
            $cnt++;
        }
        
        if ($cnt==1) return null;

        $target = $cnt - $n;
        if ($target==0) return $head->next;
        
        //echo "cnt=$cnt target=$target\n";
        $cn = 1;
        $hn = $head;
        while (1) {
            //echo $hn->val."==\n";
            //print_r($head);
            if ($cn==$target) {
                //echo $hn->next->val."\n";
                //echo $hn->next->next->val."\n";
                $hn->next = $hn->next->next;
                //print_r($head);
                break;
            } else {
                $hn = $hn->next;
                $cn++;
            }
        }
        
        return $head;
    }
}

$head = [1,2,3,4,5]; 
$n = 2;
$so = new Solution();
$r = $so->removeNthFromEnd($head);
print_r($r);