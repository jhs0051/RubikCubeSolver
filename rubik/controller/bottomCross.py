from rubik.model.constants import *
from rubik.view.rotate import rotate

def solveBottomCross(theCube, solution) -> str:
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
    
    return solveBottomCross(theCube, solution)
        

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

    for edgePiece, middlePiece in enumerate(bottomDaisyListOfTupleCombos):
        if theCube[middlePiece[FTL]] is theCube[DMM]:
            if theCube[middlePiece[FTM]] is not middleCubeIndexes[edgePiece]:
                directionList += {'F': 'FF', 'B': 'BB', 'L': 'LL', 'R': 'RR'}[middlePiece[FTR]]
                currentCubeIndex = {'F': FTM, 'B': BTM, 'L': LTM, 'R': RTM}[middlePiece[FTR]]
                theCube = rotate({cube: theCube, direction: directionList})[cube]
                break
        elif theCube[middlePiece[FTL]] is middleCubeIndexes[edgePiece] and theCube[middlePiece[FTM]] is theCube[DMM]:
            directionList += {'F': 'FlUL', 'B': 'BrUR', 'L': 'LbUB', 'R': 'RfUF'}[middlePiece[FTR]]
            currentCubeIndex = {'F': BTM, 'B': FTM, 'L': RTM, 'R': LTM}[middlePiece[FTR]]
            theCube = rotate({cube: theCube, direction: directionList})[cube]
            break

    return theCube, currentCubeIndex, directionList

def _centerCubePieceIsNotInCorrectPosition(theCube):
    cube = 'cube'
    direction = 'dir'
    directionList = ''
    bottomDaisyListOfTupleCombos = [(DTM, FBM, 'F'), (DBM, BBM, 'B'), (DML, LBM, 'L'), (DMR, RBM, 'R')]
    currentCubeIndex = None
    centerCube = FBM

    for edgePiece, middlePiece in enumerate(bottomDaisyListOfTupleCombos):
        if theCube[centerCube] is theCube[DMM]:
            if edgePiece is FTM:
                currentCubeIndex = -FTR
                break
            directionList += {'F': 'FlUL', 'B': 'BrUR', 'L': 'LbUB', 'R': 'RfUF'}[middlePiece[FTR]]
            currentCubeIndex = {'F': BTM, 'B': FTM, 'L': RTM, 'R': LTM}[middlePiece[FTR]]
            theCube = rotate({cube: theCube, direction: directionList})[cube]
            break
        centerCube += RTL
        if centerCube > LBR:
            break
    return theCube, currentCubeIndex, directionList

def _rotateTopCornerPieceToBottomCross(theCube, currentCubeIndex):
    cube = 'cube'
    direction = 'dir'
    directionList = ''
    
    if currentCubeIndex is None:
        theCube, currentCubeIndex, directionList = _centerCubePieceIsNotInCorrectPosition(theCube)

    while theCube[currentCubeIndex] is not theCube[currentCubeIndex + FML]:
        directionList += 'U'
        theCube = rotate({cube: theCube, direction: 'U'})[cube]
        currentCubeIndex = currentCubeIndex - RTL \
            if currentCubeIndex is not FTM \
            else LTM

    return theCube, currentCubeIndex, directionList

def _rotateMiddleTopMiddleFromTopToBottom(theCube, currentCubeIndex):
    cube = 'cube'
    direction = 'dir'
    directionList = ''

    directions = {FTM: 'FF', BTM: 'BB', LTM: 'LL', RTM: 'RR'}

    if currentCubeIndex in directions:
        directionList += directions[currentCubeIndex]
        theCube = rotate({cube: theCube, direction: directionList})[cube]
    else:
        directionList += 'LL'
        theCube = rotate({cube: theCube, direction: 'LL'})[cube]
    
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
            theCube = rotate({cube: theCube, direction: cornerPiece[FTR] + 'u' + cornerPiece[FTR].upper()})[cube]
            break

        elif theCube[cornerPiece[FTL]] is theCube[DMM]:
            directions = {'F': LTM, 'B': RTM, 'L': BTM, 'R': FTM}
            currentCubeIndex = directions.get(cornerPiece[FML])

            directionList += cornerPiece[FML] + 'U' + cornerPiece[FML].lower()
            theCube = rotate({cube: theCube, direction: cornerPiece[FML] + 'U' + cornerPiece[FML].lower()})[cube]
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
            directions = {'F': ('FRurf', BTM), 'B': ('BLulb', FTM), 'L': ('LFufl', RTM), 'R': ('RBubr', LTM)}

            if cornerPiece[FTR] in directions:
                rotation, currentCubeIndex = directions[cornerPiece[FTR]]
                directionList += rotation
                theCube = rotate({cube: theCube, direction: directionList})[cube]
                break

    return theCube, currentCubeIndex, directionList
