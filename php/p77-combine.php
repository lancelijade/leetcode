<?php

class Solution {

    private $n;
    private $k;
    private $r = [];

    function loop($ary, $from, $lvl) {

        for ($i=$from+1; $i<=$this->n; $i++) {

            if ($lvl<$this->k) {
                $this->loop(array_merge($ary, [$i]), $i, $lvl+1);
                continue;
            }

            $this->r[] = array_merge($ary, [$i]);

        }
    }

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer[][]
     */
    function combine2($n, $k) {
        
        $this->n = $n;
        $this->k = $k;

        $this->loop([], 0, 1);

        return $this->r;
    }


    function combine($n, $k) {
        
        $nums = [];
        for ($i=1; $i<=$k; $i++) $nums[] = $i;
        $nums[] = $n+1;
        print_r($nums);
        
        $j = 0;
        $r = [];
        while ($j<$k) {
            $r[] = array_slice($nums, 0, $k);
            print_r($nums);

            $j = 0;
            while (($j<$k) and ($nums[$j+1] == $nums[$j]+1)) {
                echo "j=$j k=$k nj+1={$nums[$j+1]} nj={$nums[$j]}".PHP_EOL;
                $nums[$j] = $j + 1;
                $j++;
                echo "j=$j k=$k nj={$nums[$j]}".PHP_EOL;
            }
            $nums[$j] += 1;
            echo "nj={$nums[$j]}".PHP_EOL;
        }
        return $r;
    }
}

$n = 4; 
$k = 2;
$so = new Solution();
$r = $so->combine($n, $k);
print_r($r);