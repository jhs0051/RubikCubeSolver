'''
Created on March 19, 2023

@author: jonhoustonseibert
'''
import unittest
import rubik.view.solve as solve
from rubik.view.rotate import _rotate
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

        actualResult = solve._solve(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_bottomLayer_010_SolvedCubeDoesNotContainRotations(self):
        cube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        rotations = ''
        
        expectedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedRotations = ''
        
        actualCube, actualRotations = middleLayer._solveMiddleLayer(cube, rotations)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_bottomLayer_020_CubeIndexProducesCorrectRotationList(self):
        cube = 'gggbbbgggrororororbbbgggbbbororororowwwyyywwwyyywwwyyy'
        cubeIndex = RTM

        expectedCube = 'gwobbbgggwgrorororbroyggbbbggwrororowywoywrbbyyywwwyyy'
        expectedsolution = 'UBuburUR'

        actualCube, actualSolution = middleLayer._rotateMiddlePieceFromTopToMiddle(cube, cubeIndex)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedsolution, actualSolution)
        
    def test_bottomLayer_030_CubeIndexProducesCorrectRotationListWhenMiddleIsAllignedWithTopColor(self):
        cube = 'gggbbbgggrororororbbbgggbbborororowowrwyyywwwyyywwwyyy'
        cubeIndex = BTM

        expectedCube = 'woobbbgggggrorrrorbrwbggbbbgyororoworywoywbgwyyywwwyyy'
        expectedsolution = 'urURUBub'

        actualCube, actualSolution = middleLayer._rotateMiddlePieceFromTopToMiddle(cube, cubeIndex)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedsolution, actualSolution)
        
    def test_bottomLayer_040_CubeIndexProducesCorrectCubeIndexToRotateMiddlePieceToTopPiece(self):
        cube = 'gggbbbgggrororororbbbgggbbbororororowwwyyywwwyyywwwyyy'
        location = BMR

        expectedCube = 'rrwbbbgggrygorororwobggbbbboggwororowyowyrwgbyyywwwyyy'
        expectedLocation = FTM

        actualCube, actualLocation, _ = middleLayer._rotateMiddlePieceFromMiddleToTop(cube, location)

        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedLocation, actualLocation)
        
    def test_bottomLayer_050_CubeIndexProducesCorrectCubeIndexToMatchTopEdgePieceWithCorrespondingPiece(self):
        cube = 'oyyogrgggrgwwwyyrbbgwbbryobrwwyyboorbrobowgggwooyrbywr'
        location = BTM

        expectedCube = 'bgwogrgggrwwwwyyrboyybbryobrgwyyboorgggwoborbwooyrbywr'
        expectedLocation = FTM
        expectedSolution = 'UU'

        actualCube, actualLocation, actualSolution = middleLayer._alignEdgePieceWithAnotherTopPiece(cube, location)

        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedLocation, actualLocation)
        self.assertEqual(expectedSolution, actualSolution)
        
    def test_bottomLayer_060_CubeIndexProducesNoRotationsToMatchTopEdgePieceWithCorrespondingPiece(self):
        cube = 'bbbbbbgggoroorororggggggbbbrorrororowwwyyywwwyyywwwyyy'
        location = FTM

        expectedCube = 'bbbbbbgggoroorororggggggbbbrorrororowwwyyywwwyyywwwyyy'
        expectedLocation = FTM
        expectedSolution = ''

        actualCube, actualLocation, actualSolution = middleLayer._alignEdgePieceWithAnotherTopPiece(cube, location)

        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedLocation, actualLocation)
        self.assertEqual(expectedSolution, actualSolution)
        
    def test_bottomLayer_070_CubeIndexMatchesExpectedCubeIndex(self):
        cube = 'gggbbbgggrororororbbbgggbbborororowowrwyyywwwyyywwwyyy'

        expectedLocation = BTM

        actualCubeIndex = middleLayer._matchCenterMiddlePieceWithOtherMiddleCenters(cube)

        self.assertEqual(expectedLocation, actualCubeIndex)
        
    def test_bottomLayer_080_CubeIndexMatchesExpectedCubeIndex(self):
        cube = 'gggbbbgggrororororbbbgggbbborororowowrwyyywwwyyywwwyyy'

        expectedLocation = FMR

        actualCubeIndex = middleLayer._alignCenterMiddlePieceWithEdgeMiddlePieces(cube)

        self.assertEqual(expectedLocation, actualCubeIndex)
        
    def test_bottomLayer_090_CubeProducesRotationsToSolveMiddleLayer(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = 'orbyrrrrrrgoggggggyrroooooogyybbobbbyygbyybbywwwwwwwww'
        cube, rotations = parms['cube'], ''

        expectResult = {}
        expectedRotations = 'ulULUFuf'
        expectResult['status'] = 'ok'

        actualCube, actualRotations = middleLayer._solveMiddleLayer(cube, rotations)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_bottomLayer_100_CubeFullySolvesMiddleLayerAndBelow(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = 'ggoorggyygbrooowyobbywywrobwbybbrwrooygrwgbryrwbwggryw'

        expectResult = {}
        expectResult['status'] = 'ok'

        actualResult = solve._solve(parms)

        rotatedCube = {}
        rotatedCube['cube'] = parms.get('cube')
        rotatedCube['dir'] = actualResult.get('solution')
        actualCube = _rotate(rotatedCube).get('cube')

        bottomCubeColors = actualCube[DTL] is actualCube[DTM] is actualCube[DTR] is actualCube[DML] is actualCube[DMM] \
                           is actualCube[DMR] is actualCube[DBL] is actualCube[DBM] is actualCube[DBR]
        frontCubeColors = actualCube[FML] is actualCube[FMM] is actualCube[FMR] is actualCube[FBL] is actualCube[FBM] \
                          is actualCube[FBR]
        rightCubeColors = actualCube[RML] is actualCube[RMM] is actualCube[RMR] is actualCube[RBL] is actualCube[RBM] \
                          is actualCube[RBR]
        backCubeColors = actualCube[BML] is actualCube[BMM] is actualCube[BMR] is actualCube[BBL] is actualCube[BBM] \
                         is actualCube[BBR]
        leftCubeColors = actualCube[LML] is actualCube[LMM] is actualCube[LMR] is actualCube[LBL] is actualCube[LBM] \
                         is actualCube[LBR]

        self.assertTrue(bottomCubeColors)
        self.assertTrue(frontCubeColors)
        self.assertTrue(rightCubeColors)
        self.assertTrue(backCubeColors)
        self.assertTrue(leftCubeColors)
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomLayer_110_CubeFullySolvesMiddleLayerAndBelow(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = 'orgrrwoyrygygbwooorybrgwggbrwwowogrwygwyoogbwrbbyybybb'

        expectResult = {}
        expectResult['status'] = 'ok'

        actualResult = solve._solve(parms)

        rotatedCube = {}
        rotatedCube['cube'] = parms.get('cube')
        rotatedCube['dir'] = actualResult.get('solution')
        actualCube = _rotate(rotatedCube).get('cube')

        bottomCubeColors = actualCube[DTL] is actualCube[DTM] is actualCube[DTR] is actualCube[DML] is actualCube[DMM] \
                           is actualCube[DMR] is actualCube[DBL] is actualCube[DBM] is actualCube[DBR]
        frontCubeColors = actualCube[FML] is actualCube[FMM] is actualCube[FMR] is actualCube[FBL] is actualCube[FBM] \
                          is actualCube[FBR]
        rightCubeColors = actualCube[RML] is actualCube[RMM] is actualCube[RMR] is actualCube[RBL] is actualCube[RBM] \
                          is actualCube[RBR]
        backCubeColors = actualCube[BML] is actualCube[BMM] is actualCube[BMR] is actualCube[BBL] is actualCube[BBM] \
                         is actualCube[BBR]
        leftCubeColors = actualCube[LML] is actualCube[LMM] is actualCube[LMR] is actualCube[LBL] is actualCube[LBM] \
                         is actualCube[LBR]

        self.assertTrue(bottomCubeColors)
        self.assertTrue(frontCubeColors)
        self.assertTrue(rightCubeColors)
        self.assertTrue(backCubeColors)
        self.assertTrue(leftCubeColors)
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomLayer_120_CubeFullySolvesMiddleLayerAndBelow(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = 'brwybbywogoywrwgoyrywggrbrgbwryogoobobgrybwbrroygwywgo'

        expectResult = {}
        expectResult['status'] = 'ok'

        actualResult = solve._solve(parms)

        rotatedCube = {}
        rotatedCube['cube'] = parms.get('cube')
        rotatedCube['dir'] = actualResult.get('solution')
        actualCube = _rotate(rotatedCube).get('cube')

        bottomCubeColors = actualCube[DTL] is actualCube[DTM] is actualCube[DTR] is actualCube[DML] is actualCube[DMM] \
                           is actualCube[DMR] is actualCube[DBL] is actualCube[DBM] is actualCube[DBR]
        frontCubeColors = actualCube[FML] is actualCube[FMM] is actualCube[FMR] is actualCube[FBL] is actualCube[FBM] \
                          is actualCube[FBR]
        rightCubeColors = actualCube[RML] is actualCube[RMM] is actualCube[RMR] is actualCube[RBL] is actualCube[RBM] \
                          is actualCube[RBR]
        backCubeColors = actualCube[BML] is actualCube[BMM] is actualCube[BMR] is actualCube[BBL] is actualCube[BBM] \
                         is actualCube[BBR]
        leftCubeColors = actualCube[LML] is actualCube[LMM] is actualCube[LMR] is actualCube[LBL] is actualCube[LBM] \
                         is actualCube[LBR]

        self.assertTrue(bottomCubeColors)
        self.assertTrue(frontCubeColors)
        self.assertTrue(rightCubeColors)
        self.assertTrue(backCubeColors)
        self.assertTrue(leftCubeColors)
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomLayer_130_CubeFullySolvesMiddleLayerAndBelow(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = 'yyggybgyorgyoorbowrbrwgyywbgrrwwogbowgworrorobbywbywgb'

        expectResult = {}
        expectResult['status'] = 'ok'

        actualResult = solve._solve(parms)

        rotatedCube = {}
        rotatedCube['cube'] = parms.get('cube')
        rotatedCube['dir'] = actualResult.get('solution')
        actualCube = _rotate(rotatedCube).get('cube')

        bottomCubeColors = actualCube[DTL] is actualCube[DTM] is actualCube[DTR] is actualCube[DML] is actualCube[DMM] \
                           is actualCube[DMR] is actualCube[DBL] is actualCube[DBM] is actualCube[DBR]
        frontCubeColors = actualCube[FML] is actualCube[FMM] is actualCube[FMR] is actualCube[FBL] is actualCube[FBM] \
                          is actualCube[FBR]
        rightCubeColors = actualCube[RML] is actualCube[RMM] is actualCube[RMR] is actualCube[RBL] is actualCube[RBM] \
                          is actualCube[RBR]
        backCubeColors = actualCube[BML] is actualCube[BMM] is actualCube[BMR] is actualCube[BBL] is actualCube[BBM] \
                         is actualCube[BBR]
        leftCubeColors = actualCube[LML] is actualCube[LMM] is actualCube[LMR] is actualCube[LBL] is actualCube[LBM] \
                         is actualCube[LBR]

        self.assertTrue(bottomCubeColors)
        self.assertTrue(frontCubeColors)
        self.assertTrue(rightCubeColors)
        self.assertTrue(backCubeColors)
        self.assertTrue(leftCubeColors)
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomLayer_140_CubeFullySolvesMiddleLayerAndBelow(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = 'oyyogrgggrgwwwyyrbbgwbbryobrwwyyboorbrobowgggwooyrbywr'

        expectResult = {}
        expectResult['status'] = 'ok'

        actualResult = solve._solve(parms)

        rotatedCube = {}
        rotatedCube['cube'] = parms.get('cube')
        rotatedCube['dir'] = actualResult.get('solution')
        actualCube = _rotate(rotatedCube).get('cube')

        bottomCubeColors = actualCube[DTL] is actualCube[DTM] is actualCube[DTR] is actualCube[DML] is actualCube[DMM] \
                           is actualCube[DMR] is actualCube[DBL] is actualCube[DBM] is actualCube[DBR]
        frontCubeColors = actualCube[FML] is actualCube[FMM] is actualCube[FMR] is actualCube[FBL] is actualCube[FBM] \
                          is actualCube[FBR]
        rightCubeColors = actualCube[RML] is actualCube[RMM] is actualCube[RMR] is actualCube[RBL] is actualCube[RBM] \
                          is actualCube[RBR]
        backCubeColors = actualCube[BML] is actualCube[BMM] is actualCube[BMR] is actualCube[BBL] is actualCube[BBM] \
                         is actualCube[BBR]
        leftCubeColors = actualCube[LML] is actualCube[LMM] is actualCube[LMR] is actualCube[LBL] is actualCube[LBM] \
                         is actualCube[LBR]

        self.assertTrue(bottomCubeColors)
        self.assertTrue(frontCubeColors)
        self.assertTrue(rightCubeColors)
        self.assertTrue(backCubeColors)
        self.assertTrue(leftCubeColors)
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        