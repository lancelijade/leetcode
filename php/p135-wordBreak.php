<?php

class Solution {

    /**
     * @param String $s
     * @param String[] $wordDict
     * @return Boolean
     */
    function wordBreak($s, $wordDict) {
        
        $dp = [];
        $dp[-1] = true;

        $len = strlen($s);
        for ($i=0; $i<$len; $i++) {

            if (!isset($dp[$i-1])) continue;

            foreach ($wordDict as $word) {
                $l = strlen($word);
                if (substr($s, $i, $l) == $word) $dp[$i+$l-1] = true;
            }
            print_r($dp);
        }

        return isset($dp[$len-1]);
    }
}

$s = "applepenapple";
$wordDict = ["apple","pen"];
//$s = "a";
//$wordDict = ["b"];
$so = new Solution();
$r = $so->wordBreak($s, $wordDict);
print_r($r);