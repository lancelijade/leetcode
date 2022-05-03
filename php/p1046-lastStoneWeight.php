<?php

class Solution {

    /**
     * @param Integer[] $stones
     * @return Integer
     */
    function lastStoneWeight($stones) {
        
        $h = new SplMaxHeap();
        foreach ($stones as $stone) $h->insert($stone);

        while ($h->count()>1) {
            
            $a = $h->extract();
            $b = $h->extract();

            if ($a-$b!=0) $h->insert(abs($a-$b));
        }

        return $h->current() ?? 0;
    }
}

$stones = [2,7,4,1,8,1];
$stones = [1];
$stones = [2,2];
$so = new Solution();
$r = $so->lastStoneWeight($stones);
print_r($r);