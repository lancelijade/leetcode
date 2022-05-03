<?php

class Solution {

    private $dp;
    private $r = [];

    function buildStr($pos, $cstr) {

        $warr = $this->dp[$pos];

        foreach ($warr as $w) {
            $nstr = $w[0].' '.$cstr;
            if ($pos-$w[1] == -1) {
                $this->r[] = rtrim($nstr);
            } else {
                $this->buildStr($pos-$w[1], $nstr);
            }
        }
    }

    /**
     * @param String $s
     * @param String[] $wordDict
     * @return Boolean
     */
    function wordBreak($s, $wordDict) {
        
        $dp = [];
        $dp[-1] = [];

        $len = strlen($s);
        for ($i=0; $i<$len; $i++) {

            if (!isset($dp[$i-1])) continue;

            foreach ($wordDict as $word) {
                $l = strlen($word);
                if (substr($s, $i, $l) == $word) $dp[$i+$l-1][] = [$word, $l];
            }
        }

        //print_r($dp);
        if (!isset($dp[$len-1])) return [];

        $this->dp = $dp;
        $this->buildStr($len-1, '');
        return $this->r;
    }
}

$s = "applepenapple";
$wordDict = ["apple","pen"];
$s = "catsanddog";
$wordDict = ["cat","cats","and","sand","dog"];
$s = "pineapplepenapple";
$wordDict = ["apple","pen","applepen","pine","pineapple"];
$so = new Solution();
$r = $so->wordBreak($s, $wordDict);
print_r($r);