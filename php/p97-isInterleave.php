<?php

class Solution {

    private $s1;
    private $s2;
    private $s3;
    private $len1;
    private $len2;
    private $len3;

    private $cache = [];

    function dp($i, $p1, $p2) {

        //echo "i=$i p1=$p1 p2=$p2".PHP_EOL;
        if ($i>=$this->len3) return true;
        if (isset($this->cache[$i][$p1][$p2])) return $this->cache[$i][$p1][$p2];

        if ($this->s3[$i]==($this->s1[$p1]??0)) $r1 = $this->dp($i+1, $p1+1, $p2);
        //echo "r1=$r1".PHP_EOL;
        if ($r1 ?? 0) {
            $this->cache[$i][$p1][$p2] = true;
            return true;
        }

        if ($this->s3[$i]==($this->s2[$p2]??0)) $r2 = $this->dp($i+1, $p1, $p2+1);
        //echo "r2=$r2".PHP_EOL;
        if ($r2 ?? 0) {
            $this->cache[$i][$p1][$p2] = true;
            return true;
        }

        $this->cache[$i][$p1][$p2] = false;
        return false;
    }


    /**
     * @param String $s1
     * @param String $s2
     * @param String $s3
     * @return Boolean
     */
    function isInterleave($s1, $s2, $s3) {
        
        if (strlen($s3)!=strlen($s1)+strlen($s2)) return false;

        $this->s1 = $s1;
        $this->s2 = $s2;
        $this->s3 = $s3;

        $this->len1 = strlen($s1);
        $this->len2 = strlen($s2);
        $this->len3 = strlen($s3);

        $r = $this->dp(0, 0, 0);
        //print_r($this->cache);
        return $r;
    }
}

$s1 = "aabcc"; $s2 = "dbbca"; $s3 = "aadbbcbcac";
//$s1 = "aabcc"; $s2 = "dbbca"; $s3 = "aadbbbaccc";
//$s1 = "a"; $s2=""; $s3="aa";
//$s1="bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"; $s2="babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab";$s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab";


$so = new Solution();
$r = $so->isInterleave($s1, $s2, $s3);
print_r($r);