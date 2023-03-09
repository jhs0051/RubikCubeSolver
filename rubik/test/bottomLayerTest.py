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
        parms = {}
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms['dir'] = 'R'
        
        expectedResult = {}
        expectedResult['status'] = 'ok'

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

        actualCube, currentCubeIndex, actualSolution = bottomLayer.rotateEdgePieceToDifferentFace(cube, cubeIndex)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedCubeIndex, currentCubeIndex)
        self.assertEqual(expectedSolution, actualSolution)
        
    def test_bottomCorners_030_TestBottomEdgePieceGetsRotatedToTopEdge(self):
        cube = 'gggbbbgggrororororbbbgggbbbororororowwwyyywwwyyywwwyyy'
        cubeIndex = FTR

        expectedCube = 'ggybbwgggrowbroworborgggbbbbrorororowyoyybwwgyyrwwwyyy'
        expectedsolution = 'RUru'

        actualCube, currentCubeIndex, actualSolution = bottomLayer.rotateBottomEdgePieceToTopEdgePiece(cube, cubeIndex)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedsolution, actualSolution)
        
    def test_bottomCorners_035_TestBottomEdgePieceGetsRotatedToTopEdge(self):
        cube = 'gggbbbgggrororororbbbgggbbbororororowwwyyywwwyyywwwyyy'
        cubeIndex = BTR

        expectedCube = 'grobbbggggororororbbyggwbbborwgorwrobwwgyyrywyyywwwoyy'
        expectedSolution = 'LUlu'
        expectedCubeIndex = BBR


        actualCube, currentCubeIndex, actualSolution = bottomLayer.rotateBottomEdgePieceToTopEdgePiece(cube, cubeIndex)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedCubeIndex, currentCubeIndex)
        self.assertEqual(expectedSolution, actualSolution)
        
    def test_bottomCorners_040_TestRotatesBottomEdgeCW(self):
        cube = 'gggbbbgggrororororbbbgggbbbororororowwwyyywwwyyywwwyyy'
        cubeIndex = BBR

        expectedCube = 'orwbbbggggororororbboggybbywgwrorbrobwwwyyggryyywwwoyy'
        expectedSolution = 'LUluLUlu'


        actualCube, currentCubeIndex, actualSolution = bottomLayer.rotateBottomEdgeCW(cube, cubeIndex)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedSolution, actualSolution)
        
    def test_bottomCorners_050_TestChangeCubeIndexForRotation(self):
        cube = 'rgwyobooybobobrgbbygybrbrrrgrbygrgggooogyyyyowwrwwwwww'

        expectedCubeIndex = 2

        currentCubeIndex = bottomLayer.doBottomEdgePieceColorsMatch(cube)
        self.assertEqual(expectedCubeIndex, currentCubeIndex)
        
    def test_bottomCorners_060_TestBottomColorsMatch(self):
        cube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        currentCubeIndex = FBR

        expectedResult = True

        actualResult = bottomLayer.doBottomColorsMatchBottomFaceColors(cube, currentCubeIndex)
        self.assertEqual(expectedResult, actualResult)
        
    '''def test_bottomCorners_070_TestBottomEdgePieceGetsRotatedToTop(self):
        cube = 'gggbbbgggrororororbbbgggbbbororororowwwyyywwwyyywwwyyy'
        currentCubeIndex = None

        expectedCube = 'ggybbwgggrowbroworborgggbbbbrorororowyoyybwwgyyrwwwyyy'
        expectedSolution = 'RUru'
        expectedCubeIndex = FTR

        actualCube, currentCubeIndex, actualSolution = bottomLayer.rotateBottomEdgePieceToTopEdgePiece(cube, currentCubeIndex)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedCubeIndex, currentCubeIndex)
        self.assertEqual(expectedSolution, actualSolution)'''
        
    def test_bottomCorners_080_TestBottomEdgePieceGetsRotatedToTop(self):
        cube = 'ryborbrrgyggrgbwggobroogoooggbrbybbbyyyoyyyrowwrwwwwww'

        expectedCubeIndex = FBR

        currentCubeIndex = bottomLayer.rotateBottomEdgesInCorrectPosition(cube)
        self.assertEqual(expectedCubeIndex, currentCubeIndex)

    def test_bottomCorners_090_TestSolveBottomLayerProducesSolutionToSolvedBottomLayerCube(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = 'bbggrwogyryobgwwyoyybroogbbwbggwrwwgrowgbwroyyyroyrorb'
        cube, rotations = parms['cube'], ''

        expectResult = {}
        expectedRotations = 'RUruRUruRUruUFUfuUULUluLUluLUluLUluLUluBUbuBUbuBUbuBUbuBUbu'
        expectResult['status'] = 'ok'

        actualCube, actualRotations = bottomLayer.solveBottomLayer(cube, rotations)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_bottomCorners_100_TestSolveBottomLayerProducesSolutionToSolvedBottomLayerCube(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = 'ggoorggyygbrooowyobbywywrobwbybbrwrooygrwgbryrwbwggryw'

        expectResult = {}
        expectResult['status'] = 'ok'
        
        actualResult = solve.solve(parms)
        
        rotatedCube = {}
        rotatedCube['cube'] = parms.get('cube')
        rotatedCube['dir'] = actualResult.get('solution')
        actualCube = rotate(rotatedCube).get('cube')

        bottomCubeColors = actualCube[45] is actualCube[46] is actualCube[47] is actualCube[48] is actualCube[49] \
                           is actualCube[50] is actualCube[51] is actualCube[52] is actualCube[53]
        frontCubeColors = actualCube[6] is actualCube[7] is actualCube[8]
        rightCubeColors = actualCube[15] is actualCube[16] is actualCube[17]
        backCubeColors = actualCube[24] is actualCube[25] is actualCube[26]
        leftCubeColors = actualCube[33] is actualCube[34] is actualCube[35]

        self.assertTrue(bottomCubeColors)
        self.assertTrue(frontCubeColors)
        self.assertTrue(rightCubeColors)
        self.assertTrue(backCubeColors)
        self.assertTrue(leftCubeColors)
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCorners_110_TestSolveBottomLayerProducesSolutionToSolvedBottomLayerCube(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = 'orgrrwoyrygygbwooorybrgwggbrwwowogrwygwyoogbwrbbyybybb'

        expectResult = {}
        expectResult['status'] = 'ok'
        
        actualResult = solve.solve(parms)

        rotatedCube = {}
        rotatedCube['cube'] = parms.get('cube')
        rotatedCube['dir'] = actualResult.get('solution')
        actualCube = rotate(rotatedCube).get('cube')

        bottomCubeColors = actualCube[45] is actualCube[46] is actualCube[47] is actualCube[48] is actualCube[49] \
                           is actualCube[50] is actualCube[51] is actualCube[52] is actualCube[53]
        frontCubeColors = actualCube[6] is actualCube[7] is actualCube[8]
        rightCubeColors = actualCube[15] is actualCube[16] is actualCube[17]
        backCubeColors = actualCube[24] is actualCube[25] is actualCube[26]
        leftCubeColors = actualCube[33] is actualCube[34] is actualCube[35]

        self.assertTrue(bottomCubeColors)
        self.assertTrue(frontCubeColors)
        self.assertTrue(rightCubeColors)
        self.assertTrue(backCubeColors)
        self.assertTrue(leftCubeColors)
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))

        
    