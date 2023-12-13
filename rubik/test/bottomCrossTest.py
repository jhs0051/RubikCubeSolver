'''
Created on Feb 12, 2023

@author: jonhoustonseibert
'''
import unittest
import rubik.view.solve as solve
import rubik.controller.bottomCross as bottomCross
from rubik.model.constants import *


class BottomCrossTest(unittest.TestCase):

    # Happy Path Tests  
    def test_bottomCross_000_SolvedCubeShouldReturnOkStatus(self):
        parms = {'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'dir': 'R'}

        expectedResult = {'status': 'ok'}

        actualResult = solve.solve(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_010_SolvedCubeContainsASolvedDaisyPattern(self):
        cube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        rotations = ''
        
        expectedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedRotations = ''
        
        actualCube, actualRotations = bottomCross.solveBottomCross(cube, rotations)
        self.assertEqual(actualCube[FMM], actualCube[FBM])
        self.assertEqual(actualCube[RMM], actualCube[RBM])
        self.assertEqual(actualCube[BMM], actualCube[BBM])
        self.assertEqual(actualCube[LMM], actualCube[LBM])
        self.assertEqual(actualCube[DTM], actualCube[DMM])
        self.assertEqual(actualCube[DML], actualCube[DMM])
        self.assertEqual(actualCube[DMR], actualCube[DMM])
        self.assertEqual(actualCube[DBM], actualCube[DMM])
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_bottomCross_020_CubeRotatesCornerPieceFromTopToBottom(self):
        cube = 'ggyobgybwbrwyrybwwbrgbggggyryroobbogwyooybyrrowrwwrowo'
        rotations = ''

        expectedRotations = 'RfUFUURR'
        expectedCube = 'ryoobbybgwyyrrgrrrbggyggwgywrgoobbogorryybwobowywwwowb'

        actualCube, actualRotations = bottomCross.solveBottomCross(cube, rotations)
        self.assertEqual(actualCube[FMM], actualCube[FBM])
        self.assertEqual(actualCube[RMM], actualCube[RBM])
        self.assertEqual(actualCube[BMM], actualCube[BBM])
        self.assertEqual(actualCube[LMM], actualCube[LBM])
        self.assertEqual(actualCube[DTM], actualCube[DMM])
        self.assertEqual(actualCube[DML], actualCube[DMM])
        self.assertEqual(actualCube[DMR], actualCube[DMM])
        self.assertEqual(actualCube[DBM], actualCube[DMM])
        self.assertEqual(expectedRotations, actualRotations)
        self.assertEqual(expectedCube, actualCube)
        
    def test_bottomCross_030_CubeRotatesMiddleTopPieceToBottom(self):
        cube = 'rrgbbwbbryrrgrrgyyyooggyogwbbwroogooyybyybbwrwwwwwgoog'
        rotations = ''

        expectedRotations = 'RUrUUBBRR'
        expectedCube = 'ybybbybbwoyrrrogrrggoyggwggyrrroowoogoybygbybwwowwwrwb'

        actualCube, actualRotations = bottomCross.solveBottomCross(cube, rotations)
        self.assertEqual(actualCube[FMM], actualCube[FBM])
        self.assertEqual(actualCube[RMM], actualCube[RBM])
        self.assertEqual(actualCube[BMM], actualCube[BBM])
        self.assertEqual(actualCube[LMM], actualCube[LBM])
        self.assertEqual(actualCube[DTM], actualCube[DMM])
        self.assertEqual(actualCube[DML], actualCube[DMM])
        self.assertEqual(actualCube[DMR], actualCube[DMM])
        self.assertEqual(actualCube[DBM], actualCube[DMM])
        self.assertEqual(expectedRotations, actualRotations)
        self.assertEqual(expectedCube, actualCube)
        
    def test_bottomCross_040_MakesBottomCrossWithStatusOk(self):
        parms = {'op': 'solve', 'cube': 'yoyoyggwbogrrobooowooywbbwrwybwrwgbwgbbrgyrggrrwrbyygy'}
        cube = parms['cube']
        rotations = ''

        expectedResult = {'status': 'ok'}
        expectedRotations = 'LbUBUULLBUbUFFfuFUUUBBUUURR'

        actualResult = solve.solve(parms)
        actualCube, actualRotations = bottomCross.solveBottomCross(cube, rotations)
        self.assertEqual(actualCube[FMM], actualCube[FBM])
        self.assertEqual(actualCube[RMM], actualCube[RBM])
        self.assertEqual(actualCube[BMM], actualCube[BBM])
        self.assertEqual(actualCube[LMM], actualCube[LBM])
        self.assertEqual(actualCube[DTM], actualCube[DMM])
        self.assertEqual(actualCube[DML], actualCube[DMM])
        self.assertEqual(actualCube[DMR], actualCube[DMM])
        self.assertEqual(actualCube[DBM], actualCube[DMM])
        self.assertEqual(expectedRotations, actualRotations)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

    def test_bottomCross_050_MakesBottomCrossWithStatusOk(self):
        parms = {'op': 'solve', 'cube': 'gwgywyyrrooroywyyrwogbgrwwwryobbwbbobgbgobbrywgggrrooy'}
        cube = parms['cube']
        rotations = ''
        
        expectedResult = {'status': 'ok'}
        expectedRotations = 'LUlUUULLluLFFFRurfBB'

        actualResult = solve.solve(parms)
        actualCube, actualRotations = bottomCross.solveBottomCross(cube, rotations)
        self.assertEqual(actualCube[FMM], actualCube[FBM])
        self.assertEqual(actualCube[RMM], actualCube[RBM])
        self.assertEqual(actualCube[BMM], actualCube[BBM])
        self.assertEqual(actualCube[LMM], actualCube[LBM])
        self.assertEqual(actualCube[DTM], actualCube[DMM])
        self.assertEqual(actualCube[DML], actualCube[DMM])
        self.assertEqual(actualCube[DMR], actualCube[DMM])
        self.assertEqual(actualCube[DBM], actualCube[DMM])
        self.assertEqual(expectedRotations, actualRotations)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

    def test_bottomCross_060_MakesBottomCrossWithStatusOk(self):
        parms = {'op': 'solve', 'cube': 'oyyogrgggrgwwwyyrbbgwbbryobrwwyyboorbrobowgggwooyrbywr'}
        cube = parms['cube']
        rotations = ''
        
        expectedResult = {'status': 'ok'}
        expectedRotations = 'RUrUUURRruRUUFFLUlUUULLFRurfBB'

        actualResult = solve.solve(parms)
        actualCube, actualRotations = bottomCross.solveBottomCross(cube, rotations)
        self.assertEqual(actualCube[FMM], actualCube[FBM])
        self.assertEqual(actualCube[RMM], actualCube[RBM])
        self.assertEqual(actualCube[BMM], actualCube[BBM])
        self.assertEqual(actualCube[LMM], actualCube[LBM])
        self.assertEqual(actualCube[DTM], actualCube[DMM])
        self.assertEqual(actualCube[DML], actualCube[DMM])
        self.assertEqual(actualCube[DMR], actualCube[DMM])
        self.assertEqual(actualCube[DBM], actualCube[DMM])
        self.assertEqual(expectedRotations, actualRotations)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

    def test_bottomCross_070_MakesBottomCrossWithStatusOk(self):
        parms = {'op': 'solve', 'cube': 'rgwgggbwbbyoywwgbrgyborbowwrbygyoorwyryyboowgrryoorgbw'}
        cube = parms['cube']
        rotations = ''

        expectedResult = {'status': 'ok'}
        expectedRotations = 'LLUBBBUbUFFLUlURRULL'

        actualResult = solve.solve(parms)
        actualCube, actualRotations = bottomCross.solveBottomCross(cube, rotations)
        self.assertEqual(actualCube[FMM], actualCube[FBM])
        self.assertEqual(actualCube[RMM], actualCube[RBM])
        self.assertEqual(actualCube[BMM], actualCube[BBM])
        self.assertEqual(actualCube[LMM], actualCube[LBM])
        self.assertEqual(actualCube[DTM], actualCube[DMM])
        self.assertEqual(actualCube[DML], actualCube[DMM])
        self.assertEqual(actualCube[DMR], actualCube[DMM])
        self.assertEqual(actualCube[DBM], actualCube[DMM])
        self.assertEqual(expectedRotations, actualRotations)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_080_MakesBottomCrossWithStatusOkForFailingTestCase(self):
        parms = {'op': 'solve', 'cube': 'dk999dif7f9k9i7if77kidkfd9ffkkddiki997ddfffid7ik77ki79'}
        cube = parms['cube']
        rotations = ''

        expectedResult = {'status': 'ok'}
        expectedRotations = 'BBUUFFLLUURRFUfLL'

        actualResult = solve.solve(parms)
        actualCube, actualRotations = bottomCross.solveBottomCross(cube, rotations)
        self.assertEqual(actualCube[FMM], actualCube[FBM])
        self.assertEqual(actualCube[RMM], actualCube[RBM])
        self.assertEqual(actualCube[BMM], actualCube[BBM])
        self.assertEqual(actualCube[LMM], actualCube[LBM])
        self.assertEqual(actualCube[DTM], actualCube[DMM])
        self.assertEqual(actualCube[DML], actualCube[DMM])
        self.assertEqual(actualCube[DMR], actualCube[DMM])
        self.assertEqual(actualCube[DBM], actualCube[DMM])
        self.assertEqual(actualCube, '7kid9fd97ffidiiki79kf9kfdkkk9ikd9id9dd7ffiki9f7d777f79')
        self.assertEqual(actualRotations, expectedRotations)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    