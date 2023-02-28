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
        parms = {}
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms['dir'] = 'R'
        
        expectedResult = {}
        expectedResult['status'] = 'ok'

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
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = 'yoyoyggwbogrrobooowooywbbwrwybwrwgbwgbbrgyrggrrwrbyygy'
        cube, rotations = parms['cube'], ''

        expectResult = {}
        expectedRotations = 'LbUBUULLBUbUFFfuFUUUBBUUURR'
        expectResult['status'] = 'ok'

        actualResult = solve.solve(parms)
        actualCube, _ = bottomCross.solveBottomCross(cube, rotations)
        self.assertEqual(actualCube[FMM], actualCube[FBM])
        self.assertEqual(actualCube[RMM], actualCube[RBM])
        self.assertEqual(actualCube[BMM], actualCube[BBM])
        self.assertEqual(actualCube[LMM], actualCube[LBM])
        self.assertEqual(actualCube[DTM], actualCube[DMM])
        self.assertEqual(actualCube[DML], actualCube[DMM])
        self.assertEqual(actualCube[DMR], actualCube[DMM])
        self.assertEqual(actualCube[DBM], actualCube[DMM])
        self.assertEqual(expectedRotations, actualResult.get('solution'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))

    def test_bottomCross_050_MakesBottomCrossWithStatusOk(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = 'gwgywyyrrooroywyyrwogbgrwwwryobbwbbobgbgobbrywgggrrooy'
        cube, rotations = parms['cube'], ''

        expectResult = {}
        expectedRotations = 'LUlUUULLluLFFFRurfBB'
        expectResult['status'] = 'ok'

        actualResult = solve.solve(parms)
        actualCube, _ = bottomCross.solveBottomCross(cube, rotations)
        self.assertEqual(actualCube[FMM], actualCube[FBM])
        self.assertEqual(actualCube[RMM], actualCube[RBM])
        self.assertEqual(actualCube[BMM], actualCube[BBM])
        self.assertEqual(actualCube[LMM], actualCube[LBM])
        self.assertEqual(actualCube[DTM], actualCube[DMM])
        self.assertEqual(actualCube[DML], actualCube[DMM])
        self.assertEqual(actualCube[DMR], actualCube[DMM])
        self.assertEqual(actualCube[DBM], actualCube[DMM])
        self.assertEqual(expectedRotations, actualResult.get('solution'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))

    def test_bottomCross_060_MakesBottomCrossWithStatusOk(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = 'oyyogrgggrgwwwyyrbbgwbbryobrwwyyboorbrobowgggwooyrbywr'
        cube, rotations = parms['cube'], ''
        
        expectResult = {}
        expectedRotations = 'RUrUUURRruRUUFFLUlUUULLFRurfBB'
        expectResult['status'] = 'ok'

        actualResult = solve.solve(parms)
        actualCube, _ = bottomCross.solveBottomCross(cube, rotations)
        self.assertEqual(actualCube[FMM], actualCube[FBM])
        self.assertEqual(actualCube[RMM], actualCube[RBM])
        self.assertEqual(actualCube[BMM], actualCube[BBM])
        self.assertEqual(actualCube[LMM], actualCube[LBM])
        self.assertEqual(actualCube[DTM], actualCube[DMM])
        self.assertEqual(actualCube[DML], actualCube[DMM])
        self.assertEqual(actualCube[DMR], actualCube[DMM])
        self.assertEqual(actualCube[DBM], actualCube[DMM])
        self.assertEqual(expectedRotations, actualResult.get('solution'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))

    def test_bottomCross_070_MakesBottomCrossWithStatusOk(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = 'rgwgggbwbbyoywwgbrgyborbowwrbygyoorwyryyboowgrryoorgbw'
        cube, rotations = parms['cube'], ''

        expectResult = {}
        expectedRotations = 'LLUBBBUbUFFLUlURRULL'
        expectResult['status'] = 'ok'

        actualResult = solve.solve(parms)
        actualCube, _ = bottomCross.solveBottomCross(cube, rotations)
        self.assertEqual(actualCube[FMM], actualCube[FBM])
        self.assertEqual(actualCube[RMM], actualCube[RBM])
        self.assertEqual(actualCube[BMM], actualCube[BBM])
        self.assertEqual(actualCube[LMM], actualCube[LBM])
        self.assertEqual(actualCube[DTM], actualCube[DMM])
        self.assertEqual(actualCube[DML], actualCube[DMM])
        self.assertEqual(actualCube[DMR], actualCube[DMM])
        self.assertEqual(actualCube[DBM], actualCube[DMM])
        self.assertEqual(expectedRotations, actualResult.get('solution'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_080_MakesBottomCrossWithStatusOk(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = 'dk999dif7f9k9i7if77kidkfd9ffkkddiki997ddfffid7ik77ki79'
        cube, rotations = parms['cube'], ''

        expectResult = {}
        expectedRotations = 'BBLLUURRBBUUFFFUfLLUUUBB'
        expectResult['status'] = 'ok'

        actualResult = solve.solve(parms)
        actualCube, _ = bottomCross.solveBottomCross(cube, rotations)
        self.assertEqual(actualCube[FMM], actualCube[FBM])
        self.assertEqual(actualCube[RMM], actualCube[RBM])
        self.assertEqual(actualCube[BMM], actualCube[BBM])
        self.assertEqual(actualCube[LMM], actualCube[LBM])
        self.assertEqual(actualCube[DTM], actualCube[DMM])
        self.assertEqual(actualCube[DML], actualCube[DMM])
        self.assertEqual(actualCube[DMR], actualCube[DMM])
        self.assertEqual(actualCube[DBM], actualCube[DMM])
        self.assertEqual(expectedRotations, actualResult.get('solution'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    # Sad Path Tests
    def test_bottomCross_910_ErrorOnEmptyString(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = ''

        expectResult = {}
        expectResult['status'] = 'error: cube can not be empty'

        actualResult = solve.solve(parms)
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    