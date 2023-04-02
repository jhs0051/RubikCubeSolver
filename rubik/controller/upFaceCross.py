from rubik.model.constants import *
from rubik.view.rotate import rotate

def solveUpCross(theCube, solution) -> str:
    if _isUpCrossSolved(theCube):
        return theCube, solution

def _isUpCrossSolved(theCube):
    topEdges = [theCube[UMM], theCube[UTM], theCube[UML], theCube[UMR], theCube[UBM]]

    return all(edge == topEdges[FTL] for edge in topEdges)

def _getUpFaceDaisyInCorrectPosition(theCube):
    topEdges = [theCube[UTM], theCube[UML], theCube[UMR], theCube[UBM]]

    if len(set(topEdges)) is FTM:
        return None
    elif topEdges[FTM] is topEdges[FTR]:
        return FTL
    elif topEdges[FTL] is topEdges[FTM]:
        return FTL
    elif topEdges[FTL] is topEdges[FML]:
        return FTM
    elif topEdges[FTM] is topEdges[FML]:
        return FTM
    elif topEdges[FTR] is topEdges[FML]:
        return FTR
    elif topEdges[FTL] is topEdges[FTR]:
        return FML
    else:
        return FTL
    
def _makeUpFaceDaisy(theCube, directionList):
    pass
