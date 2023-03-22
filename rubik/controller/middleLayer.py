from rubik.model.constants import *
from rubik.view.rotate import _rotate

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
    cube = 'cube'
    direction = 'dir'
    directionList = ''

    if currentCubeIndex is LTM:
        if theCube[UML] is theCube[BMM]:
            directionList += 'ubUBULul'
        else:
            directionList += 'UFufulUL'
    elif currentCubeIndex is RTM:
        if theCube[UMR] is theCube[FMM]:
            directionList += 'ufUFURur'
        else: 
            directionList += 'UBuburUR'
    elif currentCubeIndex is BTM:
        if theCube[UTM] is theCube[RMM]:
            directionList += 'urURUBub'
        else:
            directionList += 'ULulubUB'
    elif currentCubeIndex is FTM:
        if theCube[UBM] is theCube[LMM]:
            directionList += 'ulULUFuf'
        else:
            directionList += 'URurufUF'

    theCube = {cube: theCube, direction: directionList}
    theCube = _rotate(theCube)[cube]

    return theCube, directionList    

def _rotateMiddlePieceFromMiddleToTop(theCube, currentCubeIndex):
    rotatedCubeIndex = currentCubeIndex - FMM
    theCube, directionList = _rotateMiddlePieceFromTopToMiddle(theCube, rotatedCubeIndex)

    if currentCubeIndex is LMR:
        currentCubeIndex = RTM
    elif currentCubeIndex is RMR:
        currentCubeIndex = LTM
    elif currentCubeIndex is BMR:
        currentCubeIndex = FTM
    elif currentCubeIndex is FMR:
        currentCubeIndex = BTM
    return theCube, currentCubeIndex, directionList

def _alignEdgePieceWithAnotherTopPiece(theCube, currentCubeIndex):
    cube = 'cube'
    direction = 'dir'
    directionList = ''

    while theCube[currentCubeIndex + FML] != theCube[currentCubeIndex]:
        directionList += 'U'
        theCube = {cube: theCube, direction: 'U'}
        theCube = _rotate(theCube)[cube]

        if currentCubeIndex != FTM:
            currentCubeIndex = currentCubeIndex - RTL
        else:
            currentCubeIndex = LTM

    return theCube, currentCubeIndex, directionList

def _matchCenterMiddlePieceWithOtherMiddleCenters(theCube):
    currentCubeIndex = None
    upperEdgePieces = [(theCube[FTM], theCube[UBM]), (theCube[RTM], theCube[UMR]), (theCube[BTM], theCube[UTM]),
                       (theCube[LTM], theCube[UML])]

    centerMiddlePieces = [sorted((theCube[LMM], theCube[FMM])), sorted((theCube[RMM], theCube[BMM])),
                          sorted((theCube[BMM], theCube[LMM])), sorted((theCube[FMM], theCube[RMM]))]

    for cubePiece, edgePiece in enumerate(upperEdgePieces):
        alignedEdgePieces = sorted(edgePiece)
        
        if centerMiddlePieces.count(alignedEdgePieces) > FTL:
            currentCubeIndex = FTM + cubePiece * RTL
            break

    return currentCubeIndex

def _alignCenterMiddlePieceWithEdgeMiddlePieces(theCube):
    pass
