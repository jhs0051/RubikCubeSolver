'''
Created on Jan 28, 2023

@author: jonhoustonseibert
'''
import unittest
import rubik.model.cube as cube


class CubeTest(unittest.TestCase):

    # Happy Path Tests  
    def test_rotate_010_ShouldRotateCubeInDirection_F(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F')
        
        self.assertEqual(rotatedCube,'ywygbgggrbobwrywrwobrggrgwywyoyoobbygwwbyygrrrrbowbooo')
    
    def test_rotate_020_ShouldRotateCubeInDirection_f(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('f')
        
        self.assertEqual(rotatedCube,'rgggbgywyyoboryorwobrggrgwywywyowbbbgwwbyybrrrrgowbooo')
    
    def test_rotate_030_ShouldRotateCubeInDirection_R(self):
        cubeToRotate = 'ygyrbwworoyygywbbogryrgybygwywwrboorgoogoobrbgbwgwwrbr'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('R')
        
        self.assertEqual(rotatedCube,'ygwrbwworbgobyyowybryogyoygwywwrboorgoygowbrrgbbgwrrbg')
        
    def test_rotate_040_ShouldRotateCubeInDirection_r(self):
        cubeToRotate = 'gyrbgwgbbbwryyoogywryrrygbygborbrrywowywwgbowbgrgoooow'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('r')
        
        self.assertEqual(rotatedCube,'gyybgggbwroywygbyowryoryrbygborbrrywowgwwrbowbgrgowoob')
        
    def test_rotate_050_ShouldRotateCubeInDirection_B(self):
        cubeToRotate = 'ygboboyybgbrrowgwgbooyybyorbggrgyyyowbobrwwrwwgrrwgowr'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('B')
        
        self.assertEqual(rotatedCube,'ygboboyybgbrrowgwoyyboyorbooggbgywyorwgbrwwrwwgrrwgbry')
        
    def test_rotate_060_ShouldRotateCubeInDirection_b(self):
        cubeToRotate = 'oyrybyobbyooogbrobrwwrowwgygbygyrorgbbggrrwwbwyggwwroy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('b')
        
        self.assertEqual(rotatedCube,'oyrybyobbyobogbrogwwywogrrwrbyoyryrgogggrrwwbwyggwwbbo')
        
    def test_rotate_070_ShouldRotateCubeInDirection_L(self):
        cubeToRotate = 'gybwyrworgbgogwywbbggbbgrgwygybrryrboywwwowroryoboyroo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('L')
        
        self.assertEqual(rotatedCube,'oybwyrworgbgogwywbbgrbbbrgrybyrrgbrywywgwogrogyowoywoo')
    
    def test_rotate_080_ShouldRotateCubeInDirection_l(self):
        cubeToRotate = 'bbowyoworyorrwwggggbrgbwbygbroyrowyyorbggywwrobyrobygw'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('l')
        
        self.assertEqual(rotatedCube,'oboryoyoryorrwwggggbwgbgbyoooyrrybywbrbwgywwrgbywobrgw')
        
    def test_rotate_090_ShouldRotateCubeInDirection_U(self):
        cubeToRotate = 'byywoyorboborbgwobyogrrgyowybrwgbrygrygoyrwbbwwogwwggr'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('U')
        
        self.assertEqual(rotatedCube,'obowoyorbyogrbgwobybrrrgyowbyywgbrygworbyybrgwwogwwggr')
        
    def test_rotate_100_ShouldRotateCubeInDirection_u(self):
        cubeToRotate = 'oowybwwbybwboowrggoyrbrryyywrrwgbggoggyyygwrgboorwbrob'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('u')
        
        self.assertEqual(rotatedCube,'wrrybwwbyoowoowrggbwbbrryyyoyrwgbggoygggyrgywboorwbrob')
        
    def test_rotate_110_ShouldRotateCubeWithNoDirectionGiven(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('')
        
        self.assertEqual(rotatedCube,'ywygbgggrbobwrywrwobrggrgwywyoyoobbygwwbyygrrrrbowbooo')
        
    def test_rotate_120_ShouldRotateCubeWithMultipleValidRotations(self):
        cubeToRotate = 'gwobrwwyorrrbyowwoobgywyyoybgbgborygrgyrgbwobyrbwoggrw'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('rFrURdBuububBUufFfuLRdrRr')
        
        self.assertEqual(rotatedCube,'ogyorbwgogwywyyrorwgrwwrbybbgwbbbwyyobgygobrrowyrorgog')
        
    