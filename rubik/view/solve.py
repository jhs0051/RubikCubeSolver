import hashlib
import random
from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.constants import *
from rubik.view.rotate import _cubeLengthValidation, _isCubeValid, _validKeys
 
def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    theCube =  parms.get('cube')
    rotationList = ''
    
    validityResult = _solveValidity(theCube, rotationList, parms)
    if validityResult:
        return validityResult
    else:
        theCube, bottomCrossRotations   = solveBottomCross(theCube, rotationList)      #iteration 2
        theCube, bottomLayerRotations   = solveBottomLayer(theCube, rotationList)      #iteration 3
        theCube, middleLayerRotations   = solveMiddleLayer(theCube, rotationList)      #iteration 4
        theCube, upFaceCrossRotations   = solveUpCross(theCube, rotationList)          #iteration 5
        theCube, upFaceSurfaceRotations = solveUpSurface(theCube, rotationList)        #iteration 5
        futureRotations = solveUpperLayer(theCube)       #iteration 6
        
        finalSolution = bottomCrossRotations + bottomLayerRotations + middleLayerRotations + upFaceCrossRotations + upFaceSurfaceRotations
    
        result['solution'] = finalSolution
        result['status'] = 'ok'    
        result['integrity'] = _getIntegrity(parms.get('cube'), finalSolution)                     #iteration 5
                     
    return result

def _getIntegrity(theCube, solution):
    myAUName = "Jhs0051"
    itemToTokenize = theCube + solution + myAUName
    sha256Hash = hashlib.sha256(itemToTokenize.encode())
    hashToHex = sha256Hash.hexdigest()
    hashStartingPoint = random.randint(startingHash, len(hashToHex) - hashLength)

    return hashToHex[hashStartingPoint:hashStartingPoint + hashLength]

def _solveValidity(theCube, rotationList, parms):
    result = {}

    if not _cubeLengthValidation(theCube):
        result['status'] = 'error: cube can not be empty'
        return result
    elif not _isCubeValid(theCube, rotationList):
        result['status'] = 'error: invalid cube'
        return result
    elif not _validKeys(parms):
        result['status'] = 'error: invalid key'
        return result

    return None
    