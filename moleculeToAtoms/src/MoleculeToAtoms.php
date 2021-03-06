<?php
final class MoleculeToAtoms{
	private $final = [];

	public function parse_molecule(string $input): array
	{
		if (empty($input))
		{
			throw new InputException('Invalid input');
		}

		$molecule = $this->distributeMolecule($input);
		$molecule = $this->flattenMolecule($molecule);

		$tmp = [];
		array_walk($molecule, function($value) use (&$tmp){
			$tmp[$value] = (isset($tmp[$value])? $tmp[$value]+1:1);
		});

		return $tmp;
	}

	public function flattenMolecule(string $molecule) : array{
		$molecule = str_split($molecule);
		$last;
		$flatMolecule = [];
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

	public function distributeMolecule(string $molecule) : string{
		$factoredPart = $this->getFactoredPart($molecule);
		if(!empty($factoredPart)){
			return $factoredPart;
		}

		return $molecule;
	}

	public function getFactoredPart(string $molecule) : string{
		if(false !== strpos($molecule, '(')){
			$start = strpos($molecule, '(') + 1;
			$end = strpos($molecule, ')');

			$factorisedPart = substr($molecule, $start, $end - $start);
			$coef = substr($molecule, $end + 1, 1);

			return $this->getDistributedPart($factorisedPart, $coef);
		}

		return '';
	}

	public function getDistributedPart(string $factoredPart, int $coef) : string{

		$return = '';
		for($i=0; $i < $coef; $i++){
			$return .= $factoredPart;
		}
		return $return;
	}

}