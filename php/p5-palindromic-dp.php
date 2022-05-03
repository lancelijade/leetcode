<?php

class Solution {

    function print_matrix($t, $n)
    {
        for ($i=0; $i<$n; $i++)
        {
            for ($j=0; $j<$n; $j++)
            {
                echo $t[$i][$j].' ';
            }
            echo "\n";
        }
        echo "=====\n";
    }

    /**
     * @param String $s
     * @return String
     */
    function longestPalindrome($s) {

        $sz = strlen($s);
        
        // Base Case Length 1
        if($sz == 1) return $s;
		
		// Base Case Length 2
        if($sz == 2 && $s[0] == $s[1]) return $s;
        if($sz == 2 && $s[0] != $s[1]) return $s[0];
        
        $longest = 0;
        
        $dp = [];  
        $p = 0;
        $q = 0;

	
        for($i = 0; $i<$sz; $i++)
        {
            $dp[$i][$i] = 1;
            if($i>=1)
            {
                if($s[$i-1] == $s[$i])
                {
                    $dp[$i-1][$i] = 1;
                    $p = $i-1;
                    $q = $i;
                }
            }
        }
        //$this->print_matrix($dp, 8);

        for($i = 2; $i<$sz; ++$i)
        {
            for($j = 0; $j<$sz-$i; ++$j)
            {        
                //echo "$i $j\n";
                //$this->print_matrix($dp, 8);

                if($s[$j] == $s[$i+$j] && $dp[$j+1][$j+$i-1])
                {
                    $dp[$j][$i+$j] = 1;
                    if($i > $longest)
                    {
                        $longest = $i;
                        $q = $i+$j;
                        $p = $j;
                        //echo "$i $j\n";
                        //$this->print_matrix($dp, 8);                        
                    }
                }
            }
        }
         
        return substr($s, $p, $q-$p+1);  
    }
}

$s = "dadab";

$so = new Solution();
$r = $so->longestPalindrome($s);
//$r = $so->isPalindromic($s,1,3);
print_r($r);