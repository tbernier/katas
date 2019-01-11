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
    public function testIfThirdParameterIsInvalidThenRaisesException($input) :void
    {
    	$BestTravel = new BestTravel();
        $output = $BestTravel->choose_best_sum(100, 3, $input);
    }

    public function provideInputInvalidInputs()
    {
        yield [4, [5, 46, 45]];
        yield [5, [1]];
    }

    /**
    * @dataProvider provideInputInvalidInputs
    * @expectedException InputException
    */
    public function testIfNumberOfTownsIsLessThanNumberOfDistanceRaisesException($numberOfTowns, $listOfDistances)
    {
        $BestTravel = new BestTravel();
        $output = $BestTravel->choose_best_sum(100, $numberOfTowns, $listOfDistances);
    }

    public function provideValidInputsWithOneTown()
    {
        yield [25, 1, [5], 5];
        yield [25, 1, [6], 6];
        yield [25, 1, [6, 20], 20];
        yield [25, 1, [6, 20, 26], 20];
        yield [25, 1, [26], null];
    }

    /**
    * @dataProvider provideValidInputsWithOneTown
    */
    public function testWithOneTown($distanceLimit, $numberOfTowns, $listOfDistances, $expected)
    {
        $BestTravel = new BestTravel();
        $output = $BestTravel->choose_best_sum($distanceLimit, $numberOfTowns, $listOfDistances);
        $this->assertSame($expected, $output);
    }

    public function provideValidInputsWithTwoTowns()
    {
        yield [25, 2, [5, 15], 20];
        yield [25, 2, [5, 15, 16], 21];
        yield [25, 2, [16, 5, 15], 21];
        yield [25, 2, [20, 2, 9], 22];
        //todo
        //yield [25, 2, [20, 2, 9, 8, 25], 22];
    }

    /**
    * @dataProvider provideValidInputsWithTwoTowns
    */
    public function testWithTwoTowns($distanceLimit, $numberOfTowns, $listOfDistances, $expected)
    {
        $BestTravel = new BestTravel();
        $output = $BestTravel->choose_best_sum($distanceLimit, $numberOfTowns, $listOfDistances);
        $this->assertSame($expected, $output);
    }
}
