<?php
declare(strict_types=1);

final class DeleteADigit
{
	private function __construct()
    {
    }

	public static function deleteADigit($param)
	{
		if ( ! is_int($param)) {
			throw new \Exception('Input is not an integer');
		}

		if (($param < 10) || ($param > 1000000)) {
			throw new \Exception('Input is out of range');
		}

		return $param;
	}
}