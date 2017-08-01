<?php
	
	// return numbers of cows after x years
	function nb_cows($years){
		for ($year=0; $year < $years; $year++) { 
			if ($year >= 3){
				$nb = nb_cows($years - $year);
			}
		}
		return $nb + $years - 3;
	}

	echo nb_cows(6);
?>