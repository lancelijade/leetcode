<?php

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */
class Solution {

    function c($root, $level) {
        //echo $root->val." $level\n";
        if (!$root or $root->val===null) return $level-1;
        $n1 = $this->c($root->left, $level+1);
        $n2 = $this->c($root->right, $level+1);
        return ($n1>$n2)? $n1:$n2;
    }

    /**
     * @param TreeNode $root
     * @return Integer
     */
    function maxDepth($root) {
        return $this->c($root, 1);
    }
}

$root = [3,9,20,null,null,15,7];


$so = new Solution();
$r = $so->maxDepth($root);
print_r($r);