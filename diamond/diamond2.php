<?php

function diamond2($letter){
    $position = position($letter);
    $nb_rows = $nb_cols = $position*2-1;

    //construct multi array and fill it with spaces
    $result = array_fill(1, $nb_rows, array_fill(1, $nb_cols, ' '));
    
    //place letters in array
    foreach(range('a', $letter) as $char){
        $n_row = position($char);
        $result[$n_row][$position - (position($char)-1)] = 
        $result[$n_row][$position + (position($char)-1)] = 
        $result[$nb_rows - ($n_row-1)][$position - (position($char)-1)] = 
        $result[$nb_rows - ($n_row-1)][$position + (position($char)-1)] = $char;
    }

    //convert rows array to string
    foreach($result as $key => $row){
        $result[$key] = implode('', $row);
    }

    $result = implode("\n", $result);
    return $result;
}

function position($letter){
    return ord($letter) - 96;
}

echo diamond2('j');

?>