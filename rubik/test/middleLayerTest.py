'''
Created on March 19, 2023

@author: jonhoustonseibert
'''
import unittest
import rubik.view.solve as solve
from rubik.view.rotate import rotate
from rubik.model.constants import *
from rubik.controller import middleLayer


class MiddleLayerTest(unittest.TestCase):

    # Happy Path Tests  
    def test_middleLayer_000_SolvedCubeShouldReturnOkStatus(self):
        parms = {'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'dir': 'R'}

        expectedResult = {'status': 'ok'}

        actualResult = solve.solve(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_middleLayer_010_SolvedCubeDoesNotContainRotations(self):
        cube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        rotations = ''
        
        expectedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedRotations = ''
        
        actualCube, actualRotations = middleLayer.solveMiddleLayer(cube, rotations)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_middleLayer_020_CubeIndexProducesCorrectRotationList(self):
        cube = 'gggbbbgggrororororbbbgggbbbororororowwwyyywwwyyywwwyyy'
        cubeIndex = RTM

        expectedCube = 'gwobbbgggwgrorororbroyggbbbggwrororowywoywrbbyyywwwyyy'
        expectedSolution = 'UBuburUR'

        actualCube, actualSolution = middleLayer._rotateMiddlePieceFromTopToMiddle(cube, cubeIndex)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedSolution, actualSolution)
        
    def test_middleLayer_030_CubeIndexProducesCorrectRotationListWhenMiddleIsAllignedWithTopColor(self):
        cube = 'gggbbbgggrororororbbbgggbbborororowowrwyyywwwyyywwwyyy'
        cubeIndex = BTM

        expectedCube = 'woobbbgggggrorrrorbrwbggbbbgyororoworywoywbgwyyywwwyyy'
        expectedSolution = 'urURUBub'

        actualCube, actualSolution = middleLayer._rotateMiddlePieceFromTopToMiddle(cube, cubeIndex)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedSolution, actualSolution)
        
    def test_middleLayer_040_CubeIndexProducesCorrectCubeIndexToRotateMiddlePieceToTopPiece(self):
        cube = 'gggbbbgggrororororbbbgggbbbororororowwwyyywwwyyywwwyyy'
        cubeIndex = BMR

        expectedCube = 'rrwbbbgggrygorororwobggbbbboggwororowyowyrwgbyyywwwyyy'
        expectedCubeIndex = FTM

        actualCube, actualCubeIndex, actualSolution = middleLayer._rotateMiddlePieceFromMiddleToTop(cube, cubeIndex)

        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedCubeIndex, actualCubeIndex)
        
    def test_middleLayer_050_CubeIndexProducesCorrectCubeIndexToMatchTopEdgePieceWithCorrespondingPiece(self):
        cube = 'oyyogrgggrgwwwyyrbbgwbbryobrwwyyboorbrobowgggwooyrbywr'
        cubeIndex = BTM

        expectedCube = 'bgwogrgggrwwwwyyrboyybbryobrgwyyboorgggwoborbwooyrbywr'
        expectedCubeIndex = FTM
        expectedSolution = 'UU'

        actualCube, actualCubeIndex, actualSolution = middleLayer._alignEdgePieceWithAnotherTopPiece(cube, cubeIndex)

        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedCubeIndex, actualCubeIndex)
        self.assertEqual(expectedSolution, actualSolution)
        
    def test_middleLayer_060_CubeIndexProducesNoRotationsToMatchTopEdgePieceWithCorrespondingPiece(self):
        cube = 'bbbbbbgggoroorororggggggbbbrorrororowwwyyywwwyyywwwyyy'
        cubeIndex = FTM

        expectedCube = 'bbbbbbgggoroorororggggggbbbrorrororowwwyyywwwyyywwwyyy'
        expectedCubeIndex = FTM
        expectedSolution = ''

        actualCube, actualCubeIndex, actualSolution = middleLayer._alignEdgePieceWithAnotherTopPiece(cube, cubeIndex)

        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedCubeIndex, actualCubeIndex)
        self.assertEqual(expectedSolution, actualSolution)
        
    def test_middleLayer_070_CubeIndexMatchesExpectedCubeIndex(self):
        cube = 'gggbbbgggrororororbbbgggbbborororowowrwyyywwwyyywwwyyy'

        expectedCubeIndex = BTM

        actualCubeIndex = middleLayer._matchCenterMiddlePieceWithOtherMiddleCenters(cube)

        self.assertEqual(expectedCubeIndex, actualCubeIndex)
        
    def test_middleLayer_080_CubeIndexMatchesExpectedCubeIndex(self):
        cube = 'gggbbbgggrororororbbbgggbbborororowowrwyyywwwyyywwwyyy'

        expectedCubeIndex = FMR

        actualCubeIndex = middleLayer._alignCenterMiddlePieceWithEdgeMiddlePieces(cube)

        self.assertEqual(expectedCubeIndex, actualCubeIndex)
        
    def test_middleLayer_090_CubeProducesRotationsToSolveMiddleLayer(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = 'orbyrrrrrrgoggggggyrroooooogyybbobbbyygbyybbywwwwwwwww'
        cube, rotations = parms['cube'], ''

        expectedResult = {}
        expectedRotations = 'ulULUFuf'
        expectedResult['status'] = 'ok'

        actualCube, actualRotations = middleLayer.solveMiddleLayer(cube, rotations)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_middleLayer_100_CubeFullySolvesMiddleLayerAndBelow(self):
        cubes = ['ggoorggyygbrooowyobbywywrobwbybbrwrooygrwgbryrwbwggryw',
                 'orgrrwoyrygygbwooorybrgwggbrwwowogrwygwyoogbwrbbyybybb',
                 'brwybbywogoywrwgoyrywggrbrgbwryogoobobgrybwbrroygwywgo',
                 'yyggybgyorgyoorbowrbrwgyywbgrrwwogbowgworrorobbywbywgb',
                 'oyyogrgggrgwwwyyrbbgwbbryobrwwyyboorbrobowgggwooyrbywr',
                 'bgoogogggbgwbwyowrgoybbgbbbrwryyywyogwrbowwoyyrwrrrory']
        for cube in cubes:
            parms = {'op': 'solve', 'cube': cube}
            expectedResult = {'status': 'ok'}

            actualResult = solve.solve(parms)

            rotatedCube = {'cube': parms.get('cube'), 'dir': actualResult.get('solution')}
            actualCube = rotate(rotatedCube).get('cube')

            cubeFaces = {
                "bottom": [DTL, DTM, DTR, DML, DMM, DMR, DBL, DBM, DBR],
                "front": [FML, FMM, FMR, FBL, FBM, FBR],
                "right": [RML, RMM, RMR, RBL, RBM, RBR],
                "back": [BML, BMM, BMR, BBL, BBM, BBR],
                "left": [LML, LMM, LMR, LBL, LBM, LBR]
            }

            for cubeFaces, cubeIndexes in cubeFaces.items():
                faceColors = [actualCube[cubeIndex] for cubeIndex in cubeIndexes]
                self.assertTrue(all(color is faceColors[FTL] for color in faceColors))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
         
    # Sad Path Tests   
    def test_middleLayer_900_FailingCubesNowPass(self):
        cubes = ['bfLfELcLvbcfvbELbEEcbvLbvELLfvLcbfcEfvbLffEEvfccEvvcbc',
                 'VSmVFSSFFUUUUmVemmemUSUeUUmSmmSSUeeFVVSFVmFFVVVSFeeFee',
                 'XxXGJXxJTJxxJxXGGyXyJyGJGJyXyGxyXTGTxGGTTXyTyJyxxXTJTT',
                 'J3x33hh3xhB3xbxJB3BhbbxxJ33hxxBBBBJbxbhJJhbJB3bBbhJJhb'
                 ]
        for cube in cubes:
            parms = {'op': 'solve', 'cube': cube}
            expectedResult = {'status': 'ok'}

            actualResult = solve.solve(parms)

            rotatedCube = {'cube': parms.get('cube'), 'dir': actualResult.get('solution')}
            actualCube = rotate(rotatedCube).get('cube')

            cubeFaces = {
                "Bottom Face": [DTL, DTM, DTR, DML, DMM, DMR, DBL, DBM, DBR],
                "Front  Face": [FML, FMM, FMR, FBL, FBM, FBR],
                "Right  Face": [RML, RMM, RMR, RBL, RBM, RBR],
                "Back   Face": [BML, BMM, BMR, BBL, BBM, BBR],
                "Left   Face": [LML, LMM, LMR, LBL, LBM, LBR]
            }

            for cubeFaces, cubeIndexes in cubeFaces.items():
                faceColors = [actualCube[cubeIndex] for cubeIndex in cubeIndexes]
                self.assertTrue(all(color is faceColors[FTL] for color in faceColors))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        