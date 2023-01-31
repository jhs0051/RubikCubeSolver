from unittest import TestCase
from rubik.view.rotate import rotate
 
class RotateTest(TestCase):
        
    def test_rotate_010_ErrorOnMissingCube(self):
        parms = {}
        parms['cube'] = ''
        parms['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'
            
        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

    def test_rotate_020_ShouldRotateCubeWithExtraneousKey(self):
        parms = {}
        parms['op'] = 'rotate'
        parms['extraneous'] = 'key'
        parms['cube'] = 'ogwwrywybgyrgbgrrwoogbgwyrworyryggwbbbyyowgobroobwoybr'
        parms['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['cube'] = 'wwoyrgbywgyrobgbrwoogbgwyrworrryogwobbyyowbgyrggbwoybr'
        expectedResult['status'] = 'ok'

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube')) 
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))