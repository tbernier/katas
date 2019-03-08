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
        //yield ['H(OH)2', 'HOHOH'];
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
        yield ['(OH)2', 'OHOH'];
        yield ['OH', ''];
        //yield ['H(OH)2', 'OH'];

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

    public function provideFactoredMolecules() {
        yield ['(OH)2', ['O' => 2, 'H' => 2]];
        yield ['(OH)3', ['O' => 3, 'H' => 3]];
        //yield ['H(OH)2', ['O' => 2, 'H' => 3]];
    }

    /**
    * @dataProvider provideFactoredMolecules
    */
    public function testFactoredMoleculeReturnsExpectedOutput($input, $expected) :void
    {
        $moleculeToAtoms = new MoleculeToAtoms();
        $output = $moleculeToAtoms->parse_molecule($input);

        $this->assertSame($expected, $output);
    }

    public function provideFactoredMoleculesToGetDistributedPart() {
        yield [['OH', 2], 'OHOH'];
        yield [['OMg', 3], 'OMgOMgOMg'];
        yield [['OMg', 1], 'OMg'];
        yield [['O2', 2], 'O2O2'];
    }

    /**
    * @dataProvider provideFactoredMoleculesToGetDistributedPart
    */
    public function testGetDistributedPartReturnsExpectedOutput($input, $expected) :void
    {
        $moleculeToAtoms = new MoleculeToAtoms();
        $output = $moleculeToAtoms->getDistributedPart($input[0], $input[1]);

        $this->assertSame($expected, $output);
    }
}
