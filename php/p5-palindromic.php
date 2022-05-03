<?php

class Solution {

    function isPalindromic($s, $b=0, $e=null) {
        //echo "$s $b $e\n";
        if ($b === null) $b = 0;
        if ($e === null) $e = strlen($s) - 1;
        while ($e > $b) {
            //echo "{$s[$b]} {$s[$e]}\n";
            if ($s[$b] != $s[$e]) return false;
            $b++;
            $e--;
        }
        return true;
    }

    /**
     * @param String $s
     * @return String
     */
    function longestPalindrome($s) {
        $len = strlen($s);
        $len0 = $len;
        while ($len>0)
        {
            //echo "len=$len\n";
            $p = 0;
            while ($p+$len<=$len0)
            {
                //if ($this->isPalindromic($s, $p, $p+$len-1)) return substr($s, $p, $len);
                $b = $p;
                $e = $p + $len - 1;
                while ($e > $b) {
                    if ($s[$b] != $s[$e]) goto n;
                    $b++;
                    $e--;                    
                }
                return substr($s, $p, $len);
n:
                $p++;
            }
            $len--;
        }
        return true;
    }

    function longestPalindromeS($s) {
        $len = strlen($s);
        $len0 = $len;
        $longest = 1;
        $b0 = 0;
        $e0 = 0;
        for ($i=1; $i<$len; $i++) {
            //echo "i=$i long=$longest\n";
            $b = $i-1;
            $e = $i+1;
            while ($b>=0 and $e<$len && $this->isPalindromic($s, $b, $e)) {
                if ($e-$b+1>$longest) {
                    $longest = $e - $b + 1;
                    $b0 = $b;
                    $e0 = $e;
                    //echo "1:$longest $b0 $e0\n";
                }
                $b--;
                $e++;
            }

            if ($s[$i-1] == $s[$i]) {
                if (2>$longest) {
                    $longest = 2;
                    $b0 = $i - 1;
                    $e0 = $i;
                }
                $b = $i-2;
                $e = $i+1;
                while ($b>=0 and $e<$len and $this->isPalindromic($s, $b, $e)) {
                    if ($e-$b+1>$longest) {
                        $longest = $e - $b + 1;
                        $b0 = $b;
                        $e0 = $e;
                        //echo "2:$longest $b0 $e0\n";
                    }
                    $b--;
                    $e++;
                }
            }
        }
        return substr($s, $b0, $e0-$b0+1);
    }
}

$s = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc";

$so = new Solution();
$r = $so->longestPalindrome($s);
//$r = $so->isPalindromic($s,1,3);
print_r($r);