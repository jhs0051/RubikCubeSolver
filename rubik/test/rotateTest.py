from unittest import TestCase
from rubik.view.rotate import rotate
 
class RotateTest(TestCase):
      
    # Happy Path Tests  
    def test_rotate_010_ErrorOnMissingCube(self):
        parms = {'cube': '', 'dir': 'F'}

        expectedResult = {'status': 'error: cube can not be empty'}

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

    def test_rotate_020_ErrorWithExtraneousKey(self):
        parms = {'op': 'rotate', 'extraneous': 'key', 'cube': 'ogwwrywybgyrgbgrrwoogbgwyrworyryggwbbbyyowgobroobwoybr',
                 'dir': 'F'}

        expectedResult = {'cube': 'wwoyrgbywgyrobgbrwoogbgwyrworrryogwobbyyowbgyrggbwoybr',
                          'status': 'error: invalid key'}

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_030_ErrorOnShortCube(self):
        parms = {'op': 'rotate', 'cube': 'g', 'dir': 'r'}

        expectedResult = {'status': 'error: invalid cube'}

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_040_ErrorOnLongCube(self):
        parms = {'op': 'rotate', 'cube': 'ogwwrywybgyrgbgrrwoogbgwyrworyryggwbbbyyowgobroobwoybrrrr', 'dir': 'r'}

        expectedResult = {'status': 'error: invalid cube'}

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_050_NoDirectionGivenReturnsOkStatus(self):
        parms = {'op': 'rotate', 'cube': 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo', 'dir': None}

        expectedResult = {'status': 'ok'}

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_060_NonStandardCubeLettersReturnsOk(self):
        parms = {'op': 'rotate', 'cube': 'bb0bPP00P6f44fbbff0f060066f46P4b4Pfff0b0446Pb6b4P664PP', 'dir': 'F'}

        expectedResult = {'status': 'ok'}

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    # Sad Path Tests  
    def test_rotate_910_ErrorWhenSingleRotationIsInvalid(self):
        parms = {'op': 'rotate', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww', 'dir': 'a'}

        expectedResult = {'status': 'error: invalid cube'}

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_920_ErrorWhenMultipleRotationIsInvalid(self):
        parms = {'op': 'rotate', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww', 'dir': 'abcdefg'}

        expectedResult = {'status': 'error: invalid cube'}

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_930_ErrorWithMoreThan9ValidColorLetters(self):
        parms = {'op': 'rotate', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwr', 'dir': 'f'}

        expectedResult = {'status': 'error: invalid cube'}

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_940_ErrorOnNonUniqueStandardMiddleColors(self):
        parms = {'op': 'rotate', 'cube': 'rbbbbbbbbrrrrbrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww', 'dir': 'F'}

        expectedResult = {'status': 'error: invalid cube'}

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_950_ErrorOnNonUniqueNonStandardMiddleColors(self):
        parms = {'op': 'rotate', 'cube': '111111111EEEEEEEEEGGGGGGGGGbbbbbbbb9999999999ccccccccc', 'dir': 'F'}

        expectedResult = {'status': 'error: invalid cube'}

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
        
    def test_rotate_960_RotateOnDirection_D_notSupported(self):
        parms = {'op': 'rotate', 'cube': 'ogwwrywybgyrgbgrrwoogpgwyrworyryggwbbbyyowgobroobwoybr', 'dir': 'D'}

        expectedResult = {'status': 'error: invalid cube'}

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_970_RotateOnDirection_d_notSupported(self):
        parms = {'op': 'rotate', 'cube': 'ogwwrywybgyrgbgrrwoogpgwyrworyryggwbbbyyowgobroobwoybr', 'dir': 'd'}

        expectedResult = {'status': 'error: invalid cube'}

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_980_ErrorOnIllegalCharacters(self):
        parms = {'op': 'rotate', 'cube': '   bbbbbbrrr      ooorrrrrrbbbooooooyyyyyyyyywwwwwwwww', 'dir': 'F'}

        expectedResult = {'status': 'error: invalid cube'}

        actualResult = rotate(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        