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