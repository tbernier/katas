<?php

use PHPUnit\Framework\TestCase;

final class MoleculeToAtomsTest extends TestCase
{


    /**
    * @expectedException InputException
    */
    public function testIfEmptyInputThenRaisesException() :void
    {
        $output = MoleculeToAtoms::parse_molecule('');
    }


    public function testValidInputReturnsArray() :void
    {
        $output = MoleculeToAtoms::parse_molecule('H');

        $this->assertTrue(is_array($output));
    }

    public function provideSimpleAtom() {
        yield ['H', ['H' => 1]];
        yield ['O', ['O' => 1]];
        yield ['Mg', ['Mg' => 1]];
    }

    /**
    * @dataProvider provideSimpleAtom
    */
    public function testSimpleMoleculeReturnsExpectedOutput($input, $expected) :void
    {
        $output = MoleculeToAtoms::parse_molecule($input);

        $this->assertSame($expected, $output);
    }

    public function provideSimpleMolecules() {
        yield ['O2', ['O' => 2]];
        //yield ['Mg3', ['Mg' => 3]];
    }

    /**
    * @dataProvider provideSimpleMolecules
    */
    public function testMoleculeReturnsExpectedOutput($input, $expected) :void
    {
        $output = MoleculeToAtoms::parse_molecule($input);

        $this->assertSame($expected, $output);
    }

}
