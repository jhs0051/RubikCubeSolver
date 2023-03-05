from rubik.model.constants import *
from rubik.view.rotate import rotate
from rubik.model.cube import Cube

def solveBottomLayer(theCube: Cube, solution) -> str:
    startingCubeIndex = FTL
    
    if isBottomLayerSolved(theCube):
        return theCube, solution
    
    currentCubeIndex = doBottomEdgePieceColorsMatch(theCube)

    if currentCubeIndex is None:
        theCube, currentCubeIndex, currentDirectionList = rotateBottomEdgePieceToTopEdgePiece(theCube)
        solution += currentDirectionList

    if currentCubeIndex is None:
        currentCubeIndex = rotateBottomEdgesInCorrectPosition(theCube)
    elif currentCubeIndex is not None:
        theCube, currentCubeIndex, currentDirectionList = rotateEdgePieceToDifferentFace(theCube, currentCubeIndex)
        solution += currentDirectionList

        theCube, currentCubeIndex, currentDirectionList = rotateBottomEdgePieceToTopEdgePiece(theCube, currentCubeIndex)
        solution += currentDirectionList

    if startingCubeIndex < FML:
        while not doBottomColorsMatchBottomFaceColors(theCube, currentCubeIndex):
            theCube, currentCubeIndex, currentDirectionList = rotateBottomEdgeCW(theCube, currentCubeIndex)
            solution += currentDirectionList
            startingCubeIndex += FTM

    return solveBottomLayer(theCube, solution)

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

def doBottomEdgePieceColorsMatch(theCube):
    currentCubeIndex = None
    topEdgePieces = [(theCube[FTR], theCube[RTL], theCube[UBR]), (theCube[RTR], theCube[BTL], theCube[UTR]),
                     (theCube[BTR], theCube[LTL], theCube[UTL]), (theCube[LTR], theCube[FTL], theCube[UBL])]

    for cubePiece, edgePiece in enumerate(topEdgePieces):
        if edgePiece.count(theCube[DMM]) > FTL:
            currentCubeIndex = FTR + cubePiece * RTL

    return currentCubeIndex

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
    if currentCubeIndex is not None:
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

        return theCube, currentCubeIndex, directionList
    
    if currentCubeIndex is None:
        directionList = ''

        bottomEdgePieces = [(theCube[FMM], theCube[RMM], theCube[DMM]), (theCube[RMM], theCube[BMM], theCube[DMM]),
                            (theCube[BMM], theCube[LMM], theCube[DMM]), (theCube[LMM], theCube[FMM], theCube[DMM])]

        currentEdgePieces = [(theCube[FBR], theCube[RBL], theCube[DTR]), (theCube[RBR], theCube[BBL], theCube[DBR]),
                             (theCube[BBR], theCube[LBL], theCube[DBL]), (theCube[LBR], theCube[FBL], theCube[DTL])]

        for cubePiece, edgePiece in enumerate(currentEdgePieces):
            if sorted(edgePiece) != edgePiece.count(theCube[DMM]):
                if sorted(bottomEdgePieces[cubePiece]):
                    theCube, currentCubeIndex, directionList = \
                        rotateBottomEdgePieceToTopEdgePiece(theCube, FTR + cubePiece * RTL)
                    currentCubeIndex = FTR + cubePiece * RTL
                    break

        return theCube, currentCubeIndex, directionList

def rotateBottomEdgeCW(theCube, currentCubeIndex):
    cube = 'cube'
    direction = 'dir'
    directionList = ''

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

def doBottomColorsMatchBottomFaceColors(theCube, currentCubeIndex):
    if currentCubeIndex is LBR:
        if theCube[DTL] is theCube[DMM]:
            return True
    elif currentCubeIndex is FBR:
        if theCube[DTR] is theCube[DMM]:
            return True
    elif currentCubeIndex is BBR:
        if theCube[DBL] is theCube[DMM]:
            return True
    elif currentCubeIndex is RBR:
        if theCube[DBR] is theCube[DMM]:
            return True
        
def rotateBottomEdgesInCorrectPosition(theCube):
    currentCubeIndex = None

    bottomEdgePieces = [(theCube[FMM], theCube[RMM], theCube[DMM]), (theCube[RMM], theCube[BMM], theCube[DMM]),
                        (theCube[BMM], theCube[LMM], theCube[DMM]), (theCube[LMM], theCube[FMM], theCube[DMM])]

    currentEdgePieces = [(theCube[FBR], theCube[RBL], theCube[DTR]), (theCube[RBR], theCube[BBL], theCube[DBR]),
                         (theCube[BBR], theCube[LBL], theCube[DBL]), (theCube[LBR], theCube[FBL], theCube[DTL])]

    for cubePiece, edgePiece in enumerate(currentEdgePieces):
        if sorted(bottomEdgePieces[cubePiece]) == sorted(edgePiece):
            if bottomEdgePieces[cubePiece][FTR] != edgePiece[FTR]:
                currentCubeIndex = FBR + cubePiece * RTL
                break

    return currentCubeIndex


