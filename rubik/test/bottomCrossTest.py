import unittest
import rubik.view.solve as solve
import rubik.controller.bottomCross as bottomCross


class BottomCrossTest(unittest.TestCase):

    # Happy Path Tests  
    # Saving to end of iteration
    """def test_bottomCross_010_SolvedCubeShouldReturnOkStatus(self):
        parms = {}
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms['dir'] = 'R'
        
        expectedResult = {}
        expectedResult['status'] = 'ok'

        actualResult = bottomCross.solveBottomCross(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))"""
        
    def test_bottomCross_010_SolvedCubeContainsASolvedDaisyPattern(self):
        cube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        
        expectedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedRotations = ''
        
        actualCube, actualRotations = bottomCross.solveBottomCross(cube, '')
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)