from rubik.model.constants import *
from rubik.view.rotate import _rotate

def _solveBottomCross(theCube, solution) -> str:
    directionList = ''
    
    if _doesBottomCrossExist(theCube):
        return theCube, solution
    
    theCube, currentCubeIndex, currentRotationList = _makeBottomDaisy(theCube)
    directionList += currentRotationList
    
    if currentCubeIndex is None:
        theCube, currentCubeIndex, currentRotationList = _rotateMiddleLeftCorner(theCube)
        directionList += currentRotationList
        
    if currentCubeIndex is None:
        theCube, currentCubeIndex, directionList = _rotateMiddleTopMiddle(theCube)
        directionList += currentRotationList
    
    theCube, currentCubeIndex, currentRotationList = _rotateTopCornerPieceToBottomCross(theCube, currentCubeIndex)
    directionList += currentRotationList
    
    theCube, currentCubeIndex, currentRotationList = _rotateMiddleTopMiddleFromTopToBottom(theCube, currentCubeIndex)
    directionList += currentRotationList
    
    solution += directionList
    
    return _solveBottomCross(theCube, solution)
        

def _doesBottomCrossExist(cube):
    for currentCubeFace, matchingCubeFace in [(FMM, FBM), (LMM, LBM), (RMM, RBM), (BMM, BBM), (DMM, DTM), (DMM, DML),
                                              (DMM, DMR), (DMM, DBM)]:
        if cube[currentCubeFace] is not cube[matchingCubeFace]:
            return False
    return True

def _makeBottomDaisy(theCube):
    cube = 'cube'
    direction = 'dir'
    directionList = ''
    bottomDaisyListOfTupleCombos = [(DTM, FBM, 'F'), (DBM, BBM, 'B'), (DML, LBM, 'L'), (DMR, RBM, 'R')]
    middleCubeIndexes = [theCube[FMM], theCube[BMM], theCube[LMM], theCube[RMM]]
    currentCubeIndex = None

    for edgePiece, cornerPiece in enumerate(bottomDaisyListOfTupleCombos):
        if theCube[cornerPiece[FTL]] is theCube[DMM]:
            if theCube[cornerPiece[FTM]] != middleCubeIndexes[edgePiece]:
                directionList += {'F': 'FF', 'B': 'BB', 'L': 'LL', 'R': 'RR'}[cornerPiece[FTR]]
                currentCubeIndex = {'F': FTM, 'B': BTM, 'L': LTM, 'R': RTM}[cornerPiece[FTR]]
                theCube = _rotate({cube: theCube, direction: directionList})[cube]
                break
        elif theCube[cornerPiece[FTL]] == middleCubeIndexes[edgePiece] and theCube[cornerPiece[FTM]] == theCube[DMM]:
            directionList += {'F': 'FlUL', 'B': 'BrUR', 'L': 'LbUB', 'R': 'RfUF'}[cornerPiece[FTR]]
            currentCubeIndex = {'F': BTM, 'B': FTM, 'L': RTM, 'R': LTM}[cornerPiece[FTR]]
            theCube = _rotate({cube: theCube, direction: directionList})[cube]
            break

    return theCube, currentCubeIndex, directionList

def _rotateTopCornerPieceToBottomCross(theCube, currentCubeIndex):
    cube = 'cube'
    direction = 'dir'
    directionList = ''

    while theCube[currentCubeIndex] is not theCube[currentCubeIndex + FML]:
        directionList += 'U'
        theCube = _rotate({cube: theCube, direction: 'U'})[cube]
        currentCubeIndex = currentCubeIndex - RTL \
            if currentCubeIndex != FTM \
            else LTM

    return theCube, currentCubeIndex, directionList

def _rotateMiddleTopMiddleFromTopToBottom(theCube, currentCubeIndex):
    cube = 'cube'
    direction = 'dir'
    directionList = ''

    if currentCubeIndex is FTM:
        directionList += 'FF'
        theCube = _rotate({cube: theCube, direction: directionList})[cube]
    elif currentCubeIndex is BTM:
        directionList += 'BB'
        theCube = _rotate({cube: theCube, direction: directionList})[cube]
    elif currentCubeIndex is LTM:
        directionList += 'LL'
        theCube = _rotate({cube: theCube, direction: directionList})[cube]
    elif currentCubeIndex is RTM:
        directionList += 'RR'
        theCube = _rotate({cube: theCube, direction: directionList})[cube]
    
    return theCube, currentCubeIndex, directionList

def _rotateMiddleLeftCorner(theCube):
    cube = 'cube'
    direction = 'dir'
    directionList = ''
    edgePieceCornerPiecePairs = [(FMR, RML, 'f', 'R'), (RMR, BML, 'r', 'B'), (BMR, LML, 'b', 'L'), (LMR, FML, 'l', 'F')]
    currentCubeIndex = None

    for cornerPiece in edgePieceCornerPiecePairs:
        if theCube[cornerPiece[FTM]] is theCube[DMM]:
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
            theCube = _rotate(parms)[cube]
            break
        elif theCube[cornerPiece[FTL]] is theCube[DMM]:
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
            theCube = _rotate(parms)[cube]
            break
        
    return theCube, currentCubeIndex, directionList

def _rotateMiddleTopMiddle(theCube):
    cube = 'cube'
    direction = 'dir'
    directionList = ''
    topCornerPiecePairs = [(FTM, UBM, 'F'), (RTM, UMR, 'R'), (BTM, UTM, 'B'), (LTM, UML, 'L')]
    currentCubeIndex = None

    for cornerPiece in topCornerPiecePairs:
        if theCube[cornerPiece[FTM]] is theCube[DMM]:
            return theCube, cornerPiece[FTL], directionList

        elif theCube[cornerPiece[FTL]] is theCube[DMM]:
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
            theCube = _rotate(parms)[cube]
            break

    return theCube, currentCubeIndex, directionList
