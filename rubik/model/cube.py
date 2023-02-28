from rubik.model.constants import *
from collections import Counter

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, encodedCube):
        self._cubeModel = list(encodedCube)
    
    def get(self):
        return "".join(self._cubeModel)
    
    @staticmethod
    def _validation(encodedCube, directions):
        cube = encodedCube
        middleColorsList = list()
        
        if len(cube) != validCubeLength:
            return False
        
        middleColorsList.append(cube[FMM])
        middleColorsList.append(cube[RMM])
        middleColorsList.append(cube[BMM])
        middleColorsList.append(cube[LMM])
        middleColorsList.append(cube[UMM])
        middleColorsList.append(cube[DMM])
        
        for currentSquare in middleColorsList:
            if middleColorsList.count(currentSquare) > FTM:
                return False   
        
        for value in Counter(cube).values():
            if value != validCubeColorCount:
                return False
        
        if any(character not in validCharacters for character in cube):
            return False
        
        if directions == '' or directions == None:
            return True
        elif any(letter not in validDirections for letter in directions):
            return False 
        else:
            return True
        
    def rotate(self, directions):
        if directions == '' or directions == None:
            self._rotate_F()
        else:
            for rotationDirection in directions:
                match rotationDirection:
                    case 'F': self._rotate_F()
                    case 'f': self._rotate_f()
                    case 'R': self._rotate_R()
                    case 'r': self._rotate_r()
                    case 'B': self._rotate_B()
                    case 'b': self._rotate_b()
                    case 'L': self._rotate_L()
                    case 'l': self._rotate_l()
                    case 'U': self._rotate_U()
                    case 'u': self._rotate_u() 
                    case '':  self._rotate_F()
                    case _: 
                        return False
            
        return self._cubeModel
    

    def _rotate_F(self):
        cubeList = list(self._cubeModel)
        rotatedCubeList = cubeList[:]
        
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
        
    def _rotate_f(self):
        cubeList = list(self._cubeModel)
        rotatedCubeList = cubeList[:]
        
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
        
    def _rotate_R(self):
        cubeList = list(self._cubeModel)
        rotatedCubeList = cubeList[:]
        
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
    
    def _rotate_r(self):
        cubeList = list(self._cubeModel)
        rotatedCubeList = cubeList[:]
        
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
    
    def _rotate_B(self):
        cubeList = list(self._cubeModel)
        rotatedCubeList = cubeList[:]
        
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
    
    def _rotate_b(self):
        cubeList = list(self._cubeModel)
        rotatedCubeList = cubeList[:]
        
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
    
    def _rotate_L(self):
        cubeList = list(self._cubeModel)
        rotatedCubeList = cubeList[:]
        
        # rotate left face
        rotatedCubeList[LTR] = self._cubeModel[LTL]
        rotatedCubeList[LMR] = self._cubeModel[LTM]
        rotatedCubeList[LBR] = self._cubeModel[LTR]
        rotatedCubeList[LTM] = self._cubeModel[LML]
        rotatedCubeList[LMM] = self._cubeModel[LMM]
        rotatedCubeList[LBM] = self._cubeModel[LMR]
        rotatedCubeList[LTL] = self._cubeModel[LBL]
        rotatedCubeList[LML] = self._cubeModel[LBM]
        rotatedCubeList[LBL] = self._cubeModel[LBR]

        # rotate top to front 
        rotatedCubeList[FTL] = self._cubeModel[UTL]
        rotatedCubeList[FML] = self._cubeModel[UML]
        rotatedCubeList[FBL] = self._cubeModel[UBL]

        # rotate bottom to back
        rotatedCubeList[BBR] = self._cubeModel[DTL]
        rotatedCubeList[BMR] = self._cubeModel[DML]
        rotatedCubeList[BTR] = self._cubeModel[DBL]
        
        # rotate front to bottom
        rotatedCubeList[DTL] = self._cubeModel[FTL]
        rotatedCubeList[DML] = self._cubeModel[FML]
        rotatedCubeList[DBL] = self._cubeModel[FBL]

        # rotate back to top
        rotatedCubeList[UBL] = self._cubeModel[BTR]
        rotatedCubeList[UML] = self._cubeModel[BMR]
        rotatedCubeList[UTL] = self._cubeModel[BBR]
        
        self._cubeModel = ''.join(rotatedCubeList)
    
    def _rotate_l(self):
        cubeList = list(self._cubeModel)
        rotatedCubeList = cubeList[:]
        
        # rotate left face
        rotatedCubeList[LBL] = self._cubeModel[LTL]
        rotatedCubeList[LML] = self._cubeModel[LTM]
        rotatedCubeList[LTL] = self._cubeModel[LTR]
        rotatedCubeList[LBM] = self._cubeModel[LML]
        rotatedCubeList[LMM] = self._cubeModel[LMM]
        rotatedCubeList[LTM] = self._cubeModel[LMR]
        rotatedCubeList[LBR] = self._cubeModel[LBL]
        rotatedCubeList[LMR] = self._cubeModel[LBM]
        rotatedCubeList[LTR] = self._cubeModel[LBR]

        # rotate back to front
        rotatedCubeList[FTL] = self._cubeModel[DTL]
        rotatedCubeList[FML] = self._cubeModel[DML]
        rotatedCubeList[FBL] = self._cubeModel[DBL]
        
        # rotate front to top
        rotatedCubeList[UTL] = self._cubeModel[FTL]
        rotatedCubeList[UML] = self._cubeModel[FML]
        rotatedCubeList[UBL] = self._cubeModel[FBL]

        # rotate back to bottom
        rotatedCubeList[DBL] = self._cubeModel[BTR]
        rotatedCubeList[DML] = self._cubeModel[BMR]
        rotatedCubeList[DTL] = self._cubeModel[BBR]

        # rotate top to back
        rotatedCubeList[BBR] = self._cubeModel[UTL]
        rotatedCubeList[BMR] = self._cubeModel[UML]
        rotatedCubeList[BTR] = self._cubeModel[UBL]
        
        self._cubeModel = ''.join(rotatedCubeList)
    
    def _rotate_U(self):
        cubeList = list(self._cubeModel)
        rotatedCubeList = cubeList[:]
        
        # rotate top
        rotatedCubeList[UTR] = self._cubeModel[UTL]
        rotatedCubeList[UMR] = self._cubeModel[UTM]
        rotatedCubeList[UBR] = self._cubeModel[UTR]
        rotatedCubeList[UTM] = self._cubeModel[UML]
        rotatedCubeList[UMM] = self._cubeModel[UMM]
        rotatedCubeList[UBM] = self._cubeModel[UMR]
        rotatedCubeList[UTL] = self._cubeModel[UBL]
        rotatedCubeList[UML] = self._cubeModel[UBM]
        rotatedCubeList[UBL] = self._cubeModel[UBR]

        # rotate bottom to right 
        rotatedCubeList[RTL] = self._cubeModel[BTL]
        rotatedCubeList[RTM] = self._cubeModel[BTM]
        rotatedCubeList[RTR] = self._cubeModel[BTR]
        
        # rotate front to left
        rotatedCubeList[LTL] = self._cubeModel[FTL]
        rotatedCubeList[LTM] = self._cubeModel[FTM]
        rotatedCubeList[LTR] = self._cubeModel[FTR]
        
        # rotate left to bottom
        rotatedCubeList[BTL] = self._cubeModel[LTL]
        rotatedCubeList[BTM] = self._cubeModel[LTM]
        rotatedCubeList[BTR] = self._cubeModel[LTR]

        # rotate right to front
        rotatedCubeList[FTL] = self._cubeModel[RTL]
        rotatedCubeList[FTM] = self._cubeModel[RTM]
        rotatedCubeList[FTR] = self._cubeModel[RTR]
        
        self._cubeModel = ''.join(rotatedCubeList)
    
    def _rotate_u(self):
        cubeList = list(self._cubeModel)
        rotatedCubeList = cubeList[:]
        
        # rotate top
        rotatedCubeList[UBL] = self._cubeModel[UTL]
        rotatedCubeList[UML] = self._cubeModel[UTM]
        rotatedCubeList[UTL] = self._cubeModel[UTR]
        rotatedCubeList[UBM] = self._cubeModel[UML]
        rotatedCubeList[UMM] = self._cubeModel[UMM]
        rotatedCubeList[UTM] = self._cubeModel[UMR]
        rotatedCubeList[UBR] = self._cubeModel[UBL]
        rotatedCubeList[UMR] = self._cubeModel[UBM]
        rotatedCubeList[UTR] = self._cubeModel[UBR]

        # rotate front to right
        rotatedCubeList[RTL] = self._cubeModel[FTL]
        rotatedCubeList[RTM] = self._cubeModel[FTM]
        rotatedCubeList[RTR] = self._cubeModel[FTR]

        # rotate bottom to left 
        rotatedCubeList[LTL] = self._cubeModel[BTL]
        rotatedCubeList[LTM] = self._cubeModel[BTM]
        rotatedCubeList[LTR] = self._cubeModel[BTR]

        # rotate left to front
        rotatedCubeList[FTL] = self._cubeModel[LTL]
        rotatedCubeList[FTM] = self._cubeModel[LTM]
        rotatedCubeList[FTR] = self._cubeModel[LTR]

        # rotate right to bottom
        rotatedCubeList[BTL] = self._cubeModel[RTL]
        rotatedCubeList[BTM] = self._cubeModel[RTM]
        rotatedCubeList[BTR] = self._cubeModel[RTR]
        
        self._cubeModel = ''.join(rotatedCubeList)

        