<?php

class Solution {

    function existInFirst(&$nums, $start, $ele) {
        return $nums[$start] <= $ele;
    }

    function isBinarySearchHelpful(&$nums, $start, $ele) {
        return $nums[$start] != $ele;
    }

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Boolean
     */
    function search($nums, $target) {

        $cnt = count($nums);
        if (!$cnt) return false;

        $start = 0;
        $end = $cnt - 1;

        while ($start<=$end) {

            $mid = floor(($start+$end)/2);
            if ($target == $nums[$mid]) return true;

            $canBSearch = $this->isBinarySearchHelpful($nums, $start, $nums[$mid]);
            if (!$canBSearch) {
                $start++;
                continue;
            }

            $tInFirst = $this->existInFirst($nums, $start, $target);
            $mInFirst = $this->existInFirst($nums, $start, $nums[$mid]);

            if ($tInFirst ^ $mInFirst) {
                if ($target>$nums[$mid]) $end = $mid - 1;
                else $start = $mid + 1;
                
            } else {
                if ($target>$nums[$mid]) $start = $mid + 1;
                else $end = $mid - 1;
            }
        }

        return false;
    }
}

$nums = [2,5,6,0,0,1,2]; $target = 0;
$nums = [2,5,6,0,0,1,2]; $target = 3;
$so = new Solution();
$r = $so->search($nums, $target);
print_r($r);