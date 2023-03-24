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

    directions = {FTM: 'FF', BTM: 'BB', LTM: 'LL', RTM: 'RR'}

    if currentCubeIndex in directions:
        directionList += directions[currentCubeIndex]
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
            directions = {'f': RTM, 'b': LTM, 'l': FTM, 'r': BTM}
            currentCubeIndex = directions.get(cornerPiece[FTR])

            directionList += cornerPiece[FTR] + 'u' + cornerPiece[FTR].upper()
            theCube = _rotate({cube: theCube, direction: cornerPiece[FTR] + 'u' + cornerPiece[FTR].upper()})[cube]
            break

        elif theCube[cornerPiece[FTL]] is theCube[DMM]:
            directions = {'F': LTM, 'B': RTM, 'L': BTM, 'R': FTM}
            currentCubeIndex = directions.get(cornerPiece[FML])

            directionList += cornerPiece[FML] + 'U' + cornerPiece[FML].lower()
            theCube = _rotate({cube: theCube, direction: cornerPiece[FML] + 'U' + cornerPiece[FML].lower()})[cube]
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
