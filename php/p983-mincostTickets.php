<?php


class Solution {

    private $costs;
    private $day;
    private $maxday;
    private $cache = [];

    function dp($i) {

        //echo $i.PHP_EOL;

        if ($i>$this->maxday) return 0;
        if (isset($this->cache[$i])) return $this->cache[$i];

        $r = 0;
        if (isset($this->days[$i])) {
            $r = min( 
                $this->costs[0]+$this->dp($i+1),
                $this->costs[1]+$this->dp($i+7),
                $this->costs[2]+$this->dp($i+30),
            );
        } else {
            $r = $this->dp($i+1);
        }

        $this->cache[$i] = $r;
        return $r;
    }


    /**
     * @param Integer[] $days
     * @param Integer[] $costs
     * @return Integer
     */
    function mincostTickets($days, $costs) {
        
        $this->costs = $costs;
        $this->days = array_flip($days);
        $this->maxday = max($days);

        return $this->dp(1);
    }
}


$days = [1,4,6,7,8,20]; $costs = [2,7,15];
//$days = [1,2,3,4,5,6,7,8,9,10,30,31]; $costs = [2,7,15];
$so = new Solution();
$r = $so->mincostTickets($days, $costs);
print_r($r);