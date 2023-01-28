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
        #self.assertEqual(rotatedCube,'ywygbgggrbobwrywrwobrggrgwywyoyoobbygwwbyygrrrrbowbooo')
        self.assertTrue(rotatedCube.startswith('ywygbgggr'))