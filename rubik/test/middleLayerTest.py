'''
Created on March 19, 2023

@author: jonhoustonseibert
'''
import unittest
import rubik.view.solve as solve
import rubik.controller.middleLayer as middleLayer
from rubik.view.rotate import _rotate
from rubik.model.constants import *


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