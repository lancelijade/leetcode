<?php

class Solution {

    private $cache = [];

    function dp($i, $char) {

        if ($i==0) return 1;
        if (isset($this->cache[$i][$char])) return $this->cache[$i][$char];

        switch ($char) {
            case 'a':
                $r = $this->dp($i-1, 'e') + $this->dp($i-1, 'i') + $this->dp($i-1, 'u');
                break;
            case 'e':
                $r = $this->dp($i-1, 'a') + $this->dp($i-1, 'i');
                break;
            case 'i':
                $r = $this->dp($i-1, 'e') + $this->dp($i-1, 'o');
                break;
            case 'o':
                $r = $this->dp($i-1, 'i');
                break;
            case 'u':
                $r = $this->dp($i-1, 'i') + $this->dp($i-1, 'o');
                break;
        }

        $r = $r % 1000000007;
        $this->cache[$i][$char] = $r;
        return $r;
    }


    /**
     * @param Integer $n
     * @return Integer
     */
    function countVowelPermutation2($n) {
        $r = $this->dp($n-1, 'a') + 
                $this->dp($n-1, 'e') +
                $this->dp($n-1, 'i') +
                $this->dp($n-1, 'o') +
                $this->dp($n-1, 'u');
        return $r % 1000000007;
    }


    function countVowelPermutation($n) {
        $dp[0]['a'] = 1;
        $dp[0]['e'] = 1;
        $dp[0]['i'] = 1;
        $dp[0]['o'] = 1;
        $dp[0]['u'] = 1;

        for ($i=1; $i<$n; $i++) {
            $dp[$i]['a'] = ($dp[$i-1]['e'] + $dp[$i-1]['i'] + $dp[$i-1]['u']) % 1000000007;
            $dp[$i]['e'] = ($dp[$i-1]['a'] + $dp[$i-1]['i']) % 1000000007;
            $dp[$i]['i'] = ($dp[$i-1]['e'] + $dp[$i-1]['o']) % 1000000007;
            $dp[$i]['o'] = $dp[$i-1]['i'];
            $dp[$i]['u'] = ($dp[$i-1]['i'] + $dp[$i-1]['o']) % 1000000007;
        }

        return ($dp[$n-1]['a'] + $dp[$n-1]['e'] + $dp[$n-1]['i'] + $dp[$n-1]['o'] + $dp[$n-1]['u']) % 1000000007;
    }    
}

$n = 144;
//$n = 2;
$so = new Solution();
$r = $so->countVowelPermutation($n);
print_r($r);