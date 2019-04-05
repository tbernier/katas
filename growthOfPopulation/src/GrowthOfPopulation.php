<?php

final class GrowthOfPopulation{
	public function nb_year(int $p0 , float $percent, int $aug, int $p):int
	{
		if($p0 <= 0 || $percent < 0 || $p <= 0 ){
			throw new \InvalidArgumentException("Invalid Argument Exception", 1);
		}

		if($p0 > $p){
			throw new \InvalidArgumentException("P0 should be inferior to P", 1);
		}
		return 0;
	}

	public function computePopulation(int $p, float $percent, int $aug):int
	{
		return $p + $p * $percent / 100 + $aug;
	}
}