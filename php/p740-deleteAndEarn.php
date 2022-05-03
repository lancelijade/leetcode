<?php

class Solution {

    private $nvs;
    private $debug = 1;

    function ggain($n) {
        $r = $n * $this->nvs[$n];
        if (isset($this->nvs[$n-1])) {
            $r -= ($n-1) * $this->nvs[$n-1];
            if (isset($this->nvs[$n-2])) $r += ($n-2) * $this->nvs[$n-2];
        }
        if (isset($this->nvs[$n+1])) {
            $r -= ($n+1) * $this->nvs[$n+1];
            if (isset($this->nvs[$n+2])) $r += ($n+2) * $this->nvs[$n+2];
        }
        return $r;   
    }

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function deleteAndEarn($nums) {
        
        $max = 0;

        $this->nvs = array_count_values($nums);

        $gains = [];
        foreach ($this->nvs as $n => $vs) {
            $gains[$n] = $this->ggain($n);
        }

        // php 8+ , to keep key rsorting
        krsort($gains);
        arsort($gains);

        if ($this->debug) {
            echo "nvs=";
            print_r($this->nvs); 
            echo "gains=";
            print_r($gains);
        }

        $n = array_keys($gains)[0];
        $cnt = 0;
        while ($n !== null) {
       
            $max += $n * $this->nvs[$n];
            if ($this->debug) echo "n=$n max=$max".PHP_EOL;
            
            unset($gains[$n]);
            unset($gains[$n-1]);
            unset($gains[$n+1]);
            unset($this->nvs[$n]);
            unset($this->nvs[$n-1]);
            unset($this->nvs[$n+1]);

            if (isset($this->nvs[$n-2])) $gains[$n-2] = $this->ggain($n-2);
            if (isset($this->nvs[$n-3])) $gains[$n-3] = $this->ggain($n-3);
            if (isset($this->nvs[$n+2])) $gains[$n+2] = $this->ggain($n+2);
            if (isset($this->nvs[$n+3])) $gains[$n+3] = $this->ggain($n+3);

            krsort($gains);
            arsort($gains);

            if ($this->debug) {
                echo "nvs=";
                print_r($this->nvs);

                echo "gains=";
                print_r($gains);
            }
            
            if ($gains)
                $n = array_keys($gains)[0];
            else
                break;

            //if ($cnt++==3) exit;
        }

        return $max;
    }
}

$nums = [4,10,10,8,1,4,10,9,7,6];
$nums = [2,2,3,3,3,4];
$nums = [3,4,2];
$nums = [8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4];
//$nums = [8,7,3,8,1,4,10,10,10,2];
//$nums = [1,2,3,15,16,17,18];
$so = new Solution();
$r = $so->deleteAndEarn($nums);
print_r($r);