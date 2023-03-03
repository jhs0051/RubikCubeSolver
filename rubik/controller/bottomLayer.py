from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomLayer(theCube: Cube, solution) -> str:
    directionList = ''
    
    if isBottomLayerSolved(theCube):
        return theCube, solution

def isBottomLayerSolved(theCube):
    if theCube[FMM] != theCube[FBL]:
        return False
    elif theCube[FMM] != theCube[FBR]:
        return False
    elif theCube[RMM] != theCube[RBL]:
        return False
    elif theCube[RMM] != theCube[RBR]:
        return False
    elif theCube[BMM] != theCube[BBL]:
        return False
    elif theCube[BMM] != theCube[BBR]:
        return False
    elif theCube[LMM] != theCube[LBL]:
        return False
    elif theCube[LMM] != theCube[LBR]:
        return False
    elif theCube[DMM] != theCube[DTL]:
        return False
    elif theCube[DMM] != theCube[DTR]:
        return False
    elif theCube[DMM] != theCube[DBL]:
        return False
    elif theCube[DMM] != theCube[DBR]:
        return False
    return True

def rotateEdgePieceToDifferentFace(theCube, currentCubeIndex):
    pass
