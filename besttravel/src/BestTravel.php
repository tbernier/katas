<?php

final class BestTravel{
	public function choose_best_sum(int $distanceLimit, int $numberOftowns, array $listOfDistances): ?array
	{
		if($distanceLimit < 0 || $numberOftowns < 1 || empty($listOfDistances))
		{
			throw new InputException();
		}

		foreach($listOfDistances as $distance)
		{
			$this->checkDistance($distance);
		}

		return [];
	}

	private function checkDistance(int $distance): void
	{
		if($distance < 0)
		{
			throw new InputException();
		}
	}
}