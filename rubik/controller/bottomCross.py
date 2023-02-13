import rubik.model.constants
from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomCross(theCube: Cube) -> str:
    if doesBottomCrossExist(theCube):
        return theCube
        

def doesBottomCrossExist(cube):
    if cube[FMM] != cube[FBM]:
        return False
    elif cube[LMM] != cube[LBM]:
        return False
    elif cube[RMM] != cube[RBM]:
        return False
    elif cube[BMM] != cube[BBM]:
        return False
    elif cube[DMM] != cube[DTM]:
        return False
    elif cube[DMM] != cube[DML]:
        return False
    elif cube[DMM] != cube[DMR]:
        return False
    elif cube[DMM] != cube[DBM]:
        return False
    return True
