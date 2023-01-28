from rubik.model.constants import *

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, encodedCube):
        self._cubeModel = encodedCube
    
    def get(self):
        return "".join(self._cubeModel)
        
    def rotate(self, directions):
        self._rotateF()
        return self._cubeModel
    

    def _rotateF(self):
        rotatedCubeList = self._cubeModel[:]
        
        # rotate front face
        rotatedCubeList[FTR] = self._cubeModel[FTL]
        rotatedCubeList[FMR] = self._cubeModel[FTM]
        rotatedCubeList[FBR] = self._cubeModel[FTR]
        rotatedCubeList[FTM] = self._cubeModel[FML]
        rotatedCubeList[FMM] = self._cubeModel[FMM]
        rotatedCubeList[FBM] = self._cubeModel[FMR]
        rotatedCubeList[FTL] = self._cubeModel[FBL]
        rotatedCubeList[FML] = self._cubeModel[FBM]
        rotatedCubeList[FBL] = self._cubeModel[FBR]
                             
        # rotate up to right
        rotatedCubeList[RTL] = self._cubeModel[UBL]
        rotatedCubeList[RML] = self._cubeModel[UBM]
        rotatedCubeList[RBL] = self._cubeModel[UBR]
                        
        #rotate right to bottom 
        rotatedCubeList[DTR] = self._cubeModel[RTL]
        rotatedCubeList[DTM] = self._cubeModel[RML]
        rotatedCubeList[DTL] = self._cubeModel[RBL]
                               
        #rotate bottom to left 
        rotatedCubeList[LTR] = self._cubeModel[DTL]
        rotatedCubeList[LMR] = self._cubeModel[DTM]
        rotatedCubeList[LBR] = self._cubeModel[DTR]
                            
        #rotate left to top
        rotatedCubeList[UBR] = self._cubeModel[LTR]
        rotatedCubeList[UBM] = self._cubeModel[LMR]
        rotatedCubeList[UBL] = self._cubeModel[LBR]
        
        self._cubeModel = "".join(rotatedCubeList)

        