import unittest
import rubik.view.solve as solve
import rubik.controller.bottomCross as bottomCross


class BottomCrossTest(unittest.TestCase):

    # Happy Path Tests  
    # Saving to end of iteration
    """def test_bottomCross_010_SolvedCubeShouldReturnOkStatus(self):
        parms = {}
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms['dir'] = 'R'
        
        expectedResult = {}
        expectedResult['status'] = 'ok'

        actualResult = bottomCross.solveBottomCross(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))"""
        
    def test_bottomCross_010_SolvedCubeContainsASolvedDaisyPattern(self):
        cube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        
        expectedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedRotations = ''
        
        actualCube, actualRotations = bottomCross.solveBottomCross(cube, '')
        
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_bottomCross_020_CubeRotatesCornerPieceFromBottomToTop(self):
        cube = 'ggyobgybwbrwyrybwwbrgbggggyryroobbogwyooybyrrowrwwrowo'
        rotations = ''

        expectedRotations = 'RfUFUURR'
        expectedCube = 'ryoobbybgwyyrrgrrrbggyggwgywrgoobbogorryybwobowywwwowb'

        actualCube, actualRotations = bottomCross.solveBottomCross(cube, rotations)
        self.assertEqual(expectedRotations, actualRotations)
        self.assertEqual(expectedCube, actualCube)
        
    def test_bottomCross_030_CubeRotatesCornerPieceFromBottomToTop(self):
        cube = 'rrgbbwbbryrrgrrgyyyooggyogwbbwroogooyybyybbwrwwwwwgoog'
        rotations = ''

        expectedRotations = 'RUrUUBBRR'
        expectedCube = 'ybybbybbwoyrrrogrrggoyggwggyrrroowoogoybygbybwwowwwrwb'

        actualCube, actualRotations = bottomCross.solveBottomCross(cube, rotations)
        self.assertEqual(expectedRotations, actualRotations)
        self.assertEqual(expectedCube, actualCube)
        
    def test_bottomCross_040_MakesBottomCrossWithStatusOk(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = 'yoyoyggwbogrrobooowooywbbwrwybwrwgbwgbbrgyrggrrwrbyygy'

        expectResult = {}
        expectedRotations = 'LbUBUULLBUbUFFfuFUUUBBUUURR'
        expectResult['status'] = 'ok'

        actualResult = solve.solve(parms)
        self.assertEqual(expectedRotations, actualResult.get('solution'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    def test_bottomCross_050_MakesBottomCrossWithStatusOk(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = 'gwgywyyrrooroywyyrwogbgrwwwryobbwbbobgbgobbrywgggrrooy'

        expectResult = {}
        expectedRotations = ''
        expectResult['status'] = 'ok'

        actualResult = solve.solve(parms)
        self.assertEqual(expectedRotations, actualResult.get('solution'))
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    # Sad Path
    def test_bottomCross_910_ErrorOnEmptyString(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = ''

        expectResult = {}
        expectResult['status'] = 'error: cube can not be empty'

        actualResult = solve.solve(parms)

        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        
    