<?php

class Solution {

    /**
     * @param String $path
     * @return String
     */
    function simplifyPath($path) {
        
        $arr = explode('/', $path);
        $q = [];

        foreach ($arr as $k => $p) {

            if ($p and $p!='.' and $p!='..') {
                $q[] = $p;

            } elseif ($p == '..') {
                
                array_pop($q);
            }
        }

        return '/'.join('/', $q);
    }
}

$path = "/home/vvv/";
$path = "/../";
//$path = "/home//foo/";
//$path = "/a/./b/../../c/";
$so = new Solution();
$r = $so->simplifyPath($path);
print_r($r);