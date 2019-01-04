<?php

use PHPUnit\Framework\TestCase;

final class BestTravelTest extends TestCase
{
    public function provideInputNegativeInteger()
    {
        yield [-5];
    }

    /**
    * @dataProvider provideInputNegativeInteger
    * @expectedException InputException
    */
    public function testIfFistParameterIsNotPositiveIntegerThenRisesException($input) :void
    {
        $output = BestTravel::choose_best_sum($input, 3, [10, 12, 13, 15]);
    }

    /**
    * @dataProvider provideInputNegativeInteger
    * @expectedException InputException
    */
    public function testIfSecondParameterIsNotPositiveIntegerGreaterThanZeroThenRisesException($input) :void
    {
        $output = BestTravel::choose_best_sum(100, $input, [10, 12, 13, 15]);
    }

    public function provideInputInvalidDistances()
    {
        yield [[-1]];
        yield [[]];
        yield [[10, 15, -1, 20]];
    }

        /**
    * @dataProvider provideInputInvalidDistances
    * @expectedException InputException
    */
    public function testIfThirdParameterIsInvalidThenRisesException($input) :void
    {
    	$BestTravel = new BestTravel();
        $output = $BestTravel->choose_best_sum(100, 3, $input);
    }
}
