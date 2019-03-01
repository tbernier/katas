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

    public function provideSimpleMoleculesToFlatten() {
        yield ['O2', ['O', 'O']];
        yield ['Mg3', ['Mg', 'Mg', 'Mg']];
        yield ['Mg3O2', ['Mg', 'Mg', 'Mg', 'O', 'O']];
        yield ['Mg3O2CaCO3', ['Mg', 'Mg', 'Mg', 'O', 'O', 'Ca', 'C', 'O', 'O', 'O']];
        yield ['O2OO3O4', ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']];
        yield ['OOOOOOOOOO', ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']];
    }

    /**
    * @dataProvider provideSimpleMoleculesToFlatten
    */
    public function testFlattenMoleculeReturnsExpectedOutput($molecule, $expected) :void
    {
        $moleculeToAtoms = new MoleculeToAtoms();
        $output = $moleculeToAtoms->flattenMolecule($molecule);

        $this->assertSame($expected, $output);
    }

    public function provideFactoredMoleculesToDistribute() {
        yield ['(OH)2', 'OHOH'];
        yield ['OH2', 'OH2'];
    }

    /**
    * @dataProvider provideFactoredMoleculesToDistribute
    */
    public function testDistributeComplexMoleculeReturnsExpectedOutput($molecule, $expected) :void
    {
        $moleculeToAtoms = new MoleculeToAtoms();
        $output = $moleculeToAtoms->distributeMolecule($molecule);

        $this->assertSame($expected, $output);
    }

    public function provideFactoredMoleculesToGetFactoredPart() {
        // yield ['(OH)2', ['factoredPart' => 'OH', 'multiplier' => 2, '']];
        yield ['(OH)2', 'OH'];
        yield ['OH', ''];
        //yield ['Ca(OH)2P', 'CaPOHOH'];
    }

    /**
    * @dataProvider provideFactoredMoleculesToGetFactoredPart
    */
    public function testGetFactoredPartReturnsExpectedOutput($molecule, $expected) :void
    {
        $moleculeToAtoms = new MoleculeToAtoms();
        $output = $moleculeToAtoms->getFactoredPart($molecule);

        $this->assertSame($expected, $output);
    }
}
