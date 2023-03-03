from rubik.model.constants import *
from rubik.view.rotate import rotate
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
    cube = 'cube'
    direction = 'dir'
    directionList = ''

    bottomEdgePieces = [(theCube[FMM], theCube[RMM], theCube[DMM]), (theCube[RMM], theCube[BMM], theCube[DMM]),
                          (theCube[BMM], theCube[LMM], theCube[DMM]), (theCube[LMM], theCube[FMM], theCube[DMM])]

    topEdgePieces = [(theCube[FTR], theCube[RTL], theCube[UBR]), (theCube[RTR], theCube[BTL], theCube[UTR]),
                       (theCube[BTR], theCube[LTL], theCube[UTL]), (theCube[LTR], theCube[FTL], theCube[UBL])]

    while sorted(bottomEdgePieces[int((currentCubeIndex - FTR) / RTL)]) \
            != sorted(topEdgePieces[int((currentCubeIndex - FTR) / RTL)]):
        directionList = directionList + 'U'
        theCube = {cube: theCube, direction: 'U'}
        theCube = rotate(theCube)[cube]
        
        if currentCubeIndex != FTR:
            currentCubeIndex = currentCubeIndex - RTL
        else:
            currentCubeIndex = LTR

        topEdgePieces = [(theCube[FTR], theCube[RTL], theCube[UBR]), (theCube[RTR], theCube[BTL], theCube[UTR]),
                         (theCube[BTR], theCube[LTL], theCube[UTL]), (theCube[LTR], theCube[FTL], theCube[UBL])]

    return theCube, currentCubeIndex, directionList

def rotateBottomEdgePieceToTopEdgePiece(theCube, currentCubeIndex):
    cube = 'cube'
    direction = 'dir'
    directionList = ''

    if currentCubeIndex is LTR:
        directionList += 'FUfu'
    elif currentCubeIndex is RTR:
        directionList += 'BUbu'
    elif currentCubeIndex is BTR:
        directionList += 'LUlu'
    elif currentCubeIndex is FTR:
        directionList += 'RUru'

    parms = {cube: theCube, direction: directionList}
    theCube = rotate(parms)[cube]
    currentCubeIndex += FBL
    
    if currentCubeIndex is LBR:
        directionList += 'FUfuFUfu'
    elif currentCubeIndex is RBR:
        directionList += 'BUbuBUbu'
    elif currentCubeIndex is BBR:
        directionList += 'LUluLUlu'
    elif currentCubeIndex is FBR:
        directionList += 'RUruRUru'

    parms = {cube: theCube, direction: directionList}
    theCube = rotate(parms)[cube]

    return theCube, currentCubeIndex, directionList

