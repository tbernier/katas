<?php
declare(strict_types=1);

use PHPUnit\Framework\TestCase;

final class DeleteADigitTest extends TestCase
{

    public function provideInput()
    {
        yield ['a'];
        yield [1.20];
        yield [null];
    }

    /**
    * @dataProvider provideInput
    * @expectedException \Exception
    */
    public function testIfInputParameterIsNotAnIntegerThenRisesException($input) :void
    {
        $output = DeleteADigit::deleteADigit($input);
    }

    public function provideInputOutOfRange()
    {
        yield [9];
        yield [1000001];
    }

    /**
    * @dataProvider provideInputOutOfRange
    * @expectedException \Exception
    */
    public function testWhenInputParameterIsOutsideRangeThenRisesException($input) :void
    {
        $output = DeleteADigit::deleteADigit($input);
    }
}