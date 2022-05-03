<?php

class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function validPalindrome($s, $lvl=1) {
        
        $left = 0;
        $right = strlen($s)-1;
        $n = 0;

        while ($left<$right) {

            echo "{$s[$left]} {$s[$right]}".PHP_EOL;
            if ($s[$left] != $s[$right]) {

                if ($lvl>1) return false;

                $n++;
                if ($n>1) return false;

                if ($left+1==$right) {  // mid
                    return true;
                
                } else {

                    $r1 = $this->validPalindrome(substr($s, $left+1, $right-$left), $lvl+1);
                    $r2 = $this->validPalindrome(substr($s, $left, $right-$left), $lvl+1);
                    return $r1 or $r2;
                }
            }

            $left++;
            $right--;
        }

        return true;
    }

}

$s = "aba";
$s = "aguokepatgbnvfqmgml cupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucu lmgmqfvnbgtapekouga";
//$s = "1a3 d 31";
//$s = "13 d 3a1";
$so = new Solution();
$r = $so->validPalindrome($s);
print_r($r);