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
        parms = {}
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms['dir'] = 'R'
        
        expectedResult = {}
        expectedResult['status'] = 'ok'

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
        expectedsolution = 'UBuburUR'

        actualCube, actualSolution = middleLayer._rotateMiddlePieceFromTopToMiddle(cube, cubeIndex)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedsolution, actualSolution)
        
    def test_middleLayer_030_CubeIndexProducesCorrectRotationListWhenMiddleIsAllignedWithTopColor(self):
        cube = 'gggbbbgggrororororbbbgggbbborororowowrwyyywwwyyywwwyyy'
        cubeIndex = BTM

        expectedCube = 'woobbbgggggrorrrorbrwbggbbbgyororoworywoywbgwyyywwwyyy'
        expectedsolution = 'urURUBub'

        actualCube, actualSolution = middleLayer._rotateMiddlePieceFromTopToMiddle(cube, cubeIndex)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedsolution, actualSolution)
        
    def test_middleLayer_040_CubeIndexProducesCorrectCubeIndexToRotateMiddlePieceToTopPiece(self):
        cube = 'gggbbbgggrororororbbbgggbbbororororowwwyyywwwyyywwwyyy'
        location = BMR

        expectedCube = 'rrwbbbgggrygorororwobggbbbboggwororowyowyrwgbyyywwwyyy'
        expectedLocation = FTM

        actualCube, actualLocation, _ = middleLayer._rotateMiddlePieceFromMiddleToTop(cube, location)

        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedLocation, actualLocation)
        
    def test_middleLayer_050_CubeIndexProducesCorrectCubeIndexToMatchTopEdgePieceWithCorrespondingPiece(self):
        cube = 'oyyogrgggrgwwwyyrbbgwbbryobrwwyyboorbrobowgggwooyrbywr'
        location = BTM

        expectedCube = 'bgwogrgggrwwwwyyrboyybbryobrgwyyboorgggwoborbwooyrbywr'
        expectedLocation = FTM
        expectedSolution = 'UU'

        actualCube, actualLocation, actualSolution = middleLayer._alignEdgePieceWithAnotherTopPiece(cube, location)

        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedLocation, actualLocation)
        self.assertEqual(expectedSolution, actualSolution)
        
    def test_middleLayer_060_CubeIndexProducesNoRotationsToMatchTopEdgePieceWithCorrespondingPiece(self):
        cube = 'bbbbbbgggoroorororggggggbbbrorrororowwwyyywwwyyywwwyyy'
        location = FTM

        expectedCube = 'bbbbbbgggoroorororggggggbbbrorrororowwwyyywwwyyywwwyyy'
        expectedLocation = FTM
        expectedSolution = ''

        actualCube, actualLocation, actualSolution = middleLayer._alignEdgePieceWithAnotherTopPiece(cube, location)

        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedLocation, actualLocation)
        self.assertEqual(expectedSolution, actualSolution)
        
    def test_middleLayer_070_CubeIndexMatchesExpectedCubeIndex(self):
        cube = 'gggbbbgggrororororbbbgggbbborororowowrwyyywwwyyywwwyyy'

        expectedLocation = BTM

        actualCubeIndex = middleLayer._matchCenterMiddlePieceWithOtherMiddleCenters(cube)

        self.assertEqual(expectedLocation, actualCubeIndex)
        
    def test_middleLayer_080_CubeIndexMatchesExpectedCubeIndex(self):
        cube = 'gggbbbgggrororororbbbgggbbborororowowrwyyywwwyyywwwyyy'

        expectedLocation = FMR

        actualCubeIndex = middleLayer._alignCenterMiddlePieceWithEdgeMiddlePieces(cube)

        self.assertEqual(expectedLocation, actualCubeIndex)
        
    def test_middleLayer_090_CubeProducesRotationsToSolveMiddleLayer(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = 'orbyrrrrrrgoggggggyrroooooogyybbobbbyygbyybbywwwwwwwww'
        cube, rotations = parms['cube'], ''

        expectResult = {}
        expectedRotations = 'ulULUFuf'
        expectResult['status'] = 'ok'

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
            parms = {}
            parms['op'] = 'solve'
            parms['cube'] = cube

            expectResult = {}
            expectResult['status'] = 'ok'

            actualResult = solve.solve(parms)

            rotatedCube = {}
            rotatedCube['cube'] = parms.get('cube')
            rotatedCube['dir'] = actualResult.get('solution')
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
            self.assertEqual(expectResult.get('status'), actualResult.get('status'))
         
    # Sad Path Tests   
    def test_middleLayer_900_FailingCubesNowPass(self):
        cubes = ['bfLfELcLvbcfvbELbEEcbvLbvELLfvLcbfcEfvbLffEEvfccEvvcbc',
                 'VSmVFSSFFUUUUmVemmemUSUeUUmSmmSSUeeFVVSFVmFFVVVSFeeFee',
                 'XxXGJXxJTJxxJxXGGyXyJyGJGJyXyGxyXTGTxGGTTXyTyJyxxXTJTT',
                 'J3x33hh3xhB3xbxJB3BhbbxxJ33hxxBBBBJbxbhJJhbJB3bBbhJJhb'
                 ]
        for cube in cubes:
            parms = {}
            parms['op'] = 'solve'
            parms['cube'] = cube

            expectResult = {}
            expectResult['status'] = 'ok'

            actualResult = solve.solve(parms)

            rotatedCube = {}
            rotatedCube['cube'] = parms.get('cube')
            rotatedCube['dir'] = actualResult.get('solution')
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
            self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        