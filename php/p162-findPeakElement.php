<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findPeakElement($nums) {
        
        return max($nums);

        $cnt = count($nums);
        if ($cnt==1) return 0;
        
        $nums[-1] = PHP_INT_MIN;
        $nums[$cnt] = PHP_INT_MIN;
        $pos = ceil($cnt/2);
        
        $c = 0;

        while (1) {
            if ($c++==100) exit;

            echo $pos.PHP_EOL;

            if ($nums[$pos]>$nums[$pos-1] and $nums[$pos]>$nums[$pos+1]) 
                return $pos;
            elseif ($nums[$pos]<$nums[$pos-1])
                $pos -= ceil($pos/2);
            elseif ($nums[$pos]<$nums[$pos+1])
                $pos += ceil(($cnt-$pos)/2);
        }
        
    }
}

$input = <<<EOB
[1,2,3,1]
[1,2,1,3,5,6,4]
[2,3,4,3,2,1]
[1,2,3,4,5]
[1,2,3,2,1]
EOB;
$inputline = 1;

$inputs = explode("\n", $input);

$so = new Solution();

while ($inputs) {
    $args = [];
    for ($i=$inputline; $i>0; $i--) {
        $args[] = array_shift($inputs);
    }
    $r = $so->findPeakElement(eval('return '.$args[0].';'));
    print_r($args[0]);
    echo PHP_EOL;
    print_r($r);
    echo PHP_EOL;
}
