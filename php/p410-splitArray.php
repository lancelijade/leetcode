<?php

class Solution {

    private $nums;
    private $cnt;
    private $cache = [];
    private $prefixSum = [];


    function dp($i, $mleft) {

        //echo "i=$i mleft=$mleft".PHP_EOL;

        if ($mleft==1) return $this->prefixSum[$this->cnt-1]-$this->prefixSum[$i-1];
        if (isset($this->cache[$i][$mleft])) return $this->cache[$i][$mleft];

        $ls = 0;
        $r = PHP_INT_MAX;
        for ($j=$i+1; $j<$this->cnt; $j++) {

            $ls += $this->nums[$j-1];
            $rs = $this->dp($j, $mleft-1);
            //echo "j=$j ls=$ls rs=$rs".PHP_EOL;

            $r = min($r, max($ls, $rs));

            if ($ls>$r) break;
        }

        $this->cache[$i][$mleft] = $r;

        return $r;
    }


    /**
     * @param Integer[] $nums
     * @param Integer $m
     * @return Integer
     */
    function splitArray2($nums, $m) {
        
        $cnt = count($nums);

        if ($m==$cnt) return max($nums);

        $this->nums = $nums;
        $this->cnt = $cnt;
        
        $this->prefixSum[-1] = 0;
        $this->prefixSum[0] = $nums[0];
        for ($i=0; $i<$cnt; $i++) {
            $this->prefixSum[$i] = $this->prefixSum[$i-1] + $nums[$i];
        }

        return $this->dp(0, $m);
    }

    // can be split into $m subArrays with max sum $n
    function canSplit($n, $m) {

        //echo "mid=$n m=$m".PHP_EOL;

        $p = 1;
        $s = 0;
        for ($i=0; $i<$this->cnt; $i++) {
            //echo "s=$s p=$p i=$i".PHP_EOL;
            if ($s + $this->nums[$i]<=$n) {
                $s += $this->nums[$i];
            } else {
                $s = $this->nums[$i];
                $p++;
                if ($p>$m) return false;
            }
        }
        return true;
    }


    function splitArray($nums, $m) {

        $this->nums = $nums;
        $this->cnt = count($nums);

        $sum = array_sum($nums);
        $max = max($nums);

        $left = $max;
        $right = $sum;
        $r = 0;
        while ($left <= $right) {
            $mid = floor(($left+$right)/2);
            if ($this->canSplit($mid, $m)) {
                $r = $mid;
                $right = $mid-1;
            } else {
                $left = $mid + 1;
            }
        }
        return $r;
    }

}

$nums = [7,2,5,10,8]; $m = 2;
$nums = [1,2,3,4,5]; $m = 2;
$so = new Solution();
$r = $so->splitArray($nums, $m);
print_r($r);