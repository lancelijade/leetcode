<?php

class Solution {

    private $d;
    private $jd;
    private $len;
    private $difficultyRecord = [];
    private $cache = [];

    function dp($i, $day) {

        echo "i=$i day=$day".PHP_EOL;

        if ($day == $this->d) {
            return $this->difficultyRecord[$i];
        }

        if (isset($this->cache[$i][$day])) return $this->cache[$i][$day];

        $best = PHP_INT_MAX;
        $hardest = 0;

        for ($j=$i; $j<$this->len-($this->d - $day); $j++) {
            $hardest = max($hardest, $this->jd[$j]);
            $best = min($best, $hardest + $this->dp($j+1, $day+1));
        }

        $this->cache[$i][$day] = $best;
        return $best;
    }


    /**
     * @param Integer[] $jobDifficulty
     * @param Integer $d
     * @return Integer
     */
    function minDifficulty($jobDifficulty, $d) {
        
        $len = count($jobDifficulty);
        if ($len < $d) return -1;

        $this->d = $d;
        $this->jd = $jobDifficulty;
        $this->len = $len;

        $this->difficultyRecord[$len-1] = $jobDifficulty[$len-1];
        for ($i=$len-2; $i>=0; $i--) {
            $this->difficultyRecord[$i] = max($jobDifficulty[$i], $this->difficultyRecord[$i+1]);
        }

        
        return $this->dp(0, 1);
    }
}

$jobDifficulty = [6,5,10,3,2,1];
$d = 3;
$so = new Solution();
$r = $so->minDifficulty($jobDifficulty, $d);
print_r($r);