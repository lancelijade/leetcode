<?php

class Solution {

    private $nums;
    private $ca = [1];

    function find($i) {

        //echo "$i".PHP_EOL;

        if ($i == 0) return 1;
        if (isset($this->ca[$i])) return $this->ca[$i];

        $max = 1;
        for ($j=0; $j<$i; $j++) {
            //echo "{$this->nums[$j]} {$this->nums[$i]}".PHP_EOL;
            if ($this->nums[$j] < $this->nums[$i]) {
                $r = $this->find($j);
                $max = max($max, $r+1);
            }
        }

        $this->ca[$i] = $max;

        //print_r($this->ca);
        return $max;
    }

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function lengthOfLIS2($nums) {
        
        $this->nums = $nums;
        
        for ($i=count($nums)-1; $i>=0; $i--) {
            $this->find($i);
        }
        return max($this->ca);
    }


    function lengthOfLIS($nums) {
        
        $dp = [1];

        for ($i=1; $i<count($nums); $i++) {
            $ma = 1;
            for ($j=0; $j<$i; $j++) {
                if ($nums[$j] < $nums[$i]) $ma = max($ma, $dp[$j]+1);
            }
            $dp[$i] = $ma;
        }

        return max($dp);
    }    
}

$nums = [1,4,0,3,6];
//$nums = [10,9,2,5,3,7,101,18];
//$nums = [0,1,0,3,2,3];
//$nums = [7,7,7,7,7,7,7];
$nums = [1,3,6,7,9,4,10,5,6];
$so = new Solution();
$r = $so->lengthOfLIS($nums);
print_r($r);