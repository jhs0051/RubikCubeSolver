from unittest import TestCase
from rubik.view.rotate import rotate
 
class RotateTest(TestCase):
      
    # Happy Path Tests  
    def test_rotate_010_ErrorOnMissingCube(self):
        parms = {}
        parms['cube'] = ''
        parms['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'
            
        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

    def test_rotate_020_ErrorWithExtraneousKey(self):
        parms = {}
        parms['op'] = 'rotate'
        parms['extraneous'] = 'key'
        parms['cube'] = 'ogwwrywybgyrgbgrrwoogbgwyrworyryggwbbbyyowgobroobwoybr'
        parms['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['cube'] = 'wwoyrgbywgyrobgbrwoogbgwyrworrryogwobbyyowbgyrggbwoybr'
        expectedResult['status'] = 'error: extraneous key detected'

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_030_ErrorOnShortCube(self):
        parms = {}
        parms['op'] = 'rotate'
        parms['cube'] = 'g'
        parms['dir'] = 'r'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_040_ErrorOnLongCube(self):
        parms = {}
        parms['op'] = 'rotate'
        parms['cube'] = 'ogwwrywybgyrgbgrrwoogbgwyrworyryggwbbbyyowgobroobwoybrrrr'
        parms['dir'] = 'r'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    # Sad Path Tests  
    def test_rotate_910_ErrorWhenSingleRotationIsInvalid(self):
        parms = {}
        parms['op'] = 'rotate'
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        parms['dir'] = 'a'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_920_ErrorWhenMultipleRotationIsInvalid(self):
        parms = {}
        parms['op'] = 'rotate'
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        parms['dir'] = 'abcdefg'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_930_ErrorWithMoreThan9ValidColorLetters(self):
        parms = {}
        parms['op'] = 'rotate'
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwr'
        parms['dir'] = 'f'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_940_ErrorOnNonUniqueMiddleColors(self):
        parms = {}
        parms['op'] = 'rotate'
        parms['cube'] = 'rbbbbbbbbrrrrbrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        parms['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_950_ErrorOnNonSupportedColors(self):
        parms = {}
        parms['op'] = 'rotate'
        parms['cube'] = 'ogwwrywybgyrgbgrrwoogpgwyrworyryggwbbbyyowgobroobwoybr'
        parms['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_960_RotateOnDirection_D_notSupported(self):
        parms = {}
        parms['op'] = 'rotate'
        parms['cube'] = 'ogwwrywybgyrgbgrrwoogpgwyrworyryggwbbbyyowgobroobwoybr'
        parms['dir'] = 'D'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_970_RotateOnDirection_d_notSupported(self):
        parms = {}
        parms['op'] = 'rotate'
        parms['cube'] = 'ogwwrywybgyrgbgrrwoogpgwyrworyryggwbbbyyowgobroobwoybr'
        parms['dir'] = 'd'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        