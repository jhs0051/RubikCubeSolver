from rubik.model.constants import *
from rubik.view.rotate import rotate

def solveUpCross(theCube, solution) -> str:
    if _isUpCrossSolved(theCube):
        return theCube, solution

def _isUpCrossSolved(theCube):
    topEdges = [theCube[UMM], theCube[UTM], theCube[UML], theCube[UMR], theCube[UBM]]

    return all(edge == topEdges[FTL] for edge in topEdges)
