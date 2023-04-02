from rubik.model.constants import *
from rubik.view.rotate import rotate

def solveUpSurface(theCube, solution) -> str:
    if _isUpFaceSolved(theCube):
        return theCube, solution
    
def _isUpFaceSolved(theCube):
    topPieces = [theCube[UTL], theCube[UTM], theCube[UTR], theCube[UML], theCube[UMM], theCube[UMR],
                 theCube[UBL], theCube[UBM], theCube[UBR]]

    return all(piece == topPieces[FMM] for piece in topPieces)
