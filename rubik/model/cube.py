from rubik.model.constants import *

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, encodedCube):
        self._cubeModel = list(encodedCube)
    
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
        
    def _rotatef(self):
        rotatedCubeList = self._cubeModel[:]
        
        # rotate front face
        rotatedCubeList[FBL] = self._cubeModel[FTL]
        rotatedCubeList[FML] = self._cubeModel[FTM]
        rotatedCubeList[FTL] = self._cubeModel[FTR]
        rotatedCubeList[FBM] = self._cubeModel[FML]
        rotatedCubeList[FMM] = self._cubeModel[FMM]
        rotatedCubeList[FTM] = self._cubeModel[FMR]
        rotatedCubeList[FBR] = self._cubeModel[FBL]
        rotatedCubeList[FMR] = self._cubeModel[FBM]
        rotatedCubeList[FTR] = self._cubeModel[FBR]

        # rotate up to right
        rotatedCubeList[UBL] = self._cubeModel[RTL]
        rotatedCubeList[UBM] = self._cubeModel[RML]
        rotatedCubeList[UBR] = self._cubeModel[RBL]

        # rotate bottom to left
        rotatedCubeList[DTL] = self._cubeModel[LTR]
        rotatedCubeList[DTM] = self._cubeModel[LMR]
        rotatedCubeList[DTR] = self._cubeModel[LBR]

        # rotate up to left
        rotatedCubeList[LBR] = self._cubeModel[UBL]
        rotatedCubeList[LMR] = self._cubeModel[UBM]
        rotatedCubeList[LTR] = self._cubeModel[UBR]

        # rotate bottom to right
        rotatedCubeList[RBL] = self._cubeModel[DTL]
        rotatedCubeList[RML] = self._cubeModel[DTM]
        rotatedCubeList[RTL] = self._cubeModel[DTR]
        
        self._cubeModel = ''.join(rotatedCubeList)
    
    

        