from rubik.model.constants import *
from rubik.view.rotate import rotate

def _solveBottomLayer(theCube, solution) -> str:
    startingCubeIndex = FTL
    
    if _isBottomLayerSolved(theCube):
        return theCube, solution
    
    currentCubeIndex = _doBottomEdgePieceColorsMatch(theCube)

    if currentCubeIndex is None:
        theCube, currentCubeIndex, currentDirectionList = _rotateBottomEdgePieceToTopEdge(theCube)
        solution += currentDirectionList

    if currentCubeIndex is None:
        currentCubeIndex = _rotateBottomEdgesInCorrectPosition(theCube)
    elif currentCubeIndex is not None:
        theCube, currentCubeIndex, currentDirectionList = _rotateEdgePieceToDifferentFace(theCube, currentCubeIndex)
        solution += currentDirectionList

        theCube, currentCubeIndex, currentDirectionList = _rotateBottomEdgePieceToTopEdgePiece(theCube, currentCubeIndex)
        solution += currentDirectionList

    if startingCubeIndex < FML:
        while not _doBottomColorsMatchBottomFaceColors(theCube, currentCubeIndex):
            theCube, currentCubeIndex, currentDirectionList = _rotateBottomEdgeCW(theCube, currentCubeIndex)
            solution += currentDirectionList
            startingCubeIndex += FTM

    return _solveBottomLayer(theCube, solution)

def _isBottomLayerSolved(theCube):
    for currentCubeFace, matchingCubeFace in [(FMM, FBL), (FMM, FBR), (RMM, RBL), (RMM, RBR), (BMM, BBL), (BMM, BBR),
                                              (LMM, LBL), (LMM, LBR), (DMM, DTL), (DMM, DTR), (DMM, DBL), (DMM, DBR)]:
        if theCube[currentCubeFace] is not theCube[matchingCubeFace]:
            return False
    return True

def _doBottomEdgePieceColorsMatch(theCube):
    currentCubeIndex = None
    topEdgePieces = [(theCube[FTR], theCube[RTL], theCube[UBR]), (theCube[RTR], theCube[BTL], theCube[UTR]),
                     (theCube[BTR], theCube[LTL], theCube[UTL]), (theCube[LTR], theCube[FTL], theCube[UBL])]

    for cubePiece, edgePiece in enumerate(topEdgePieces):
        if edgePiece.count(theCube[DMM]) > FTL:
            currentCubeIndex = FTR + cubePiece * RTL
            break

    return currentCubeIndex

def _rotateEdgePieceToDifferentFace(theCube, currentCubeIndex):
    cube = 'cube'
    direction = 'dir'
    directionList = ''

    bottomEdgePieces = [(theCube[FMM], theCube[RMM], theCube[DMM]), (theCube[RMM], theCube[BMM], theCube[DMM]),
                          (theCube[BMM], theCube[LMM], theCube[DMM]), (theCube[LMM], theCube[FMM], theCube[DMM])]

    topEdgePieces = [(theCube[FTR], theCube[RTL], theCube[UBR]), (theCube[RTR], theCube[BTL], theCube[UTR]),
                       (theCube[BTR], theCube[LTL], theCube[UTL]), (theCube[LTR], theCube[FTL], theCube[UBL])]

    while sorted(bottomEdgePieces[int((currentCubeIndex - FTR) / RTL)]) \
            != sorted(topEdgePieces[int((currentCubeIndex - FTR) / RTL)]):
        directionList += 'U'
        theCube = rotate({cube: theCube, direction: 'U'})[cube]
        
        if currentCubeIndex != FTR:
            currentCubeIndex = currentCubeIndex - RTL
        else:
            currentCubeIndex = LTR

        topEdgePieces = [(theCube[FTR], theCube[RTL], theCube[UBR]), (theCube[RTR], theCube[BTL], theCube[UTR]),
                         (theCube[BTR], theCube[LTL], theCube[UTL]), (theCube[LTR], theCube[FTL], theCube[UBL])]

    return theCube, currentCubeIndex, directionList

def _rotateBottomEdgePieceToTopEdgePiece(theCube, currentCubeIndex):
    cube = 'cube'
    direction = 'dir'
    directionList = ''

    directions = {LTR: 'FUfu', RTR: 'BUbu', BTR: 'LUlu', FTR: 'RUru'}
    directionList += directions[currentCubeIndex]

    theCube = rotate({cube: theCube, direction: directionList})[cube]
    currentCubeIndex += FBL

    return theCube, currentCubeIndex, directionList

def _rotateBottomEdgePieceToTopEdge(theCube):
    currentCubeIndex = None
    directionList = ''

    bottomEdgePieces = [(theCube[FMM], theCube[RMM], theCube[DMM]), (theCube[RMM], theCube[BMM], theCube[DMM]),
                        (theCube[BMM], theCube[LMM], theCube[DMM]), (theCube[LMM], theCube[FMM], theCube[DMM])]

    currentEdgePieces = [(theCube[FBR], theCube[RBL], theCube[DTR]), (theCube[RBR], theCube[BBL], theCube[DBR]),
                         (theCube[BBR], theCube[LBL], theCube[DBL]), (theCube[LBR], theCube[FBL], theCube[DTL])]

    for cubePiece, edgePiece in enumerate(currentEdgePieces):
        if edgePiece.count(theCube[DMM]):
            if sorted(edgePiece) != sorted(bottomEdgePieces[cubePiece]):
                theCube, currentCubeIndex, directionList = \
                    _rotateBottomEdgePieceToTopEdgePiece(theCube, FTR + cubePiece * RTL)
                currentCubeIndex = FTR + cubePiece * RTL
                break

    return theCube, currentCubeIndex, directionList

def _rotateBottomEdgeCW(theCube, currentCubeIndex):
    cube = 'cube'
    direction = 'dir'
    directionList = ''

    directions = {LBR: 'FUfuFUfu', RBR: 'BUbuBUbu', BBR: 'LUluLUlu', FBR: 'RUruRUru'}
    directionList += directions[currentCubeIndex]

    theCube = rotate({cube: theCube, direction: directionList})[cube]

    return theCube, currentCubeIndex, directionList

def _doBottomColorsMatchBottomFaceColors(theCube, currentCubeIndex):
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
        
def _rotateBottomEdgesInCorrectPosition(theCube):
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
