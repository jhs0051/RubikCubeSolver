from rubik.model.constants import *
from rubik.view.rotate import rotate

def solveMiddleLayer(theCube, solution) -> str:
    if _isMiddleLayerSolved(theCube):
        return theCube, solution

    currentCubeIndex = _matchCenterMiddlePieceWithOtherMiddleCenters(theCube)

    if currentCubeIndex is None:
        currentCubeIndex = _alignCenterMiddlePieceWithEdgeMiddlePieces(theCube)
        theCube, currentCubeIndex, currentDirectionList = _rotateMiddlePieceFromMiddleToTop(theCube, currentCubeIndex)
        solution += currentDirectionList

    theCube, currentCubeIndex, currentDirectionList = _alignEdgePieceWithAnotherTopPiece(theCube, currentCubeIndex)
    solution += currentDirectionList

    theCube, currentDirectionList = _rotateMiddlePieceFromTopToMiddle(theCube, currentCubeIndex)
    solution += currentDirectionList

    return solveMiddleLayer(theCube, solution)

def _isMiddleLayerSolved(theCube):
    middleLayerCubeIndexes = [(FML, FMM), (FMR, FMM), (RML, RMM), (RMR, RMM), (BML, BMM), (BMR, BMM), (LML, LMM),
                              (LMR, LMM)]
    for matchingCubeFace, currentCubeFace in middleLayerCubeIndexes:
        if theCube[matchingCubeFace] is not theCube[currentCubeFace]:
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

    theCube = rotate({cube: theCube, direction: directionList})[cube]

    return theCube, directionList    

def _rotateMiddlePieceFromMiddleToTop(theCube, currentCubeIndex):
    rotatedCubeIndex = currentCubeIndex - FMM
    theCube, directionList = _rotateMiddlePieceFromTopToMiddle(theCube, rotatedCubeIndex)

    directions = {LMR: RTM, RMR: LTM, BMR: FTM, FMR: BTM}
    currentCubeIndex = directions.get(currentCubeIndex)
    
    return theCube, currentCubeIndex, directionList

def _alignEdgePieceWithAnotherTopPiece(theCube, currentCubeIndex):
    cube = 'cube'
    direction = 'dir'
    directionList = ''

    while theCube[currentCubeIndex + FML] is not theCube[currentCubeIndex]:
        if currentCubeIndex is not FTM:
            currentCubeIndex = currentCubeIndex - RTL
        else:
            currentCubeIndex = LTM

        directionList += 'U'
        theCube = rotate({cube: theCube, direction: 'U'})[cube]

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
    currentCubeIndex = None
    middleRowPieces = [(theCube[FMR], theCube[RML]), (theCube[RMR], theCube[BML]), (theCube[BMR], theCube[LML]),
                       (theCube[LMR], theCube[FML])]

    centerMiddlePieces = [(theCube[FMM], theCube[RMM]), (theCube[RMM], theCube[BMM]), (theCube[BMM], theCube[LMM]),
                          (theCube[LMM], theCube[FMM])]

    for cubePiece, middlePiece in enumerate(middleRowPieces):
        centerMiddlePiece = centerMiddlePieces[cubePiece]

        if middlePiece != centerMiddlePiece:
            if theCube[UMM] not in middlePiece:
                currentCubeIndex = FMR + cubePiece * RTL
                break

    return currentCubeIndex
