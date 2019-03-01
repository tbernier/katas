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

		$tmp = [];
		array_walk($molecule, function($value) use (&$tmp){
			$tmp[$value] = (isset($tmp[$value])? $tmp[$value]+1:1);
		});

		return $tmp;
	}

	public function flattenMolecule(string $molecule) : array{
		$last;
		$flatMolecule = [];
		$molecule = str_split($molecule);
		foreach ($molecule as $key => $character) {
			if(!isset($molecule[$key+1])){
				if(ctype_upper($character)){
					$flatMolecule[] = $character;
				}
				if(!is_numeric($character)){
					break;
				}
			}

			if(is_numeric($character)){
				for($i=1; $i < $character; $i++){
					$flatMolecule[] = $last;
				}
				continue;
			}

			$next = $molecule[$key+1];
			if(ctype_lower($next)){
				$flatMolecule[] = $character.$next;
				$last = $character.$next;
				continue;
			}

			if(ctype_lower($character)){
				continue;
			}

			$flatMolecule[] = $character;
			$last = $character;
		}

		return $flatMolecule;
	}
}