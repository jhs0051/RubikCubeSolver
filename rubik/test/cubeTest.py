'''
Created on Jan 28, 2023

@author: jonhoustonseibert
'''
import unittest
import rubik.model.cube as cube


class CubeTest(unittest.TestCase):


    def test_rotate_010_ShouldRotateCubeInFDirection(self):
        cubeToRotate = 'ygrwbayggbobrryrnwobrgargwywy.ryorbbagwubyybwwooyowbooo'
        theCube = cube. Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F')
        self. assertEqual (rotatedCube,'ywygbgggrbobwrywrwobrggrqwywyoyoobbygwwbyygrrrrbowbooo')
