'''
Created on April 15, 2023

@author: jonhoustonseibert
'''
import unittest
import rubik.view.solve as solve
from rubik.view.rotate import rotate
from rubik.model.constants import *
from rubik.controller import upperLayer


class UpperLayerTest(unittest.TestCase):

    # Happy Path Tests  
    def test_upperLayer_000_SolvedCubeShouldReturnOkStatus(self):
        parms = {}
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms['dir'] = 'R'
        
        expectedResult = {}
        expectedResult['status'] = 'ok'

        actualResult = solve.solve(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_upperLayer_010_upperLayerNotSolvedReturnsFalse(self):
        cubes = ['orbyrrrrrrgoggggggyrroooooogyybbobbbyygbyybbywwwwwwwww',
                 'llKllkklleexxxKJkKJkKxkkxKkkxxJexeKKeKkJKJJelxJeeJeJll',
                 'dPNfdttffffN55Pt55dtPNPPNd5ffttfNPN5tdfPtt55PPdddNNN5d',
                 'uG3Uuu3YYUG8333uU3YYG888uU8YGUGG8Guu833YYUGu8U8GYUuU3Y',
                 'O5rFor5rgooForO5gOO5rgOogOFO55Fgggro5rrg55gOFrFoOFooFF',
                 '45G44D344EDDG55G45433DEE3EDEE5DGG5E4GGGG34D3D5333D5E5E',
                 'sjssjjbbjKSKKKbSjbsKSSQQQSSKsjKbjKbQjsjQsQbSQSsbQSbQKs',
                 'aJ0LJJa0MMaMMqMLLLLa00aaqa0q000MMMLLJMaJLqqqaqqJq0JJLJ',
                 'GEPETFPFFFGnPnPnnPETPGFPFEnGFTTPPFTTTnTnEFnnGEEEGGGGTE',
                 'sjjJPPJsPPxxJjAAjsPsJPsjxAjPsJJAAxAAAxjJxPjPJsjxsJxsxA']

        for cube in cubes:
            expectedResult = False

            actualResult = upperLayer._isTopLayerSolved(cube)
            self.assertEqual(expectedResult, actualResult)
            
    def test_upperLayer_015_upperLayerSolvedReturnsTrue(self):
        cube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult = True

        actualResult = upperLayer._isTopLayerSolved(cube)
        self.assertEqual(expectedResult, actualResult)
        
    def test_upperLayer_020_upperLayerEdgePiecesNotSolvedReturnsFalse(self):
        cubes = ['orrbbbbbbgobrrrrrrrgoggggggbbgooooooyyyyyyyyywwwwwwwww',
                 'bbbrrrrrrrogggggggoroooooooggrbbbbbbyyyyyyyyywwwwwwwww'
                 'rrrbbbbbggobrrrrrrogoggggggbbbooooooyyyyyyyyywwwwwwwww']

        for cube in cubes:

            expectedResult = False

            actualResult = upperLayer._areTopLayerEdgePiecesSolved(cube)
            self.assertEqual(expectedResult, actualResult)
            
    def test_upperLayer_025_upperLayerEdgePieceSolvedReturnsTrue(self):
        cube = 'ogooooooobobbbbbbbrrrrrrrrrgbgggggggyyyyyyyyywwwwwwwww'
        expectedResult = True

        actualResult = upperLayer._areTopLayerEdgePiecesSolved(cube)
        self.assertEqual(expectedResult, actualResult)
        
    def test_upperLayer_030_AlignedTopLeftFaceRowProduces1(self):
        cube = 'rrrbbbbbggobrrrrrrogoggggggbbbooooooyyyyyyyyywwwwwwwww'

        expectResult = 1

        actualResult = upperLayer._alignTopRow(cube)
        self.assertEqual(expectResult, actualResult)
        
        