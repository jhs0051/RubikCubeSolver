from rubik.model.constants import *

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, encodedCube):
        self.cube = encodedCube
        
    def rotate(self, directions):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        
        # rotate front face
        rotatedCubeList[2] = cubeList[0]
        rotatedCubeList[5] = cubeList[1]
        rotatedCubeList[8] = cubeList[2]
        rotatedCubeList[1] = cubeList[3]
        rotatedCubeList[4] = cubeList[4]
        rotatedCubeList[7] = cubeList[5]
        rotatedCubeList[0] = cubeList[6]
        rotatedCubeList[3] = cubeList[7]
        rotatedCubeList[6] = cubeList[8]
        
        self.cube = "".join(rotatedCubeList)
        return self.cube
    
    def get(self):
        return self.cube
        