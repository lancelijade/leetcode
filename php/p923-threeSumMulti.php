<?php

class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $target
     * @return Integer
     */
    function threeSumMulti($arr, $target) {

        $sum = [$arr[0]];
        for ($i=1; $i<count($arr); $i++) $sum[$i] = $sum[$i-1] + $arr[$i];
        //print_r($sum);

        $r[0][1][$arr[0]] = 1;

        $r[1][1][$arr[0]] = 1;
        $r[1][1][$arr[1]] += 1;
        $r[1][2][$arr[0]+$arr[1]] = 1;
        
        for ($i=1; $i<count($arr); $i++) {

            for ($s=0; $s<=min($target, $sum[$i]); $s++) {
                if ($arr[$i] > $s) {
                    $r[$i][1][$s] = $r[$i-1][1][$s] ?? 0;
                    $r[$i][2][$s] = $r[$i-1][2][$s] ?? 0;
                    $r[$i][3][$s] = $r[$i-1][3][$s] ?? 0;
                } elseif ($arr[$i] == $s) {
                    $r[$i][1][$s] = ($r[$i-1][1][$s] ?? 0) + 1;
                    $r[$i][2][$s] = ($r[$i-1][1][0] ?? 0) + ($r[$i-1][2][$s] ?? 0);
                    $r[$i][3][$s] = ($r[$i-1][2][0] ?? 0) + ($r[$i-1][3][$s] ?? 0);
                } else {
                    $r[$i][1][$s] = $r[$i-1][1][$s] ?? 0;
                    $r[$i][2][$s] = ($r[$i-1][1][$s-$arr[$i]] ?? 0) + ($r[$i-1][2][$s] ?? 0);
                    $r[$i][3][$s] = ($r[$i-1][2][$s-$arr[$i]] ?? 0) + ($r[$i-1][3][$s] ?? 0);
                }

                $r[$i][1][$s] %= 1000000007;
                $r[$i][2][$s] %= 1000000007;
                $r[$i][3][$s] %= 1000000007;

                unset($r[$i-2][1]);
                unset($r[$i-2][2]);
                unset($r[$i-2][3]);
            }
        }

        //print_r($r);
        return $r[count($r)-1][3][$target];
    }


    function threeSumMulti_3pointer($A, $target) {

        $MOD = 1000000007;
        $ans = 0;
        sort($A);
        $size = count($A);

        for ($i=0; $i<$size; $i++) {

            $T = $target - $A[$i];
            $j = $i + 1;
            $k = $size - 1;

            while ($j < $k) {
                if ($A[$j] + $A[$k] < $T) {
                    $j++;

                } elseif ($A[$j] + $A[$k] > $T) {
                    $k--;

                } elseif ($A[$j] != $A[$k]) {
                    $left = 1;
                    $right = 1;
                    while ($j+1 < $k and $A[$j] == $A[$j+1]) {
                        $left++;
                        $j++;
                    }
                    while ($k-1 > $j and $A[$k] == $A[$k-1]) {
                        $right++;
                        $k--;
                    }

                    $ans += $left * $right;
                    $ans %= $MOD;
                    $j++;
                    $k--;

                } else {
                    $ans += ($k-$j+1) * ($k-$j) / 2;
                    $ans %= $MOD;
                    break;
                }
            }
        }

        return $ans;
    }

    
    function threeSumMulti_counting($A, $target) {  // Approach 2: Counting with Cases

        $MOD = 1000000007;
        $count = array_count_values($A);

        $ans = 0;

        // x != y != z
        for ($x=0; $x<=100; $x++) {
            for ($y=$x+1; $y<=100; $y++) {
                $z = $target - $x - $y;
                if ($y < $z and $z <=100) {
                    $ans += $count[$x] * $count[$y] * $count[$z];
                    $ans %= $MOD;
                }
            }
        }

        // x == y != z
        for ($x=0; $x<=100; $x++) {
            $z = $target - $x * 2;
            if ($x < $z and $z<=100) {
                $ans += $count[$x] * ($count[$x] - 1) / 2 * $count[$z];
                $ans %= $MOD;
            }
        }

        // x != y == z
        for ($x=0; $x<=100; $x++) {
            if ($target % 2 == $x % 2) {
                $y = ($target - $x) / 2;
                if ($x < $y and $y <= 100) {
                    $ans += $count[$x] * $count[$y] * ($count[$y] - 1) / 2;
                    $ans %= $MOD;
                }
            }
        }

        // x == y == z
        if ($target % 3 == 0) {
            $x = $target / 3;
            if (0 <= $x and $x <= 100) {
                $ans += $count[$x] * ($count[$x] - 1) * ($count[$x] - 2) / 6;
                $ans %= $MOD;
            }
        }

        return $ans;
    }
}


$arr = [1,1,2,2,3,3,4,4,5,5]; $target = 8;
//$arr = [1,1,2,2,2,2]; $target = 5;
//$arr = [0,0,0]; $target = 0;

$so = new Solution();
$r = $so->threeSumMulti_counting($arr, $target);
print_r($r);