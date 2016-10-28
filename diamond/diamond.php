<?php

function diamond($letter){
    $position = position($letter);
    $nb_rows = $nb_cols = $position*2-1;

    //construct multi array for first part and fill it with spaces
    $first_part = array_fill(1, $position, array_fill(1, $nb_cols, ' '));
    
    //fill first part
    foreach(range('a', $letter) as $char){
        $n_row = position($char);
        $first_part[$n_row][$position - (position($char)-1)] = $char;
        $first_part[$n_row][$position + (position($char)-1)] = $char;
    }

    //convert rows array to string
    foreach($first_part as $key => $row){
        $first_part[$key] = implode('', $row);
    }

    $center[] = array_pop($first_part); //pop center row because we don't want to mirror it
    $last_part = array_reverse($first_part); //mirror first part
    $result = array_merge($first_part, $center, $last_part); //merge all parts

    $result = implode("\n", $result);
    return $result;
}

function position($letter){
    return ord($letter) - 96;
}

echo diamond('o');

?>