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
        
    def test_rotate_050_NoDirectionGivenReturnsOkStatus(self):
        parms = {}
        parms['op'] = 'rotate'
        parms['cube'] = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        parms['dir'] = None
        
        expectedResult = {}
        expectedResult['status'] = 'ok'
        
        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_060_NonStandardCubeLettersReturnsOk(self):
        parms = {}
        parms['op'] = 'rotate'
        parms['cube'] = 'bb0bPP00P6f44fbbff0f060066f46P4b4Pfff0b0446Pb6b4P664PP'
        parms['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['status'] = 'ok'
        
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
        
    def test_rotate_940_ErrorOnNonUniqueStandardMiddleColors(self):
        parms = {}
        parms['op'] = 'rotate'
        parms['cube'] = 'rbbbbbbbbrrrrbrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        parms['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_950_ErrorOnNonUniqueNonStandardMiddleColors(self):
        parms = {}
        parms['op'] = 'rotate'
        parms['cube'] = '111111111EEEEEEEEEGGGGGGGGGbbbbbbbb9999999999ccccccccc'
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
        
    def test_rotate_980_ErrorOnIllegalCharacters(self):
        parms = {}
        parms['op'] = 'rotate'
        parms['cube'] = '   bbbbbbrrr      ooorrrrrrbbbooooooyyyyyyyyywwwwwwwww'
        parms['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        