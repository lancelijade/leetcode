<?php

class Solution {

    private $t1;
    private $t2;
    private $c = [];

    function dp($i, $j) {
        if ($i<0 or $j<0) return 0;
        if (isset($this->c[$i][$j])) return $this->c[$i][$j];

        if ($this->t1[$i] == $this->t2[$j]) {
            $r = $this->dp($i-1, $j-1);
            $this->c[$i-1][$j-1] = $r;
            return $r + 1;
        } else {
            $r1 = $this->dp($i-1, $j);
            $r2 = $this->dp($i, $j-1);
            $r = max($r1, $r2);
            $this->c[$i][$j] = $r;
            return $r;
        }
    }

    /**
     * @param String $text1
     * @param String $text2
     * @return Integer
     */
    function longestCommonSubsequence2($text1, $text2) {
        $this->t1 = $text1;
        $this->t2 = $text2;
        return $this->dp(strlen($text1)-1, strlen($text2)-1);
    }

    function longestCommonSubsequence($text1, $text2) {
        $len1 = strlen($text1);
        $len2 = strlen($text2);

        $dp = [];
        for ($i=0; $i<=$len1; $i++) $dp[$i][$len2] = 0;
        for ($j=0; $j<=$len2; $j++) $dp[$len1][$j] = 0;

        for ($i=$len1-1; $i>=0; $i--) {
            for ($j=$len2-1; $j>=0; $j--) {
                if ($text1[$i] == $text2[$j]) {
                    $dp[$i][$j] = $dp[$i+1][$j+1] + 1;
                } else {
                    $dp[$i][$j] = max($dp[$i+1][$j], $dp[$i][$j+1]);
                }
            }
        }
        return $dp[0][0];
    }    
}

$text1 = "ylqpejqbalahwr";
$text2 = "yrkzavgdmdgtqpg";
$so = new Solution();
$r = $so->longestCommonSubsequence($text1, $text2);
var_dump($r);