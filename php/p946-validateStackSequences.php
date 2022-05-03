<?php

class Solution {

    /**
     * @param Integer[] $pushed
     * @param Integer[] $popped
     * @return Boolean
     */
    function validateStackSequences($pushed, $popped) {
        
        $q = [];

        while ($pushed or $popped) {

            //echo join('', $pushed).PHP_EOL;
            //echo join('', $popped).PHP_EOL;
            //echo join('', $q).PHP_EOL."===".PHP_EOL;

            $do = false;
            while ($popped and end($q) === $popped[0]) {
                array_pop($q);
                array_shift($popped);
                $do = true;
            }

            //echo join('', $q).PHP_EOL."===".PHP_EOL;

            if ($pushed) {
                $q[] = array_shift($pushed);
                $do = true;
            }

            if (!$do) break;
        }

        return !$q;
    }
}

$pushed = [0];
$popped = [0];
$so = new Solution();
$r = $so->validateStackSequences($pushed, $popped);
var_dump($r);