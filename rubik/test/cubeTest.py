'''
Created on Jan 28, 2023

@author: jonhoustonseibert
'''
import unittest
import rubik.model.cube as cube


class CubeTest(unittest.TestCase):


    def test_rotate_010_ShouldRotateCubeInFDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F')
        self.assertEqual(rotatedCube,'ywygbgggrbobwrywrwobrggrgwywyoyoobbygwwbyygrrrrbowbooo')
    
    def test_rotate_020_ShouldRotateCubeInfDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('f')
        self.assertEqual(rotatedCube,'rgggbgywyyoboryorwobrggrgwywywyowbbbgwwbyybrrrrgowbooo')
    
    def test_rotate_030_ShouldRotateCubeInRDirection(self):
        cubeToRotate = 'ygyrbwworoyygywbbogryrgybygwywwrboorgoogoobrbgbwgwwrbr'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('R')
        self.assertEqual(rotatedCube,'ygwrbwworbgobyyowybryogyoygwywwrboorgoygowbrrgbbgwrrbg')
        
    def test_rotate_040_ShouldRotateCubeInrDirection(self):
        cubeToRotate = 'gyrbgwgbbbwryyoogywryrrygbygborbrrywowywwgbowbgrgoooow'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('r')
        self.assertEqual(rotatedCube,'gyybgggbwroywygbyowryoryrbygborbrrywowgwwrbowbgrgowoob')
        
    def test_rotate_050_ShouldRotateCubeInBDirection(self):
        cubeToRotate = 'ygboboyybgbrrowgwgbooyybyorbggrgyyyowbobrwwrwwgrrwgowr'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('B')
        self.assertEqual(rotatedCube,'ygboboyybgbrrowgwoyyboyorbooggbgywyorwgbrwwrwwgrrwgbry')
        
    def test_rotate_060_ShouldRotateCubeInbDirection(self):
        cubeToRotate = 'oyrybyobbyooogbrobrwwrowwgygbygyrorgbbggrrwwbwyggwwroy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('b')
        self.assertEqual(rotatedCube,'oyrybyobbyobogbrogwwywogrrwrbyoyryrgogggrrwwbwyggwwbbo')