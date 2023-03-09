from rubik.model.constants import *
from rubik.model.cube import Cube
from rubik.view.rotate import rotate

def solveBottomCross(theCube: Cube, solution) -> str:
    directionList = ''
    
    if doesBottomCrossExist(theCube):
        return theCube, solution
    
    theCube, currentCubeIndex, currentRotationList = makeBottomDaisy(theCube)
    directionList += currentRotationList
    
    if currentCubeIndex == - FTM:
        theCube, currentCubeIndex, currentRotationList = rotateMiddleLeftCorner(theCube)
        directionList += currentRotationList
        
    if currentCubeIndex == - FTM:
        theCube, currentCubeIndex, directionList = rotateMiddleTopMiddle(theCube)
        directionList += currentRotationList
    
    theCube, currentCubeIndex, currentRotationList = rotateTopCornerPieceToBottomCross(theCube, currentCubeIndex)
    directionList += currentRotationList
    
    theCube, currentCubeIndex, currentRotationList = rotateMiddleTopMiddleFromTopToBottom(theCube, currentCubeIndex)
    directionList += currentRotationList
    
    solution = solution + directionList
    
    return solveBottomCross(theCube, solution)
        

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
    cube = 'cube'
    direction = 'dir'
    directionList = ''
    bottomDaisyListOfTupleCombos = [(DTM, FBM, 'F'), (DBM, BBM, 'B'), (DML, LBM, 'L'), (DMR, RBM, 'R')]
    middleCubeIndexes = [theCube[FMM], theCube[BMM], theCube[LMM], theCube[RMM]]
    currentCubeIndex = - FTM

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

            parms = {cube: theCube, direction: directionList}
            theCube = rotate(parms)[cube]
            break

        elif theCube[cornerPiece[FTL]] == middleCubeIndexes[edgePiece] and theCube[cornerPiece[FTM]] == theCube[DMM]:
            if cornerPiece[FTR] == 'F':
                directionList += 'FlUL'
                currentCubeIndex = BTM
            elif cornerPiece[FTR] == 'B':
                directionList += 'BrUR'
                currentCubeIndex = FTM
            elif cornerPiece[FTR] == 'L':
                directionList += 'LbUB'
                currentCubeIndex = RTM
            elif cornerPiece[FTR] == 'R':
                directionList += 'RfUF'
                currentCubeIndex = LTM

            parms = {cube: theCube, direction: directionList}
            theCube = rotate(parms)[cube]
            break

    return theCube, currentCubeIndex, directionList

def rotateTopCornerPieceToBottomCross(theCube, currentCubeIndex):
    cube = 'cube'
    direction = 'dir'
    directionList = ''

    while theCube[currentCubeIndex] is not theCube[currentCubeIndex + FML]:
        directionList = directionList + 'U'
        theCube = rotate({cube: theCube, direction: 'U'})[cube]
        currentCubeIndex = currentCubeIndex - RTL \
            if currentCubeIndex != FTM \
            else LTM

    return theCube, currentCubeIndex, directionList

def rotateMiddleTopMiddleFromTopToBottom(theCube, currentCubeIndex):
    cube = 'cube'
    direction = 'dir'
    directionList = ''

    if currentCubeIndex == FTM:
        directionList = directionList + 'FF'
        parms = {cube: theCube, direction: directionList}
        theCube = rotate(parms)[cube]
    elif currentCubeIndex == BTM:
        directionList = directionList + 'BB'
        parms = {cube: theCube, direction: directionList}
        theCube = rotate(parms)[cube]
    elif currentCubeIndex == LTM:
        directionList = directionList + 'LL'
        parms = {cube: theCube, direction: directionList}
        theCube = rotate(parms)[cube]
    elif currentCubeIndex == RTM:
        directionList = directionList + 'RR'
        parms = {cube: theCube, direction: directionList}
        theCube = rotate(parms)[cube]
    
    return theCube, currentCubeIndex, directionList

def rotateMiddleLeftCorner(theCube):
    cube = 'cube'
    direction = 'dir'
    directionList = ''
    edgePieceCornerPiecePairs = [(FMR, RML, 'f', 'R'), (RMR, BML, 'r', 'B'), (BMR, LML, 'b', 'L'), (LMR, FML, 'l', 'F')]
    currentCubeIndex = - FTM

    for cornerPiece in edgePieceCornerPiecePairs:
        if theCube[cornerPiece[FTM]] == theCube[DMM]:
            if cornerPiece[FTR] == 'f':
                currentCubeIndex = RTM
            elif cornerPiece[FTR] == 'b':
                currentCubeIndex = LTM
            elif cornerPiece[FTR] == 'l':
                currentCubeIndex = FTM
            elif cornerPiece[FTR] == 'r':
                currentCubeIndex = BTM

            directionList += cornerPiece[FTR] + 'u' + cornerPiece[FTR].upper()
            parms = {cube: theCube, direction: cornerPiece[FTR] + 'u' + cornerPiece[FTR].upper()}
            theCube = rotate(parms)[cube]
            
            break

        elif theCube[cornerPiece[FTL]] == theCube[DMM]:
            if cornerPiece[FML] == 'F':
                currentCubeIndex = LTM
            elif cornerPiece[FML] == 'B':
                currentCubeIndex = RTM
            elif cornerPiece[FML] == 'L':
                currentCubeIndex = BTM
            elif cornerPiece[FML] == 'R':
                currentCubeIndex = FTM

            directionList += cornerPiece[FML] + 'U' + cornerPiece[FML].lower()
            parms = {cube: theCube, direction: cornerPiece[FML] + 'U' + cornerPiece[FML].lower()}
            theCube = rotate(parms)[cube]

            break
        
    return theCube, currentCubeIndex, directionList

def rotateMiddleTopMiddle(theCube):
    cube = 'cube'
    direction = 'dir'
    directionList = ''
    topCornerPiecePairs = [(FTM, UBM, 'F'), (RTM, UMR, 'R'), (BTM, UTM, 'B'), (LTM, UML, 'L')]
    currentCubeIndex = - FTM

    for cornerPiece in topCornerPiecePairs:
        if theCube[cornerPiece[FTM]] == theCube[DMM]:
            return theCube, cornerPiece[FTL], directionList

        elif theCube[cornerPiece[FTL]] == theCube[DMM]:
            if cornerPiece[FTR] == 'F':
                directionList += 'FRurf'
                currentCubeIndex = BTM
            elif cornerPiece[FTR] == 'B':
                directionList += 'BLulb'
                currentCubeIndex = FTM
            elif cornerPiece[FTR] == 'L':
                directionList += 'LFufl'
                currentCubeIndex = RTM
            elif cornerPiece[FTR] == 'R':
                directionList += 'RBubr'
                currentCubeIndex = LTM

            parms = {cube: theCube, direction: directionList}
            theCube = rotate(parms)[cube]

            break

    return theCube, currentCubeIndex, directionList



