'''
Created on April 2, 2023

@author: jonhoustonseibert
'''
import unittest
import rubik.view.solve as solve
from rubik.view.rotate import rotate
from rubik.model.constants import *
from rubik.controller import upFaceSurface


class UpFaceSurfaceTest(unittest.TestCase):

    # Happy Path Tests  
    def test_upFaceSurface_000_SolvedCubeShouldReturnOkStatus(self):
        parms = {}
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms['dir'] = 'R'
        
        expectedResult = {}
        expectedResult['status'] = 'ok'

        actualResult = solve.solve(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_upFaceSurface_010_SolvedCubeDoesNotContainRotations(self):
        cube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        rotations = ''
        
        expectedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedRotations = ''
        
        actualCube, actualRotations = upFaceSurface.solveUpSurface(cube, rotations)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_upFaceSurface_020_TestEdgePiecesMatch(self):
        cube = 'rybggggggrgoooooooyoobbbbbbbyyrrrrrryygryygbywwwwwwwww'
        rotations = ''

        expectedCube = 'oyoggggggbgroooooogobbbbbbbrygrrrrrryyyryyybywwwwwwwww'
        expectedSolution = 'RUrURUUrRUrURUUrRUrURUUr'

        actualCube, actualSolution = upFaceSurface._solveUpFaceEdgePieces(cube, rotations)

        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedSolution, actualSolution)
        
    def test_upFaceSurface_030_AreUpEdgePiecesSolved(self):
        cube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'

        actualResult = upFaceSurface._doUpFaceEdgePiecesMatch(cube)

        self.assertTrue(actualResult)
        
    def test_upFaceCross_050_SolveUpFaceSurface(self):
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
            upFaceSurfaceColors = actualCube[UTL] is actualCube[UTR] is actualCube[UBL] is actualCube[UBR]
            
            self.assertTrue(bottomCubeColors)
            self.assertTrue(frontCubeColors)
            self.assertTrue(rightCubeColors)
            self.assertTrue(backCubeColors)
            self.assertTrue(leftCubeColors)
            self.assertTrue(upFaceCrossColors)
            self.assertTrue(upFaceSurfaceColors)
            self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        