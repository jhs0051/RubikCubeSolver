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
        for rotationDirection in directions:
            match rotationDirection:
                case 'F':
                    self._rotateF()
                case 'f':
                    self._rotatef()
                case 'R':
                    self._rotateR()
                case 'r':
                    self._rotater()
                case 'B':
                    self._rotateB()
                case 'b':
                    self._rotateb()
                case 'L':
                    self._rotateL()
                case 'l':
                    self._rotatel()
                case 'U':
                    self._rotateU()
                case 'u':
                    self._rotateu() 
        
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

        # rotate right to top
        rotatedCubeList[UBL] = self._cubeModel[RTL]
        rotatedCubeList[UBM] = self._cubeModel[RML]
        rotatedCubeList[UBR] = self._cubeModel[RBL]

        # rotate left to bottom
        rotatedCubeList[DTL] = self._cubeModel[LTR]
        rotatedCubeList[DTM] = self._cubeModel[LMR]
        rotatedCubeList[DTR] = self._cubeModel[LBR]

        # rotate top to left
        rotatedCubeList[LBR] = self._cubeModel[UBL]
        rotatedCubeList[LMR] = self._cubeModel[UBM]
        rotatedCubeList[LTR] = self._cubeModel[UBR]

        # rotate bottom to right
        rotatedCubeList[RBL] = self._cubeModel[DTL]
        rotatedCubeList[RML] = self._cubeModel[DTM]
        rotatedCubeList[RTL] = self._cubeModel[DTR]
        
        self._cubeModel = ''.join(rotatedCubeList)
        
    def _rotateR(self):
        rotatedCubeList = self._cubeModel[:]
        
        # rotate right face
        rotatedCubeList[RTR] = self._cubeModel[RTL]
        rotatedCubeList[RMR] = self._cubeModel[RTM]
        rotatedCubeList[RBR] = self._cubeModel[RTR]
        rotatedCubeList[RTM] = self._cubeModel[RML]
        rotatedCubeList[RMM] = self._cubeModel[RMM]
        rotatedCubeList[RBM] = self._cubeModel[RMR]
        rotatedCubeList[RTL] = self._cubeModel[RBL]
        rotatedCubeList[RML] = self._cubeModel[RBM]
        rotatedCubeList[RBL] = self._cubeModel[RBR]

        # rotate top to back
        rotatedCubeList[BTL] = self._cubeModel[UBR]
        rotatedCubeList[BML] = self._cubeModel[UMR]
        rotatedCubeList[BBL] = self._cubeModel[UTR]
        
        # rotate front to top  
        rotatedCubeList[UTR] = self._cubeModel[FTR]
        rotatedCubeList[UMR] = self._cubeModel[FMR]
        rotatedCubeList[UBR] = self._cubeModel[FBR]

        # rotate back to bottom
        rotatedCubeList[DBR] = self._cubeModel[BTL]
        rotatedCubeList[DMR] = self._cubeModel[BML]
        rotatedCubeList[DTR] = self._cubeModel[BBL]

        # rotate bottom to front
        rotatedCubeList[FTR] = self._cubeModel[DTR]
        rotatedCubeList[FMR] = self._cubeModel[DMR]
        rotatedCubeList[FBR] = self._cubeModel[DBR]
        
        self._cubeModel = ''.join(rotatedCubeList)
    
    def _rotater(self):
        rotatedCubeList = self._cubeModel[:]
        
        # rotate right face
        rotatedCubeList[RBL] = self._cubeModel[RTL]
        rotatedCubeList[RML] = self._cubeModel[RTM]
        rotatedCubeList[RTL] = self._cubeModel[RTR]
        rotatedCubeList[RBM] = self._cubeModel[RML]
        rotatedCubeList[RMM] = self._cubeModel[RMM]
        rotatedCubeList[RTM] = self._cubeModel[RMR]
        rotatedCubeList[RBR] = self._cubeModel[RBL]
        rotatedCubeList[RMR] = self._cubeModel[RBM]
        rotatedCubeList[RTR] = self._cubeModel[RBR]

        # rotate front to bottom
        rotatedCubeList[DTR] = self._cubeModel[FTR]
        rotatedCubeList[DMR] = self._cubeModel[FMR]
        rotatedCubeList[DBR] = self._cubeModel[FBR]

        # rotate bottom to up
        rotatedCubeList[UBR] = self._cubeModel[BTL]
        rotatedCubeList[UMR] = self._cubeModel[BML]
        rotatedCubeList[UTR] = self._cubeModel[BBL]

        # rotate up to front
        rotatedCubeList[FBR] = self._cubeModel[UBR]
        rotatedCubeList[FMR] = self._cubeModel[UMR]
        rotatedCubeList[FTR] = self._cubeModel[UTR]

        # rotate bottom to back
        rotatedCubeList[BBL] = self._cubeModel[DTR]
        rotatedCubeList[BML] = self._cubeModel[DMR]
        rotatedCubeList[BTL] = self._cubeModel[DBR]
        
        self._cubeModel = ''.join(rotatedCubeList)
    
    def _rotateB(self):
        rotatedCubeList = self._cubeModel[:]
        
        # rotate back face
        rotatedCubeList[BTR] = self._cubeModel[BTL]
        rotatedCubeList[BMR] = self._cubeModel[BTM]
        rotatedCubeList[BBR] = self._cubeModel[BTR]
        rotatedCubeList[BTM] = self._cubeModel[BML]
        rotatedCubeList[BMM] = self._cubeModel[BMM]
        rotatedCubeList[BBM] = self._cubeModel[BMR]
        rotatedCubeList[BTL] = self._cubeModel[BBL]
        rotatedCubeList[BML] = self._cubeModel[BBM]
        rotatedCubeList[BBL] = self._cubeModel[BBR]

        # rotate right to top
        rotatedCubeList[UTL] = self._cubeModel[RTR]
        rotatedCubeList[UTM] = self._cubeModel[RMR]
        rotatedCubeList[UTR] = self._cubeModel[RBR]

        # rotate left to bottom
        rotatedCubeList[DBL] = self._cubeModel[LTL]
        rotatedCubeList[DBM] = self._cubeModel[LML]
        rotatedCubeList[DBR] = self._cubeModel[LBL]

        # rotate bottom to right
        rotatedCubeList[RBR] = self._cubeModel[DBL]
        rotatedCubeList[RMR] = self._cubeModel[DBM]
        rotatedCubeList[RTR] = self._cubeModel[DBR]

        # rotate top to left
        rotatedCubeList[LBL] = self._cubeModel[UTL]
        rotatedCubeList[LML] = self._cubeModel[UTM]
        rotatedCubeList[LTL] = self._cubeModel[UTR]
        
        self._cubeModel = ''.join(rotatedCubeList)
    
    def _rotateb(self):
        rotatedCubeList = self._cubeModel[:]
        
        # rotate back face
        rotatedCubeList[BBL] = self._cubeModel[BTL]
        rotatedCubeList[BML] = self._cubeModel[BTM]
        rotatedCubeList[BTL] = self._cubeModel[BTR]
        rotatedCubeList[BBM] = self._cubeModel[BML]
        rotatedCubeList[BMM] = self._cubeModel[BMM]
        rotatedCubeList[BTM] = self._cubeModel[BMR]
        rotatedCubeList[BBR] = self._cubeModel[BBL]
        rotatedCubeList[BMR] = self._cubeModel[BBM]
        rotatedCubeList[BTR] = self._cubeModel[BBR]

        # rotate right to bottom
        rotatedCubeList[DBR] = self._cubeModel[RTR]
        rotatedCubeList[DBM] = self._cubeModel[RMR]
        rotatedCubeList[DBL] = self._cubeModel[RBR]

        # rotate top to right
        rotatedCubeList[RTR] = self._cubeModel[UTL]
        rotatedCubeList[RMR] = self._cubeModel[UTM]
        rotatedCubeList[RBR] = self._cubeModel[UTR]

        # rotate left to top
        rotatedCubeList[UTR] = self._cubeModel[LTL]
        rotatedCubeList[UTM] = self._cubeModel[LML]
        rotatedCubeList[UTL] = self._cubeModel[LBL]

        # rotate bottom to left
        rotatedCubeList[LTL] = self._cubeModel[DBL]
        rotatedCubeList[LML] = self._cubeModel[DBM]
        rotatedCubeList[LBL] = self._cubeModel[DBR]
        
        self._cubeModel = ''.join(rotatedCubeList)
    
    def _rotateL(self):
        pass
    
    def _rotatel(self):
        pass
    
    def _rotateU(self):
        pass
    
    def _rotateu(self):
        pass

        