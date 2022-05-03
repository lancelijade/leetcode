<?php

class Solution {

    /**
     * @param Integer[] $height
     * @return Integer
     */
    function trap($height) {

        $left_max = -1;
        $left_cur = -1;
        //$depth = [];
        $total = 0;

        $len = count($height);
        if ($len == 1) return 0;

        $i = 0;
        while ($i<$len-1) {

            echo "i=$i cur={$height[$i]} next={$height[$i+1]} maxleft=$left_max left=$left_cur total=$total ".PHP_EOL;

            if ($height[$i] < $height[$i+1]) {      // 上坡

                if ($left_cur != -1) {      // 已经在坑里

                    for ($j=$left_cur+1; $j<$i+1; $j++) {
                        $min = min($height[$i+1], $height[$left_cur]);
                        $total += max(0, $min - $height[$j]);   // 用 left_cur 与 i+1 中较小的确认收益
                        $height[$j] = $min;             // 把当前坑填满
                    }
                    $left_cur = $height[$i+1] > $height[$left_cur] ? $i+1 : $left_cur;
                }

                if ($left_max != -1 and $height[$i+1] >= $height[$left_max]) {   // 大坑结束

                    for ($j=$left_max+1; $j<$i+1; $j++) {
                        $total += max(0, $height[$left_max] - $height[$j]);   // 确认收益
                        $height[$j] = $height[$left_max];             // 把当前坑填满
                    }
                    $left_max = $i + 1;
                }

            } else {

                if ($left_max == -1) {
                    $left_max = $i;
                    $left_cur = $i;
                } 
            }

            echo "max=$left_max left=$left_cur total=$total ".join('',$height).PHP_EOL."===".PHP_EOL;

            $i++;
        }

        
        return $total;
    }
}

//$height = [0,1,0,2,1,0,1,3,2,1,2,1];
//$height = [4,2,0,3,2,5];
//$height = [4,2,3];
//$height = [0];
//$height = [5,4,1,2];
$height = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3];
$so = new Solution();
$r = $so->trap($height);
print_r($r);