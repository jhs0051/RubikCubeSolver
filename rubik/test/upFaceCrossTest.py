'''
Created on April 2, 2023

@author: jonhoustonseibert
'''
import unittest
import rubik.view.solve as solve
from rubik.view.rotate import rotate
from rubik.model.constants import *
from rubik.controller import upFaceCross


class UpFaceCrossTest(unittest.TestCase):

    # Happy Path Tests  
    def test_upFaceCross_000_SolvedCubeShouldReturnOkStatus(self):
        parms = {}
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms['dir'] = 'R'
        
        expectedResult = {}
        expectedResult['status'] = 'ok'

        actualResult = solve.solve(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_upFaceCross_010_SolvedCubeDoesNotContainRotations(self):
        cube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        rotations = ''
        
        expectedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedRotations = ''
        
        actualCube, actualRotations = upFaceCross.solveUpCross(cube, rotations)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_upFaceCross_020_CubeIndexForUpFaceCrossIsInCorrectPosition(self):
        cube = 'rybggggggrgoooooooyoobbbbbbbyyrrrrrryygryygbywwwwwwwww'
        expectedCubeIndex = FML

        actualCubeIndex = upFaceCross._getUpFaceDaisyInCorrectPosition(cube)

        self.assertEqual(expectedCubeIndex, actualCubeIndex)
        
    def test_upFaceCross_040_UpFaceDaisyProducesCorrectSolution(self):
        cube = 'rybggggggrgoooooooyoobbbbbbbyyrrrrrryygryygbywwwwwwwww'

        expectedSolution = 'UUUFRUrufFRUruf'
        expectedCube = 'ybrggggggggyoooooobrgbbbbbboobrrrrrryyryyyoyywwwwwwwww'

        actualCube, actualsolution = upFaceCross._makeUpFaceDaisy(cube, '')

        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedSolution, actualsolution)
        
    def test_upFaceCross_050_SolveUpFaceCross(self):
        cubes = ['orbyrrrrrrgoggggggyrroooooogyybbobbbyygbyybbywwwwwwwww',
                 'U2ig99iU9F9iUgFUiFggF92F92292F2FUgg2U99gUi2U2gFgiiFUii',
                 'kauEgkaEkEavvukggkkkgaauEEavuaakguvuugavEvEEgvuvgvuEkg',
                 'cxlM9MM9c99Kclx9Kc9Kc9MxlKKllxcxxllKMMxcclMKKxcxMK9Ml9',
                 'C0hhXX0XC22CC2C22h22y20000hhyXyyy2yyX00CChyhXChXXhX0Cy',
                 'm22wwmBwmwBBQ2Bw5w2mQ2Q5BQQ2mQmm2m5m5BQwBQB55wB5w5Q522']
        for cube in cubes:
            parms = {}
            parms['op'] = 'solve'
            parms['cube'] = cube

            expectResult = {}
            expectResult['status'] = 'ok'

            actualResult = solve.solve(parms)

            rotatedCube = {}
            rotatedCube['cube'] = parms.get('cube')
            rotatedCube['dir'] = actualResult.get('solution')
            actualCube = rotate(rotatedCube).get('cube')

            bottomCubeColors = actualCube[DTL] is actualCube[DTM] is actualCube[DTR] is actualCube[DML] is actualCube[
                DMM] \
                               is actualCube[DMR] is actualCube[DBL] is actualCube[DBM] is actualCube[DBR]
            frontCubeColors = actualCube[FML] is actualCube[FMM] is actualCube[FMR] is actualCube[FBL] is actualCube[
                FBM] \
                              is actualCube[FBR]
            rightCubeColors = actualCube[RML] is actualCube[RMM] is actualCube[RMR] is actualCube[RBL] is actualCube[
                RBM] \
                              is actualCube[RBR]
            backCubeColors = actualCube[BML] is actualCube[BMM] is actualCube[BMR] is actualCube[BBL] is actualCube[BBM] \
                             is actualCube[BBR]
            leftCubeColors = actualCube[LML] is actualCube[LMM] is actualCube[LMR] is actualCube[LBL] is actualCube[LBM] \
                             is actualCube[LBR]
            upFaceCrossColors = actualCube[UTM] is actualCube[UML] is actualCube[UMM] is actualCube[UMR] is actualCube[UBM]

            self.assertTrue(bottomCubeColors)
            self.assertTrue(frontCubeColors)
            self.assertTrue(rightCubeColors)
            self.assertTrue(backCubeColors)
            self.assertTrue(leftCubeColors)
            self.assertTrue(upFaceCrossColors)
            self.assertEqual(expectResult.get('status'), actualResult.get('status'))