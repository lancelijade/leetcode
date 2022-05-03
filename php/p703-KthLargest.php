<?php

class KthLargest {

    private $q;
    private $k;

    /**
     * @param Integer $k
     * @param Integer[] $nums
     */
    function __construct($k, $nums) {

        $this->q = new SplMinHeap();
        $this->k = $k;
        
        foreach ($nums as $num) $this->q->insert($num);

        $cnt = count($nums);
        for ($i=1; $i<=$cnt-$k-1; $i++) $this->q->extract();
    }
  
    /**
     * @param Integer $val
     * @return Integer
     */
    function add($val) {
        
        if ($this->q->count() < $this->k) {
            $this->q->insert($val);
            return $this->q->top();
        }

        $this->q->insert($val);
        $this->q->extract();
        return $this->q->top();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * $obj = KthLargest($k, $nums);
 * $ret_1 = $obj->add($val);
 */

$input = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]];
$input = [[1,[]],[-3],[-2],[-4],[0],[4]];
$input = [[2,[0]],[-1],[1],[-2],[-4],[3]];
$input = [[3,[5,-1]],[2],[1],[-1],[3],[4]];


$k = $input[0][0];
$nums = $input[0][1];
$obj = new KthLargest($k, $nums);

print_r($obj);

for ($i=1; $i<count($input); $i++) {
    $r = $obj->add($input[$i][0]);
    echo $r.' ';
    //print_r($obj);
}