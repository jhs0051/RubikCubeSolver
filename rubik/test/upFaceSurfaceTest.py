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
        
    '''def test_upFaceSurface_020_TestEdgePiecesMatch(self):
        cube = 'rybggggggrgoooooooyoobbbbbbbyyrrrrrryygryygbywwwwwwwww'
        rotations = ''

        expectedCube = 'oyoggggggbgroooooogobbbbbbbrygrrrrrryyyryyybywwwwwwwww'
        expectedSolution = 'RUrURUUrRUrURUUrRUrURUUr'

        actualCube, actualSolution = upFaceSurface._solveUpFaceEdgePieces(cube, rotations)

        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedSolution, actualSolution)'''
        
    def test_upFaceSurface_030_AreUpEdgePiecesSolved(self):
        cube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'

        actualResult = upFaceSurface._doUpFaceEdgePiecesMatch(cube)

        self.assertTrue(actualResult)
        