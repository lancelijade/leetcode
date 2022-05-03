<?php

class Solution {

    /**
     * @param String $s
     * @param Integer $numRows
     * @return String
     */
    function convert($s, $numRows) {
        $len = strlen($s);
        $pos = 0;
        $r = [];
        $row = 0;
        $h = 0;

        if ($numRows == 1) $row_dir = 0;
        else $row_dir = 1;
        $h_dir = 0;
        while ($pos < $len) {
            //echo "$row $h $pos\n";

            $r[$row][$h] = $s[$pos];
            //print_r($r);

            if ($row_dir == 1) {
                $row++;
                if ($row>$numRows-1) {
                    $row_dir = -1;
                    $h_dir = 1;
                    $row -= 2;
                }
            } elseif ($row_dir == -1) {
                $row--;
                if ($row<0) {
                    $row_dir = 1;
                    $h_dir = 0;
                    $row += 2;
                }                
            } else {
                $h_dir = 1;
            }

            if ($h_dir == 1) {
                $h++;
            }
            
            $pos++;
        }

        return $this->tostr($r);
    }

    function totbl($r) {
        foreach ($r as $row) {
            for ($i=0; $i<=1000; $i++) {
                if (isset($row[$i])) echo $row[$i];
                else echo " ";
            }
            echo "\n";
        }        
    }

    function tostr($r) {
        $s = '';
        foreach ($r as $row) {
            $s .= join('', $row);
        }       
        return $s; 
    }
}


$s = "ABC";
$numRows = 1;

$so = new Solution();
$r = $so->convert($s, $numRows);
print_r($r);
