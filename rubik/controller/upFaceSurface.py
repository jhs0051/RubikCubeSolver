from rubik.model.constants import *
from rubik.view.rotate import rotate

def solveUpSurface(theCube, solution) -> str:
    if _isUpFaceSolved(theCube):
        return theCube, solution
    elif _doUpFaceEdgePiecesMatch(theCube):
        return theCube, solution
    else:
        theCube, solution = _solveUpFaceEdgePieces(theCube, solution)

    return solveUpSurface(theCube, solution)
    
def _isUpFaceSolved(theCube):
    topPieces = [theCube[UTL], theCube[UTM], theCube[UTR], theCube[UML], theCube[UMM], theCube[UMR],
                 theCube[UBL], theCube[UBM], theCube[UBR]]

    return all(piece == topPieces[FMM] for piece in topPieces)

def _doUpFaceEdgePiecesMatch(theCube):
    topCorners = [theCube[UMM], theCube[UTL], theCube[UTR], theCube[UBL], theCube[UBR]]
    
    return all(corner == topCorners[FTL] for corner in topCorners)

def _solveUpFaceEdgePieces(theCube, directionList):
    topCorners = [theCube[UMM], theCube[UTL], theCube[UTR], theCube[UBL], theCube[UBR]]
    
    if _doUpFaceEdgePiecesMatch(theCube):
        return theCube, directionList
    
    topCornerCount = topCorners.count(topCorners[FTL])

    while True:
        if topCornerCount is FTM:
            if theCube[LTR] is theCube[UMM]:
                break
        elif topCornerCount is FTR:
            if theCube[UBL] is theCube[UMM]:
                break
        elif topCornerCount is FML:
            if theCube[UBR] is theCube[UMM]:
                break
        directionList += 'U'
        theCube = rotate({'cube': theCube, 'dir': 'U'})['cube']

    directionList += 'RUrURUUr'
    theCube = rotate({'cube': theCube, 'dir': 'RUrURUUr'})['cube']

    return _solveUpFaceEdgePieces(theCube, directionList)
