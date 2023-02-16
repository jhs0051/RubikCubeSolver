import rubik.model.constants
from rubik.model.constants import *
from rubik.model.cube import Cube
from rubik.view.rotate import rotate

def solveBottomCross(theCube: Cube, solution) -> str:
    directionList = ''
    
    if doesBottomCrossExist(theCube):
        return theCube, solution
    
    theCube, currentCubeIndex, currentRotationList = makeBottomDaisy(theCube)
    directionList += currentRotationList
        

def doesBottomCrossExist(cube):
    if cube[FMM] != cube[FBM]:
        return False
    elif cube[LMM] != cube[LBM]:
        return False
    elif cube[RMM] != cube[RBM]:
        return False
    elif cube[BMM] != cube[BBM]:
        return False
    elif cube[DMM] != cube[DTM]:
        return False
    elif cube[DMM] != cube[DML]:
        return False
    elif cube[DMM] != cube[DMR]:
        return False
    elif cube[DMM] != cube[DBM]:
        return False
    return True

def makeBottomDaisy(theCube):
    cube, direction, directionList = 'cube', 'dir', ''
    bottomDaisyListOfTupleCombos = [(DTM, FBM, 'F'), (DBM, BBM, 'B'), (DML, LBM, 'L'), (DMR, RBM, 'R')]
    middleCubeIndexes = [theCube[FMM], theCube[BMM], theCube[LMM], theCube[RMM]]
    currentCubeIndex = -FTM

    for edgePiece, cornerPiece in enumerate(bottomDaisyListOfTupleCombos):
        if theCube[cornerPiece[FTL]] == theCube[DMM] and theCube[cornerPiece[FTM]] != middleCubeIndexes[edgePiece]:
            if cornerPiece[FTR] == 'F':
                directionList += 'FF'
                currentCubeIndex = FTM
            elif cornerPiece[FTR] == 'B':
                directionList += 'BB'
                currentCubeIndex = BTM
            elif cornerPiece[FTR] == 'L':
                directionList += 'LL'
                currentCubeIndex = LTM
            elif cornerPiece[FTR] == 'R':
                directionList += 'RR'
                currentCubeIndex = RTM
            else:
                return False

            parms = {cube: theCube, direction: directionList}
            theCube = rotate(parms)[cube]

    return theCube, currentCubeIndex, directionList


