<?php

class Solution {

    /**
     * @param String $s
     * @return String
     */
    function minRemoveToMakeValid($s) {
        
        $q = new SplQueue();
        //$remove = [];
        for ($i=0; $i<strlen($s); $i++) {

            if ($s[$i] == '(') $q->push($i);

            if ($s[$i] == ')') {
                if (!$q->isEmpty()) {
                    $q->pop();
                } else {
                    $s[$i] = " ";
                }
            }
        }

        while (!$q->isEmpty()) $s[$q->pop()] = " ";

        return str_replace(' ', '', $s);
    }
}

$s = "lee(t(c)o)de)";
//$s = "))((";
$s = "a)b(c)d";
$so = new Solution();
$r = $so->minRemoveToMakeValid($s);
print_r($r);