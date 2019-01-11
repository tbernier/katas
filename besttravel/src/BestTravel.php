<?php

final class BestTravel{
	public function choose_best_sum(int $distanceLimit, int $numberOftowns, array $listOfDistances): ?int
	{
		if($distanceLimit < 0 || $numberOftowns < 1 || empty($listOfDistances) || $numberOftowns > count($listOfDistances))
		{
			throw new InputException();
		}

		foreach($listOfDistances as $key => $distance)
		{
			$this->checkDistance($distance);
			if($distance > $distanceLimit)
			{
				unset($listOfDistances[$key]);
			}
		}

		if(empty($listOfDistances))
		{
			return null;
		}

		if($numberOftowns === 1)
		{
			return max($listOfDistances);
		}

		rsort($listOfDistances);
		$result = array_shift($listOfDistances);
		foreach ($listOfDistances as $distance) {
			if($result + $distance <= $distanceLimit)
			{
				return $result + $distance;
			}
		}

		return array_sum($listOfDistances);
	}

	private function checkDistance(int $distance): void
	{
		if($distance < 0)
		{
			throw new InputException();
		}
	}
}