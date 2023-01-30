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
