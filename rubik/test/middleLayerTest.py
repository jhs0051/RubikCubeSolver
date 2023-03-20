'''
Created on March 19, 2023

@author: jonhoustonseibert
'''
import unittest
import rubik.view.solve as solve
import rubik.controller.middleLayer as middleLayer
from rubik.view.rotate import _rotate
from rubik.model.constants import *
from rubik.controller import middleLayer


class MiddleLayerTest(unittest.TestCase):

    # Happy Path Tests  
    def test_middleLayer_000_SolvedCubeShouldReturnOkStatus(self):
        parms = {}
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms['dir'] = 'R'
        
        expectedResult = {}
        expectedResult['status'] = 'ok'

        actualResult = solve._solve(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_bottomLayer_010_SolvedCubeDoesNotContainRotations(self):
        cube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        rotations = ''
        
        expectedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedRotations = ''
        
        actualCube, actualRotations = middleLayer._solveMiddleLayer(cube, rotations)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_bottomLayer_020_CubeIndexProducesCorrectRotationList(self):
        cube = 'gggbbbgggrororororbbbgggbbbororororowwwyyywwwyyywwwyyy'
        cubeIndex = RTM

        expectedCube = 'gwobbbgggwgrorororbroyggbbbggwrororowywoywrbbyyywwwyyy'
        expectedsolution = 'UBuburUR'

        actualCube, actualSolution = middleLayer._rotateMiddlePieceFromTopToMiddle(cube, cubeIndex)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedsolution, actualSolution)
        
    def test_bottomLayer_030_CubeIndexProducesCorrectRotationListWhenMiddleIsAllignedWithTopColor(self):
        cube = 'gggbbbgggrororororbbbgggbbborororowowrwyyywwwyyywwwyyy'
        cubeIndex = BTM

        expectedCube = 'woobbbgggggrorrrorbrwbggbbbgyororoworywoywbgwyyywwwyyy'
        expectedsolution = 'urURUBub'

        actualCube, actualSolution = middleLayer._rotateMiddlePieceFromTopToMiddle(cube, cubeIndex)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedsolution, actualSolution)
        
    def test_bottomLayer_040_CubeIndexProducesCorrectCubeIndexToRotateMiddlePieceToTopPiece(self):
        cube = 'gggbbbgggrororororbbbgggbbbororororowwwyyywwwyyywwwyyy'
        location = BMR

        expectedCube = 'rrwbbbgggrygorororwobggbbbboggwororowyowyrwgbyyywwwyyy'
        expectedLocation = FTM

        actualCube, actualLocation, _ = middleLayer._rotateMiddlePieceFromMiddleToTop(cube, location)

        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedLocation, actualLocation)
        