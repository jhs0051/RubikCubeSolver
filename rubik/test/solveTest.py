from unittest import TestCase
from rubik.view.solve import solve, _getIntegrity
 

class SolveTest(TestCase):
    # Happy Path
    def test010_solve_Integrity(self):
        parms = {}
        parms['cube'] = 'ccpattYcpYaaYaatcYotaoootcocYtppYpptopYoYtaaoapcYcoctp'

        actualResult = solve(parms)

        theCube = parms.get('cube')
        solution = actualResult.get('solution')

        expectedToken = 'ff5377269c54c452a6070de1c72b2dc47947ff48f01c2a598f0b7864a88b4b9c'

        actualToken = _getIntegrity(theCube, solution)
        self.assertIn(actualToken, expectedToken)
        
    '''def test020_solve_Integrity(self):
        parms = {}
        parms['cube'] = 'poap344343343aOOaoaaaoo3poo4OOaOOOpO3oo44O34p3poap4ppa'

        actualResult = solve(parms)

        theCube = parms.get('cube')
        solution = actualResult.get('solution')

        expectedToken = 'e6d515a906d2765ad1c9c74f4cc2be8a6e2f86833c3be5103ceccad3f84c8abd'

        actualToken = _getIntegrity(theCube, solution)
        self.assertIn(actualToken, expectedToken)'''
        
    # Sad Path
    def test900_solve_ErrorOnShortCube(self):
        parms = {}
        parms['cube'] = 'w5i1w5i1S1iwa5iaSSSi1aa5iw15wSSia5waw1i5'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test910_solve_ErrorOnLongCube(self):
        parms = {}
        parms['cube'] = 'PFUPFPLrL2rFUrrFPrrLL2PL22UUULrU222FPU2F2FrLPUPrFLLFUPPFUPFPLrL2rFUrrFPrrLL2PL22UUULrU222FPU2F2FrLPU'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test920_solve_ErrorOnCubeWithIllegalCharacters(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbb*********rrrrrrrrroooooooooyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test930_solve_ErrorOnMoreThan9OfAColor(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwb'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test940_solve_ErrorOnNonUniqueMiddleCharacter(self):
        parms = {}
        parms['cube'] = 'rbbbbbbbbrrrrbrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test950_solve_ErrorOnInvalidKey(self):
        parms = {}
        parms['cube'] = 'ogwwrywybgyrgbgrrwoogbgwyrworyryggwbbbyyowgobroobwoybr'
        parms['extra'] = 'key'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid key', result['status'])
        
    def test_bottomCross_960_ErrorOnEmptyString(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = ''

        expectResult = {}
        expectResult['status'] = 'error: cube can not be empty'

        actualResult = solve(parms)
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
