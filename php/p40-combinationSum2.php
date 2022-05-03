<?php

class Solution {

    private $r = [];
    private $va;
    private $vaks;
    
    function sum($currarr, $vak, $target) {

        //echo join('', $currarr)." vak=$vak target=$target".PHP_EOL;

        if (!isset($this->vaks[$vak])) return false;

        $key = $this->vaks[$vak];
        $val = $this->va[$key];
        //if ($key > $target) return false;

        //echo join('', $currarr)." vak=$vak target=$target key=$key val=$val".PHP_EOL;

        $max_val_num = floor($target / $key);
        $tarr = $currarr;
        for ($i=1; $i<=min($max_val_num, $val); $i++) {

            $tarr[] = $key;
            $n = $i * $key;
            //echo "i=$i n=$n tarr=".join('',$tarr).PHP_EOL;

            if ($n == $target) {
                $this->r[] = $tarr;
                break;
            }
            $this->sum($tarr, $vak+1, $target-$n);
        }

        $this->sum($currarr, $vak+1, $target);

    }

    /**
     * @param Integer[] $candidates
     * @param Integer $target
     * @return Integer[][]
     */
    function combinationSum2($candidates, $target) {
        
        $va = array_count_values($candidates);
        ksort($va);
        $this->va = $va;
        $this->vaks = array_keys($this->va);
        //print_r($this->va);
        //print_r($this->vaks);

        $this->sum([], 0, $target);

        return $this->r;
    }
}

$candidates = [4,4,2,1,4,2,2,1,3];
$target = 6;

$so = new Solution();
$r = $so->combinationSum2($candidates, $target);
print_r($r);
