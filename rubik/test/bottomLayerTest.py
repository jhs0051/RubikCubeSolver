'''
Created on Feb 28, 2023

@author: jonhoustonseibert
'''
import unittest
import rubik.view.solve as solve
import rubik.controller.bottomLayer as bottomLayer
from rubik.view.rotate import rotate
from rubik.model.constants import *


class BottomLayerTest(unittest.TestCase):

    # Happy Path Tests  
    def test_bottomLayer_000_SolvedCubeShouldReturnOkStatus(self):
        parms = {'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'dir': 'R'}

        expectedResult = {'status': 'ok'}

        actualResult = solve.solve(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_bottomLayer_010_SolvedCubeDoesNotContainRotations(self):
        cube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        rotations = ''
        
        expectedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedRotations = ''
        
        actualCube, actualRotations = bottomLayer.solveBottomLayer(cube, rotations)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_bottomCorners_020_TestEdgePieceGetsRotatedToDifferentFaceSameEdge(self):
        cube = 'gggbbbgggrororororbbbgggbbbororororowwwyyywwwyyywwwyyy'
        cubeIndex = BTL

        expectedCube = 'rorbbbgggbbbororororogggbbbgggrororowywwywwywyyywwwyyy'
        expectedSolution = 'U'
        expectedCubeIndex = RTL

        actualCube, currentCubeIndex, actualSolution = bottomLayer._rotateEdgePieceToDifferentFace(cube, cubeIndex)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedCubeIndex, currentCubeIndex)
        self.assertEqual(expectedSolution, actualSolution)
        
    def test_bottomCorners_030_TestBottomEdgePieceGetsRotatedToTopEdge(self):
        cube = 'gggbbbgggrororororbbbgggbbbororororowwwyyywwwyyywwwyyy'
        cubeIndex = FTR

        expectedCube = 'ggybbwgggrowbroworborgggbbbbrorororowyoyybwwgyyrwwwyyy'
        expectedsolution = 'RUru'

        actualCube, currentCubeIndex, actualSolution = bottomLayer._rotateBottomEdgePieceToTopEdgePiece(cube, cubeIndex)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedsolution, actualSolution)
        
    def test_bottomCorners_035_TestBottomEdgePieceGetsRotatedToTopEdge(self):
        cube = 'gggbbbgggrororororbbbgggbbbororororowwwyyywwwyyywwwyyy'
        cubeIndex = BTR

        expectedCube = 'grobbbggggororororbbyggwbbborwgorwrobwwgyyrywyyywwwoyy'
        expectedSolution = 'LUlu'
        expectedCubeIndex = BBR


        actualCube, currentCubeIndex, actualSolution = bottomLayer._rotateBottomEdgePieceToTopEdgePiece(cube, cubeIndex)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedCubeIndex, currentCubeIndex)
        self.assertEqual(expectedSolution, actualSolution)
        
    def test_bottomCorners_040_TestRotatesBottomEdgeCW(self):
        cube = 'gggbbbgggrororororbbbgggbbbororororowwwyyywwwyyywwwyyy'
        cubeIndex = BBR

        expectedCube = 'orwbbbggggororororbboggybbywgwrorbrobwwwyyggryyywwwoyy'
        expectedSolution = 'LUluLUlu'


        actualCube, currentCubeIndex, actualSolution = bottomLayer._rotateBottomEdgeCW(cube, cubeIndex)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedSolution, actualSolution)
        
    def test_bottomCorners_050_TestChangeCubeIndexForRotation(self):
        cube = 'rgwyobooybobobrgbbygybrbrrrgrbygrgggooogyyyyowwrwwwwww'

        expectedCubeIndex = FTR

        currentCubeIndex = bottomLayer._doBottomEdgePieceColorsMatch(cube)
        self.assertEqual(expectedCubeIndex, currentCubeIndex)
        
    def test_bottomCorners_060_TestBottomColorsMatch(self):
        cube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        currentCubeIndex = FBR

        expectedResult = True

        actualResult = bottomLayer._doBottomColorsMatchBottomFaceColors(cube, currentCubeIndex)
        self.assertEqual(expectedResult, actualResult)
        
    def test_bottomCorners_070_TestBottomEdgePieceGetsRotatedToTop(self):
        cube = 'gwogwbbyrbyowroyyowwwgyogoorrwyowwrrbrbbbgroyybgggrgby'

        expectedCube = 'gwggwrbyoywbwroyyowyogyogoowrwyowwrrbgrbbbrorybbggrgby'
        expectedSolution = 'RUru'
        expectedCubeIndex = FTR

        actualCube, currentCubeIndex, actualSolution = bottomLayer._rotateBottomEdgePieceToTopEdge(cube)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedCubeIndex, currentCubeIndex)
        self.assertEqual(expectedSolution, actualSolution)
        
    def test_bottomCorners_080_TestBottomEdgePieceGetsRotatedToTop(self):
        cube = 'ryborbrrgyggrgbwggobroogoooggbrbybbbyyyoyyyrowwrwwwwww'

        expectedCubeIndex = FBR

        currentCubeIndex = bottomLayer._rotateBottomEdgesInCorrectPosition(cube)
        self.assertEqual(expectedCubeIndex, currentCubeIndex)

    def test_bottomCorners_090_TestSolveBottomLayerProducesSolutionToSolvedBottomLayerCube(self):
        parms = {'op': 'solve', 'cube': 'bbggrwogyryobgwwyoyybroogbbwbggwrwwgrowgbwroyyyroyrorb'}
        cube, rotations = parms['cube'], ''

        expectedResult = {'status': 'ok'}
        expectedRotations = 'RUruRUruRUruUFUfuUULUluLUluLUluLUluLUluBUbuBUbuBUbuBUbuBUbu'

        actualResult = solve.solve(parms)
        actualCube, actualRotations = bottomLayer.solveBottomLayer(cube, rotations)
        self.assertEqual(expectedRotations, actualRotations)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

    def test_bottomCorners_100_TestSolvedCubeColorsMatch(self):
        cubes = ['ggoorggyygbrooowyobbywywrobwbybbrwrooygrwgbryrwbwggryw',
                 'orgrrwoyrygygbwooorybrgwggbrwwowogrwygwyoogbwrbbyybybb',
                 'brwybbywogoywrwgoyrywggrbrgbwryogoobobgrybwbrroygwywgo',
                 'yyggybgyorgyoorbowrbrwgyywbgrrwwogbowgworrorobbywbywgb',
                 'oyyogrgggrgwwwyyrbbgwbbryobrwwyyboorbrobowgggwooyrbywr',
                 'bgoogogggbgwbwyowrgoybbgbbbrwryyywyogwrbowwoyyrwrrrory'
                ]
        for cube in cubes:
            parms = {'op': 'solve', 'cube': cube}
            expectedResult = {'status': 'ok'}
    
            actualResult = solve.solve(parms)
    
            rotatedCube = {'cube': parms.get('cube'), 'dir': actualResult.get('solution')}
            actualCube = rotate(rotatedCube).get('cube')
    
            cubeFaces = {
                "Bottom Face": [DTL, DTM, DTR, DML, DMM, DMR, DBL, DBM, DBR],
                "Front  Face": [FBL, FBM, FBR],
                "Right  Face": [RBL, RBM, RBR],
                "Back   Face": [BBL, BBM, BBR],
                "Left   Face": [LBL, LBM, LBR]
            }

            for cubeFaces, cubeIndexes in cubeFaces.items():
                faceColors = [actualCube[cubeIndex] for cubeIndex in cubeIndexes]
                self.assertTrue(all(color is faceColors[FTL] for color in faceColors))
    
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))  
    