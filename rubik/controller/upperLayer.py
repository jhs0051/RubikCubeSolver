from rubik.model.constants import *
from rubik.view.rotate import rotate
from rubik.model.cube import Cube

def solveUpperLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the entire upper layer is solved.
        
        input:  an instance of the cube class with up-face surface solved
        output: the rotations required to solve the upper layer  
    '''  
    return 'D'      #TODO:  remove this stubbed value

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

def _rotateTopRow(self):
    pass
