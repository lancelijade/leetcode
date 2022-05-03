<?php

class Solution {

    private $h;
    private $len;
    private $total = 0;

    private $cnt;

    function keng($start, $from) {

        echo "{$this->h[$start]} start=$start from=$from total={$this->total} ".join('',$this->h).PHP_EOL;

        if ($this->cnt++==100) exit;

        if ($start > $this->len - 1) return false;

        if ($this->h[$start] > $this->h[$start+1]) {
            $ns = $this->keng($start+1, $start);
            if ($ns === false) return false;
            return $this->keng($ns, $from);

        } elseif ($this->h[$start] == $this->h[$start+1]) {
            $ns = $this->keng($start+1, $from);
            if ($ns === false) return false;
            return $this->keng($ns, $from);

        } else {
            $do = false;
            $min = min($this->h[$start+1], $this->h[$from]);
            echo "from_val={$this->h[$from]} next_val={$this->h[$start+1]}".PHP_EOL;
            for ($i=$from+1; $i<$start+1; $i++) {
                $this->total += max(0, $min - $this->h[$i]);   // 用 from 与 start 中较小的确认收益
                $this->h[$i] = $min;                           // 把当前坑填满  
                $do = true;
            }
            return $start;
        }
       

        return $ns;
    }

    function trap($height) {

        $this->h = $height;
        $this->len = count($height);
        $ns = 0;

        //while ($ns !== false) {
            $ns = $this->keng(0, 0);
            echo "ns=$ns".PHP_EOL;
        //}

        return $this->total;
    }


}

$height = [0,1,0,2,1,0,1,3,2,1,2,1];
//$height = [4,2,0,3,2,5];
//$height = [4,2,3];
//$height = [0];
//$height = [5,4,1,2];
//$height = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3];
$so = new Solution();
$r = $so->trap($height);
print_r($r);