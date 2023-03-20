from rubik.model.constants import *

def _solveMiddleLayer(theCube, solution) -> str:
    if _isMiddleLayerSolved(theCube):
        return theCube, solution
    
    return _solveMiddleLayer(theCube, solution)

def _isMiddleLayerSolved(theCube):
    if theCube[FML] != theCube[FMM]:
        return False
    elif theCube[FMR] != theCube[FMM]:
        return False
    elif theCube[LML] != theCube[LMM]:
        return False
    elif theCube[LMR] != theCube[LMM]:
        return False
    elif theCube[RML] != theCube[RMM]:
        return False
    elif theCube[RMR] != theCube[RMM]:
        return False
    elif theCube[BML] != theCube[BMM]:
        return False
    elif theCube[BMR] != theCube[BMM]:
        return False
    return True

def _rotateMiddlePieceFromTopToMiddle(theCube, currentCubeIndex):
    pass