<?php
declare(strict_types=1);

final class DeleteADigit
{
	private function __construct()
    {
    }

	public static function deleteADigit($param)
	{
		if ( ! is_int($param))
		{
			throw new NanException('Input is not an integer');
		}

		if (($param < 10) || ($param > 1000000))
		{
			throw new RangeException('Input is out of range');
		}

		$param = str_split((string)$param);

		foreach ($param as $key => $digit)
		{
			if($digit < $param[$key+1])
			{
				unset($param[$key]);
				break;
			}

			if($key === (count($param)-2))
			{
				unset($param[$key+1]);
				break;
			}
		}

		return (int)implode($param);
	}
}