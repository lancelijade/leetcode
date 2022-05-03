<?php

class TreeNode {
    public $val = null;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

function buildTree($ary) {

    $q = [];
    $p = 0;
    $len = count($ary);

    $tn = new TreeNode($ary[$p++]);
    $q[] = $tn;
    $h = $tn;

    while ($node = array_shift($q)) {
        $tn = new TreeNode($ary[$p++]);
        if ($tn->val and $tn) {
            $node->left = $tn;
            $q[] = $tn;
        }
        if ($p>=$len) break;

        $tn = new TreeNode($ary[$p++]);
        if ($tn->val and $tn) {
            $node->right = $tn;
            $q[] = $tn;
        }
        if ($p>=$len) break;
    }

    return $h;
}


class Solution {

    /**
     * @param TreeNode $root1
     * @param TreeNode $root2
     * @return TreeNode
     */
    function mergeTrees($t1, $t2) {
        
        if (!$t1) return $t2;
        if (!$t2) return $t1;

        $t1->val += $t2->val;
        $t1->left = $this->mergeTrees($t1->left, $t2->left);
        $t1->right = $this->mergeTrees($t1->right, $t2->right);

        return $t1;
    }
}


$root1 = [1,3,2,5];
$root2 = [2,1,3,null,4,null,7];

$t1 = buildTree($root1);
$t2 = buildTree($root2);

$so = new Solution();
$r = $so->mergeTrees($t1, $t2);
var_dump($r);