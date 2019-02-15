<?php

use PHPUnit\Framework\TestCase;

final class MoleculeToAtomsTest extends TestCase
{


    /**
    * @expectedException InputException
    */
    public function testIfEmptyInputThenRaisesException() :void
    {
        $moleculeToAtoms = new MoleculeToAtoms();
        $output = $moleculeToAtoms->parse_molecule('');
    }


    public function testValidInputReturnsArray() :void
    {
        $moleculeToAtoms = new MoleculeToAtoms();
        $output = $moleculeToAtoms->parse_molecule('H');

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
        $moleculeToAtoms = new MoleculeToAtoms();
        $output = $moleculeToAtoms->parse_molecule($input);

        $this->assertSame($expected, $output);
    }

    public function provideSimpleMolecules() {
        yield ['O2', ['O' => 2]];
        yield ['Mg3', ['Mg' => 3]];
        yield ['Mg3O2', ['Mg' => 3, 'O' => 2]];
        yield ['Mg3O2CaCO3', ['Mg' => 3, 'O' => 5, 'Ca' => 1, 'C' => 1]];
        yield ['O2OO3O4', ['O' => 10]];
        yield ['OOOOOOOOOO', ['O' => 10]];
    }

    /**
    * @dataProvider provideSimpleMolecules
    */
    public function testMoleculeReturnsExpectedOutput($input, $expected) :void
    {
        $moleculeToAtoms = new MoleculeToAtoms();
        $output = $moleculeToAtoms->parse_molecule($input);

        $this->assertSame($expected, $output);
    }

}
