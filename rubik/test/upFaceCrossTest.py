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