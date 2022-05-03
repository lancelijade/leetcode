<?php

class Solution {

    /**
     * @param Integer[] $people
     * @param Integer $limit
     * @return Integer
     */
    function numRescueBoats($people, $limit) {
        
        $vs = array_count_values($people);

        //print_r($vs);
        $r = $vs[$limit] ?? 0;
        unset($vs[$limit]);

        krsort($vs);
        $ks = array_keys($vs);
        $left = 0;
        foreach ($ks as $weight) {

            $num = $vs[$weight];
            if (!$num) continue;

            if ($weight>$limit/2) {
                $r += $num;

                //echo "weight=$weight num=$num r=$r".PHP_EOL;
                for ($i=$limit-$weight; $i>=1; $i--) {
                    if (isset($vs[$i]) and $vs[$i] > 0) {
                        //echo $vs[$i].' '.$i.' '.$num.PHP_EOL;
                        if ($vs[$i] >= $num) {
                            $vs[$i] -= $num;
                            //echo $vs[$i].PHP_EOL;
                            continue 2;
                        } else {
                            $num -= $vs[$i];
                            $vs[$i] = 0;
                        }
                    }
                }
            } else {

                $left += $num;
            }
        }

        return $r+ceil($left/2);
    }
}

$people = [3,5,3,4]; $limit = 5;
$people = [3,2,2,1]; $limit = 3;
$people = [5,5,5,5,2,2,2,2,1]; $limit = 6;
$so = new Solution();
$r = $so->numRescueBoats($people, $limit);
print_r($r);