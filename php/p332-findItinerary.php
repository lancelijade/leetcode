<?php

class Solution {

    private $len = 0;

    function dfs($tickets, $city, $path) {

        //echo "city=$city ".join('->',$path).PHP_EOL;
        //print_r($tickets);

        $last = end($path);
        $tk = [$last,$city];

        $pos = array_search($tk, $tickets);
        if ($pos!==false) unset($tickets[$pos]);

        $path[] = $city;
        if (count($path) == $this->len+1) return $path;

        foreach ($tickets as $t) {
            if ($t[0] == $city) {
                $r = $this->dfs($tickets, $t[1], $path);
                if ($r) return $r;
            }
        }

        return false;
    }


    /**
     * @param String[][] $tickets
     * @return String[]
     */
    function findItinerary($tickets) {
        
        sort($tickets);
        $this->len = count($tickets);
        return $this->dfs($tickets, "JFK", []);
    }
}

$tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]];
//$tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]];
//$tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]];
//$tickets = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]];
$tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]];

$so = new Solution();
$r = $so->findItinerary($tickets);
print_r($r);