<?php
declare(strict_types=1);

use PHPUnit\Framework\TestCase;

final class DeleteADigitTest extends TestCase
{

    public function provideInputNan()
    {
        yield ['a'];
        yield [1.20];
        yield [null];
    }

    /**
    * @dataProvider provideInputNan
    * @expectedException NanException
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
    * @expectedException RangeException
    */
    public function testWhenInputParameterIsOutsideRangeThenRisesException($input) :void
    {
        $output = DeleteADigit::deleteADigit($input);
    }

    public function provideInputTwoDigits()
    {
        yield [52, 5];
        yield [42, 4];
        yield [27, 7];
        yield [80, 8];
        yield [52, 5];
        yield [10, 1];
    }

    /**
    * @dataProvider provideInputTwoDigits
    *
    */
    public function testWithTwoDigits($input, $expected) :void
    {
        $output = DeleteADigit::deleteADigit($input);
        $this->assertSame($expected, $output);
    }

    public function provideInput()
    {
        yield [152, 52];
        yield [58496, 8496];
        yield [87654, 8765];
        yield [45678, 5678];
        yield [56784, 6784];
        yield [98456, 9856];
        yield [333245, 33345];
        yield [33361, 3361];
        yield [1001, 101];
        yield [1111, 111];
        yield [1000000, 100000];
    }

    /**
    * @dataProvider provideInput
    *
    */
    public function testWithMultipleDigits($input, $expected) :void
    {
        $output = DeleteADigit::deleteADigit($input);
        $this->assertSame($expected, $output);
    }
}