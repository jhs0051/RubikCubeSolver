from rubik.model.constants import *
from rubik.view.rotate import rotate

def solveUpperLayer(theCube, solution) -> str:
    if _isTopLayerSolved(theCube):
        return theCube, solution
    elif _doTopLayerSidesMatch(theCube):
        solution += 'U'
        theCube = rotate({'cube': theCube, 'dir': 'U'})['cube']
        return solveUpperLayer(theCube, solution)

    theCube, solution = _rotateTopEdge(theCube, solution)
    theCube, solution = _rotateTopRow(theCube, solution)

    return solveUpperLayer(theCube, solution)

def _isTopLayerSolved(theCube):
    upFacePieces = [theCube[UTL], theCube[UTM], theCube[UTR], theCube[UML], theCube[UMM], theCube[UMR], theCube[UBL],
                 theCube[UBM], theCube[UBR]]

    topLayerPieces = [theCube[FTL], theCube[FTM], theCube[FTR], theCube[RTL], theCube[RTM], theCube[RTR], theCube[BTL],
                  theCube[BTM], theCube[BTR], theCube[LTL], theCube[LTM], theCube[LTR]]

    if upFacePieces.count(upFacePieces[FMM]) != len(upFacePieces) \
            or topLayerPieces[FTL:FML].count(theCube[FMM]) != FML \
            or topLayerPieces[FML:FBL].count(theCube[RMM]) != FML \
            or topLayerPieces[FBL:RTL].count(theCube[BMM]) != FML \
            or topLayerPieces[RTL:RML].count(theCube[LMM]) != FML:
        return False
    return True

def _areTopLayerEdgePiecesSolved(theCube):
    if theCube[FTL] != theCube[FTR] or theCube[RTL] != theCube[RTR] or theCube[BTL] != theCube[BTR] \
        or theCube[LTL] != theCube[LTR]:
        return False
    return True

def _alignTopRow(theCube):
    if theCube[LTL] is theCube[LTM] is theCube[LTR]:
        return FTM
    elif theCube[FTL] is theCube[FTM] is theCube[FTR]:
        return FTR
    elif theCube[RTL] is theCube[RTM] is theCube[RTR]:
        return FML
    return FTL

def _doTopLayerSidesMatch(theCube):
    edgePieces = [theCube[FTL], theCube[FTM], theCube[FTR], theCube[RTL], theCube[RTM], theCube[RTR], theCube[BTL],
                  theCube[BTM], theCube[BTR], theCube[LTL], theCube[LTM], theCube[LTR]]

    edgePairings = [edgePieces[FTL:FML], edgePieces[FML:FBL], edgePieces[FBL:RTL], edgePieces[RTL:RML]]

    return all(len(set(edges)) is FTM for edges in edgePairings)

def _alignTopEdgePieces(theCube):
    if theCube[LTL] is theCube[LTR]:
        return FTM
    elif theCube[FTL] is theCube[FTR]:
        return FTR
    elif theCube[RTL] is theCube[RTR]:
        return FML
    return FTL

def _rotateTopEdge(theCube, directionList):
    if _areTopLayerEdgePiecesSolved(theCube):
        return theCube, directionList
    
    currentCubeIndex = _alignTopEdgePieces(theCube)

    directionList += 'U' * currentCubeIndex + 'rFrBBRfrBBRR'
    theCube = rotate({'cube': theCube, 'dir': 'U' * currentCubeIndex + 'rFrBBRfrBBRR'})['cube']

    return _rotateTopEdge(theCube, directionList)

def _rotateTopRow(theCube, directionList):
    if _doTopLayerSidesMatch(theCube):
        return theCube, directionList

    currentCubeIndex = _alignTopRow(theCube)

    directionList += 'U' * currentCubeIndex + 'RuRURURuruRR'
    theCube = rotate({'cube': theCube, 'dir': 'U' * currentCubeIndex + 'RuRURURuruRR'})['cube']

    return _rotateTopRow(theCube, directionList)
