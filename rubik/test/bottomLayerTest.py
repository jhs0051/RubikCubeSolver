'''
Created on Feb 28, 2023

@author: jonhoustonseibert
'''
import unittest
import rubik.view.solve as solve
import rubik.controller.bottomLayer as bottomLayer
from rubik.model.constants import *


class BottomLayerTest(unittest.TestCase):

    # Happy Path Tests  
    def test_bottomLayer_000_SolvedCubeShouldReturnOkStatus(self):
        parms = {}
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms['dir'] = 'R'
        
        expectedResult = {}
        expectedResult['status'] = 'ok'

        actualResult = solve.solve(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_bottomLayer_010_SolvedCubeDoesNotContainRotations(self):
        cube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        rotations = ''
        
        expectedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedRotations = ''
        
        actualCube, actualRotations = bottomLayer.solveBottomLayer(cube, rotations)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_bottomCorners_020_TestEdgePieceGetsRotatedToDifferentFaceSameEdge(self):
        cube = 'gggbbbgggrororororbbbgggbbbororororowwwyyywwwyyywwwyyy'
        cubeIndex = BTL

        expectedCube = 'rorbbbgggbbbororororogggbbbgggrororowywwywwywyyywwwyyy'
        expectedsolution = 'U'
        expectedLocation = RTL

        actualCube, currentCubeIndex, actualSolution = bottomLayer.rotateEdgePieceToDifferentFace(cube, cubeIndex)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedLocation, currentCubeIndex)
        self.assertEqual(expectedsolution, actualSolution)