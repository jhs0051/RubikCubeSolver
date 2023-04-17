from unittest import TestCase
from rubik.view.rotate import rotate
from rubik.model.constants import *
from rubik.view.solve import solve, _getIntegrity
 

class SolveTest(TestCase):
    # Happy Path
    def test010_solve_Integrity(self):
        parms = {}
        parms['cube'] = 'ccpattYcpYaaYaatcYotaoootcocYtppYpptopYoYtaaoapcYcoctp'

        actualResult = solve(parms)

        theCube = parms.get('cube')
        solution = actualResult.get('solution')

        expectedToken = '16551a2ef32869f249f2994d5456a7cad0b946f0578de0cd65806d27b6f689d0'

        actualToken = _getIntegrity(theCube, solution)
        self.assertIn(actualToken, expectedToken)
        
    def test020_solve_Integrity(self):
        parms = {}
        parms['cube'] = 'poap344343343aOOaoaaaoo3poo4OOaOOOpO3oo44O34p3poap4ppa'

        actualResult = solve(parms)

        theCube = parms.get('cube')
        solution = actualResult.get('solution')

        expectedToken = '3756408d941c9ec075be1127fa9b06e16cfe1242de2c785043d3a7d9470c173d'

        actualToken = _getIntegrity(theCube, solution)
        self.assertIn(actualToken, expectedToken)
        
    def test030_unsolvedCubesFromIteration1AreFullySolved(self):
        cubes = ['Q5KQQKQfftQKtfyyyQ5f5KKfytfK55Ktf5tyfytQyttKyt5K55QQyf',
                 '33vvvyDrrtDyDrtyrrDvvv3vv3tDDtDDy33ytrvty3rrr3t3ytyDty',
                 'cXEdrXrrXr1cr1E1EX1cdXd1ddXEd1dEXr1EcrdEcrr1cXEdcXc1cE',
                 'dVVdTTTVWeTVddTedVlVelVVeeVTeWeelWedlddWlWTlllWTTWWdlW',
                 'GGAA9LL9ALkaAAAkLL9aAkLLa99G9akaGkGA9GGkGaLLGkA99kaaak',
                 'zooz3I33myzImzm3z33yz3o3zmoyIIzmoIoIo3zoIyoymmIymyImyy',
                 'yQhhnh8nh00yyy8008QyhQ8nQynyQ8h000hQnnn0Q8hy8yQn8hnQ80',
                 'xx3IFFII444PPPxFFPF3I333FFPFI3Ixx33xx4IP4P44P3FxPIxI44',
                 '70h0qGhGqGGGzz77hzqz7hh00qhGzqz770q0hqzhG70hz7qG70Gz0q',
                 'OoNbbNNbPbiOiNNbObiiioOOPiObNiPPPPPoNbNOiOPboONoooooPi',
                 'UU66UUKYi0KiiY0KKYKK6iKYU6YKYii00iU60iYU6Y00UY606i0UK6',
                 'IMMIMiMiMIMIufiImfmImfimumifIufIuuufiMimmuifumImfuifMM',
                 'ggt88I8c8gIIcIcII8ttqgcqqtgI8c8ggqggccctq8qqctqtttq8II'
                ]
        for cube in cubes:
            parms = {}
            parms['op'] = 'solve'
            parms['cube'] = cube

            expectResult = {}
            expectResult['status'] = 'ok'

            actualResult = solve(parms)

            rotatedCube = {}
            rotatedCube['cube'] = parms.get('cube')
            rotatedCube['dir'] = actualResult.get('solution')
            actualCube = rotate(rotatedCube).get('cube')

            cubeFaces = {
                "bottom": [DTL, DTM, DTR, DML, DMM, DMR, DBL, DBM, DBR],
                "front": [FTL, FTM, FTR, FML, FMM, FMR, FBL, FBM, FBR],
                "right": [RTL, RTM, RTR, RML, RMM, RMR, RBL, RBM, RBR],
                "back": [BTL, BTM, BTR, BML, BMM, BMR, BBL, BBM, BBR],
                "left": [LTL, LTM, LTR, LML, LMM, LMR, LBL, LBM, LBR],
                "up": [UTL, UTM, UTR, UML, UMM, UMR, UBL, UBM, UBR],
            }

            for cubeFaces, cubeIndexes in cubeFaces.items():
                faceColors = [actualCube[cubeIndex] for cubeIndex in cubeIndexes]
                self.assertTrue(all(color is faceColors[FTL] for color in faceColors))

            self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
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
