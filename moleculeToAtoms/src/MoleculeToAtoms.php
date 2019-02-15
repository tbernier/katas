<?php
final class MoleculeToAtoms{
	private $final = [];

	public function parse_molecule(string $input): array
	{
		if (empty($input))
		{
			throw new InputException('Invalid input');
		}

		$molecule = str_split($input);


		$last = '';
		foreach ($molecule as $character)
		{
			if (ctype_lower($character)){
				$this->final[$last.$character] = 1;
				unset($this->final[$last]);
				$last = $last.$character;
				continue;
			}

			if(!is_numeric($character)){
				$this->addAtom($character);

				$last = $character;
			}else{
				$number = (int)$character;
				if(isset($this->final[$last])){
					$number--;
				}
				$this->addAtom($last, $number);
			}
		}

		return $this->final;
	}

	private function addAtom(string $atom, int $number = 1) :void{
		if(!isset($this->final[$atom])){
			$this->final[$atom] = $number;
		}else{
			$this->final[$atom] += $number;
		}
	}
}