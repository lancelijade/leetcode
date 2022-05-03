<?php

class Solution {

    /**
     * @param Integer[][] $mat1
     * @param Integer[][] $mat2
     * @return Integer[][]
     */
    function multiply2($mat1, $mat2) {
        
        $m = count($mat1);
        $k = count($mat1[0]);
        $n = count($mat2[0]);
        echo "m=$m k=$k n=$n".PHP_EOL;

        $r = [];

        for ($i=0; $i<$m; $i++) {
            $r[$i] = [];
            for ($j=0; $j<$n; $j++) {
                $r[$i][$j] = 0;
                for ($elementPos=0; $elementPos<$k; $elementPos++) {
                    $r[$i][$j] += $mat1[$i][$elementPos] * $mat2[$elementPos][$j];
                }
            }
        }

        return $r;
    }

    function multiply($mat1, $mat2) {
        
        $m = count($mat1);
        $k = count($mat1[0]);
        $n = count($mat2[0]);
        echo "m=$m k=$k n=$n".PHP_EOL;

        $r = [];

        for ($i=0; $i<$m; $i++) {
            $r[$i] = array_fill(0, $n, 0);
            for ($elementPos=0; $elementPos<$k; $elementPos++) {
                if ($mat1[$i][$elementPos] != 0) {
                    for ($j=0; $j<$n; $j++) {
                        $r[$i][$j] += $mat1[$i][$elementPos] * $mat2[$elementPos][$j];
                    }
                }
            }
        }

        return $r;
    }    
}

$mat1 = [[1,0,0],[-1,0,3]]; $mat2 = [[7,0,0],[0,0,0],[0,0,1]];
//$mat1 = [[1,0,2],[-1,3,1]]; $mat2 = [[3,1],[2,1],[1,0]];
$mat1 = [[0]]; $mat2 = [[0]];
$mat1 = [[1,-5]]; $mat2 = [[12],[-1]];


$so = new Solution();
$r = $so->multiply($mat1, $mat2);
print_r($r);