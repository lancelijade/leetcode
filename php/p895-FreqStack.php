<?php

class FreqStack {
    
    private $stack;
    private $seq = 0.00001;
    private $freq = [];
    
    /**
     */
    function __construct() {
        $this->stack = new SplPriorityQueue();
    }
  
    /**
     * @param Integer $val
     * @return NULL
     */
    function push($val) {
        $this->freq[$val] = ($this->freq[$val] ?? 0) + 1 ;
        $this->stack->insert($val, $this->freq[$val] + $this->seq);
        $this->seq += 0.00001;
    }
  
    function isEmpty() {
        return $this->stack->isEmpty();
    }

    /**
     * @return Integer
     */
    function pop() {
        $val = $this->stack->extract();
        $this->freq[$val]--;
        return $val;
    }
}

$in = [[8],[2],[2],[2],[8],[8],[9],[9],[8],[8],[2],[2],[8],[2],[9],[9],[9],[2],[9],[8],[8],[2],[2],[2],[8],[2],[2],[8],[9],[8],[8],[8],[9],
[2],[9],[2],[9],[2],[9],[9],[8],[9],[2],[9],[2],[8],[8],[9],[9],[2]];


$obj = new FreqStack();

foreach ($in as $i) {
    $obj->push($i[0]);
}
print_r($obj);

$cnt = 0;
while (1) {
    if ($cnt++==12) print_r($obj);
    if (!$obj->isEmpty()) {
        $ret_2 = $obj->pop();
        echo $ret_2.' ';
    }
    else break;
}
