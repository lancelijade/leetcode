<?php

/* The isBadVersion API is defined in the parent class VersionControl.
      public function isBadVersion($version){} */
$BAD = 0;

class Solution {

    function isBadVersion($version) {
        global $BAD;
        if ($version>=$BAD) return true;
        return false;
    }

    /**
     * @param Integer $n
     * @return Integer
     */
    function firstBadVersion($n) {
        
        $left = 0;
        $right = $n;
        $r = -1;
        while ($left < $right) {
            $mid = floor(($left+$right)/2);
            //echo "$left $right $mid".PHP_EOL;
            if ($this->isBadVersion($mid)) {
                $right = $mid - 1;
                $r = $mid;
            } else {
                $left = $mid + 1;
            }
        }
        if ($this->isBadVersion($left)) {
            return $left;
        } elseif ($this->isBadVersion($right)) {
            return $right;
        } else {
            return $r;
        }
    }
}

$n = 4;
$bad = 2;

$BAD = $bad;
$so = new Solution();
$r = $so->firstBadVersion($n);
print_r($r);