<?php
final class MoleculeToAtoms{
	private $final = [];

	public function parse_molecule(string $input): array
	{
		if (empty($input))
		{
			throw new InputException('Invalid input');
		}

		$molecule = $this->flattenMolecule($input);

		$molecule = str_split($molecule);


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

	private function flattenMolecule(string $molecule) : string{

		$last;
		$flatMolecule = '';
		$molecule = str_split($molecule);
		foreach ($molecule as $key => $character) {
			if(!isset($molecule[$key+1])){
				if(ctype_upper($next)){
					$flatMolecule .= $character;
				}
				break;
			}

			$next = $molecule[$key+1];
			if(ctype_lower($next)){
				$flatMolecule .= $character;
				$last = $last.$character;
				break;
			}

			if(is_numeric($next)){
				//TODO
				break;
			}

			$flatMolecule .= $character;
			$last = $character;
		}

		return $molecule;
	}
}