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
        parms = {'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'dir': 'R'}

        expectedResult = {'status': 'ok'}

        actualResult = solve.solve(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_upperLayer_010_upperLayerNotSolvedReturnsFalse(self):
        cubes = [ 'orbyrrrrrrgoggggggyrroooooogyybbobbbyygbyybbywwwwwwwww',
                  'llKllkklleexxxKJkKJkKxkkxKkkxxJexeKKeKkJKJJelxJeeJeJll',
                  'dPNfdttffffN55Pt55dtPNPPNd5ffttfNPN5tdfPtt55PPdddNNN5d',
                  'uG3Uuu3YYUG8333uU3YYG888uU8YGUGG8Guu833YYUGu8U8GYUuU3Y',
                  'O5rFor5rgooForO5gOO5rgOogOFO55Fgggro5rrg55gOFrFoOFooFF',
                  '45G44D344EDDG55G45433DEE3EDEE5DGG5E4GGGG34D3D5333D5E5E',
                  'sjssjjbbjKSKKKbSjbsKSSQQQSSKsjKbjKbQjsjQsQbSQSsbQSbQKs',
                  'aJ0LJJa0MMaMMqMLLLLa00aaqa0q000MMMLLJMaJLqqqaqqJq0JJLJ',
                  'GEPETFPFFFGnPnPnnPETPGFPFEnGFTTPPFTTTnTnEFnnGEEEGGGGTE',
                  'sjjJPPJsPPxxJjAAjsPsJPsjxAjPsJJAAxAAAxjJxPjPJsjxsJxsxA'
                ]

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
                 'bbbrrrrrrrogggggggoroooooooggrbbbbbbyyyyyyyyywwwwwwwww',
                 'rrrbbbbbggobrrrrrrogoggggggbbbooooooyyyyyyyyywwwwwwwww'
                ]

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

        expectedResult = 1

        actualResult = upperLayer._alignTopRow(cube)
        self.assertEqual(expectedResult, actualResult)
        
    def test_upperLayer_035_AlignedTopMiddleFaceRowProduces2(self):
        cube = 'NNNGlNTlG444444AAAllGTTGlGlAl4AATGANlTNGGGTNTA4TlNT4AN'

        expectedResult = 2

        actualResult = upperLayer._alignTopRow(cube)
        self.assertEqual(expectedResult, actualResult)
        
    def test_upperLayer_035_1_AlignedTopRightFaceRowProduces3(self):
        cube = 'NTGGlNTlG444444AAAllGTTGlNlAl4AATGANlNNGGGTNTA4TlNT4AN'

        expectedResult = 3

        actualResult = upperLayer._alignTopRow(cube)
        self.assertEqual(expectedResult, actualResult)
        
    def test_upperLayer_035_2_NotAlignedTopFaceRowProduces0(self):
        cube = 'orrbbbbbbgobrrrrrrrgoggggggbbgooooooyyyyyyyyywwwwwwwww'

        expectedResult = 0

        actualResult = upperLayer._alignTopRow(cube)
        self.assertEqual(expectedResult, actualResult)
        
    def test_upperLayer_040_TopLayerSolvedWithMatchingSidesReturnsTrue(self): 
        cube = 'ggggrggggrrrrrrgrrbbbbbbobbooooobooowwwwywwwwyyyyyywyy'

        expectedResult = True

        actualResult = upperLayer._doTopLayerSidesMatch(cube)
        self.assertEqual(expectedResult, actualResult) 
        
    def test_upperLayer_045_TopLayerNotSolvedWithNonMatchingSidesReturnsFalse(self): 
        cube = 'NTGGlNTlG444444AAAllGTTGlNlAl4AATGANlNNGGGTNTA4TlNT4AN'

        expectedResult = False

        actualResult = upperLayer._doTopLayerSidesMatch(cube)
        self.assertEqual(expectedResult, actualResult)
        
    def test_upperLayer_050_RotateTopEdgeProducesRotationsToSolveTopEdges(self): 
        cube = 'orrbbbbbbgobrrrrrrrgoggggggbbgooooooyyyyyyyyywwwwwwwww'
        rotations = ''

        expectedCube = 'rorbbbbbbgggrrrrrroboggggggbrbooooooyyyyyyyyywwwwwwwww'
        expectedRotations = 'rFrBBRfrBBRRUrFrBBRfrBBRR'

        actualCube, actualRotations = upperLayer._rotateTopEdge(cube, rotations)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_upperLayer_055_RotateTopEdgeProducesRotationsToSolveTopEdges(self): 
        cube = 'gbbrrrrrrrogggggggorooooooobgrbbbbbbyyyyyyyyywwwwwwwww'
        rotations = ''

        expectedCube = 'gbgrrrrrroooggggggbrboooooorgrbbbbbbyyyyyyyyywwwwwwwww'
        expectedRotations = 'rFrBBRfrBBRR'

        actualCube, actualRotations = upperLayer._rotateTopEdge(cube, rotations)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_upperLayer_055_1_RotateTopEdgeWithAlreadySolvedTopLayerProducesEmptyRotations(self): 
        cube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        rotations = ''

        expectedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedRotations = ''

        actualCube, actualRotations = upperLayer._rotateTopEdge(cube, rotations)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_upperLayer_060_AlignedTopLeftFaceEdgePiecesProduces1(self):
        cube = 'rrrbbbbbggobrrrrrrogoggggggbbbooooooyyyyyyyyywwwwwwwww'

        expectedResult = 1

        actualResult = upperLayer._alignTopEdgePieces(cube)
        self.assertEqual(expectedResult, actualResult)
        
    def test_upperLayer_065_AlignedTopMiddleFaceEdgePiecesProduces2(self):
        cube = 'NNNGlNTlG444444AAAllGTTGlGlAl4AATGANlTNGGGTNTA4TlNT4AN'

        expectedResult = 2

        actualResult = upperLayer._alignTopRow(cube)
        self.assertEqual(expectedResult, actualResult)
        
    def test_upperLayer_065_1_AlignedTopRightFaceEdgePiecesProduces3(self):
        cube = 'NTGGlNTlG444444AAAllGTTGlNlAl4AATGANlNNGGGTNTA4TlNT4AN'

        expectedResult = 3

        actualResult = upperLayer._alignTopRow(cube)
        self.assertEqual(expectedResult, actualResult)
        
    def test_upperLayer_065_2_NotAlignedTopEdgesProduces0(self):
        cube = 'orrbbbbbbgobrrrrrrrgoggggggbbgooooooyyyyyyyyywwwwwwwww'

        expectedResult = 0

        actualResult = upperLayer._alignTopRow(cube)
        self.assertEqual(expectedResult, actualResult)
        
    def test_upperLayer_070_RotateTopRowProducesRotationsToSolveTopRow(self): 
        cube = 'rbrrrrrrrorooooooogggggggggbobbbbbbbwwwwwwwwwyyyyyyyyy'
        rotations = ''

        expectedCube = 'rrrrrrrrrooooooooogggggggggbbbbbbbbbwwwwwwwwwyyyyyyyyy'
        expectedRotations = 'RuRURURuruRRRuRURURuruRR'

        actualCube, actualRotations = upperLayer._rotateTopRow(cube, rotations)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_upperLayer_075_RotateTopRowProducesRotationsToSolveTopRow(self): 
        cube = 'yyybbbbbbroroooooobrbyyyyyyoborrrrrrwwwwwwwwwggggggggg'
        rotations = ''

        expectedCube = 'bbbbbbbbboooooooooyyyyyyyyyrrrrrrrrrwwwwwwwwwggggggggg'
        expectedRotations = 'UURuRURURuruRRRuRURURuruRR'

        actualCube, actualRotations = upperLayer._rotateTopRow(cube, rotations)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_upperLayer_075_1_RotateTopRowWithAlreadySolvedTopLayerProducesEmptyRotations(self): 
        cube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        rotations = ''

        expectedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedRotations = ''

        actualCube, actualRotations = upperLayer._rotateTopRow(cube, rotations)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_upperLayer_080_SolveUpperLayerProducesSameSolutionAsComponents(self): 
        cube = 'yyybbbbbbroroooooobrbyyyyyyoborrrrrrwwwwwwwwwggggggggg'
        rotations = ''

        expectedCube = 'bbbbbbbbboooooooooyyyyyyyyyrrrrrrrrrwwwwwwwwwggggggggg'
        expectedRotations = 'UURuRURURuruRRRuRURURuruRR'

        actualCube, actualRotations = upperLayer.solveUpperLayer(cube, rotations)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_upperLayer_085_SolveUpperLayerProducesRotationsToSolveCube(self): 
        cube = 'gbbrrrrrrrogggggggorooooooobgrbbbbbbyyyyyyyyywwwwwwwww'
        rotations = ''

        expectedCube = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        expectedRotations = 'rFrBBRfrBBRRUUURuRURURuruRR'

        actualCube, actualRotations = upperLayer.solveUpperLayer(cube, rotations)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_upperLayer_090_SolveTopLayer(self):
        cubes = ['orbyrrrrrrgoggggggyrroooooogyybbobbbyygbyybbywwwwwwwww',
                 'U2ig99iU9F9iUgFUiFggF92F92292F2FUgg2U99gUi2U2gFgiiFUii',
                 'kauEgkaEkEavvukggkkkgaauEEavuaakguvuugavEvEEgvuvgvuEkg',
                 'cxlM9MM9c99Kclx9Kc9Kc9MxlKKllxcxxllKMMxcclMKKxcxMK9Ml9',
                 'C0hhXX0XC22CC2C22h22y20000hhyXyyy2yyX00CChyhXChXXhX0Cy',
                 'm22wwmBwmwBBQ2Bw5w2mQ2Q5BQQ2mQmm2m5m5BQwBQB55wB5w5Q522'
                ]
        for cube in cubes:
            parms = {'op': 'solve', 'cube': cube}

            expectedResult = {'status': 'ok'}

            actualResult = solve.solve(parms)

            rotatedCube = {'cube': parms.get('cube'), 'dir': actualResult.get('solution')}
            actualCube = rotate(rotatedCube).get('cube')

            cubeFaces = {
                "Bottom Face":  [DTL, DTM, DTR, DML, DMM, DMR, DBL, DBM, DBR],
                "Front  Face":  [FTL, FTM, FTR, FML, FMM, FMR, FBL, FBM, FBR],
                "Right  Face":  [RTL, RTM, RTR, RML, RMM, RMR, RBL, RBM, RBR],
                "Back   Face":  [BTL, BTM, BTR, BML, BMM, BMR, BBL, BBM, BBR],
                "Left   Face":  [LTL, LTM, LTR, LML, LMM, LMR, LBL, LBM, LBR],
                "Up     Face":  [UTL, UTM, UTR, UML, UMM, UMR, UBL, UBM, UBR]
            }

            for cubeFaces, cubeIndexes in cubeFaces.items():
                faceColors = [actualCube[cubeIndex] for cubeIndex in cubeIndexes]
                self.assertTrue(all(color is faceColors[FTL] for color in faceColors))

            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            