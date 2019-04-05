<?php

use PHPUnit\Framework\TestCase;

final class GrowthOfPopulationTest extends TestCase{

    public function provideInvalidParameters(){
        yield [-1000, 5, 100, 1500];
        yield [1000, -5, 100, 1500];
        yield [1000, 5, 100, -1500];
    }

    /**
     * @dataProvider provideInvalidParameters
     * @expectedException \InvalidArgumentException
     */
    public function testIfParametersAreInvalidThenRisesException($p0, $percent, $aug, $p){
        $year = GrowthOfPopulation::nb_year($p0, $percent, $aug, $p);
    }

    public function providePInferiorToP0Parameters(){
        yield [1000, 5, 100, 800];
    }

    /**
     * @dataProvider providePInferiorToP0Parameters
     * @expectedException \InvalidArgumentException
     */
    public function testIfPIsInferiorToP0ThenRisesException($p0, $percent, $aug, $p){
        $year = GrowthOfPopulation::nb_year($p0, $percent, $aug, $p);
    }

    public function provideOneYearParameters(){
        yield [1000, 5, 100, 1150];
    }

    /**
     * @dataProvider provideOneYearParameters
     */
    public function testComputePopulationGrowthInOneYear($p0, $percent, $aug, $expected){
        $population = GrowthOfPopulation::computePopulation($p0, $percent, $aug);

        $this->assertSame($expected, $population);
    }

}
