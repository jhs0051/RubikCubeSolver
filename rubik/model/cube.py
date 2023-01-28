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
        rotatedCubeList[FTR] = cubeList[FTL]
        rotatedCubeList[FMR] = cubeList[FTM]
        rotatedCubeList[FBR] = cubeList[FTR]
        rotatedCubeList[FTM] = cubeList[FML]
        rotatedCubeList[FMM] = cubeList[FMM]
        rotatedCubeList[FBM] = cubeList[FMR]
        rotatedCubeList[FTL] = cubeList[FBL]
        rotatedCubeList[FML] = cubeList[FBM]
        rotatedCubeList[FBL] = cubeList[FBR]
        
        self.cube = "".join(rotatedCubeList)
        return self.cube
    
    def get(self):
        return self.cube
        