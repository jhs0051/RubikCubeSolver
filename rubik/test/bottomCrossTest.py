import unittest
import rubik.view.solve as solve
import rubik.controller.bottomCross as bottomCross


class BottomCrossTest(unittest.TestCase):

    # Happy Path Tests  
    def test_bottomCross_010_SolvedCubeShouldReturnOkStatus(self):
        parms = {}
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms['dir'] = 'R'
        
        expectedResult = {}
        expectedResult['status'] = 'ok'

        actualResult = bottomCross.solveBottomCross(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))