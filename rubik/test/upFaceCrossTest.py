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
        rotations = ''

        expectedSolution = 'UUUFRUrufFRUruf'
        expectedCube = 'ybrggggggggyoooooobrgbbbbbboobrrrrrryyryyyoyywwwwwwwww'

        actualCube, actualsolution = upFaceCross._makeUpFaceDaisy(cube, rotations)

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

            cubeFaces = {
                "bottom": [DTL, DTM, DTR, DML, DMM, DMR, DBL, DBM, DBR],
                "front": [FML, FMM, FMR, FBL, FBM, FBR],
                "right": [RML, RMM, RMR, RBL, RBM, RBR],
                "back": [BML, BMM, BMR, BBL, BBM, BBR],
                "left": [LML, LMM, LMR, LBL, LBM, LBR],
                "up": [UTM, UML, UMM, UMR, UBM]
            }

            for cubeFaces, cubeIndexes in cubeFaces.items():
                faceColors = [actualCube[cubeIndex] for cubeIndex in cubeIndexes]
                self.assertTrue(all(color is faceColors[FTL] for color in faceColors))

            self.assertEqual(expectResult.get('status'), actualResult.get('status'))