<?php
final class MoleculeToAtoms{

	public static function parse_molecule(string $input): array
	{
		if (empty($input))
		{
			throw new InputException('Invalid input');
		}

		$molecule = str_split($input);


		$last = '';
		$final = [];
		foreach ($molecule as $character)
		{
			if (ctype_lower($character)){
				$final[$last.$character] = 1;
				unset($final[$last]);
				$last = $last.$character;
				break;
			}

			if (!is_numeric($character))
			{
				$final[$character] = 1;
				$last = $character;
			} else {
				$final[$last] = (int)$character;
			}
		}

		return $final;
	}
}