from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.view.rotate import _cubeLengthValidation, _isCubeValid, _validKeys
 
def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    theCube =  parms.get('cube')
    rotationList = ''
    
    if not _cubeLengthValidation(theCube):
        result['status'] = 'error: cube can not be empty'
        return result
    if not _isCubeValid(theCube, rotationList):
        result['status'] = 'error: invalid cube'
        return result
    if not _validKeys(parms):
        result['status'] = 'error: invalid key'
        return result
    else:
        theCube, bottomCrossRotations = solveBottomCross(theCube, rotationList)      #iteration 2
        theCube, bottomLayerRotations = solveBottomLayer(theCube, rotationList)      #iteration 3
        theCube, middleLayerRotations = solveMiddleLayer(theCube, rotationList)      #iteration 4
        theCube, upFaceCrossRotations = solveUpCross(theCube, rotationList)          #iteration 5
        futureRotations = solveUpSurface(theCube)        #iteration 5
        futureRotations = solveUpperLayer(theCube)       #iteration 6
        
        finalSolution = bottomCrossRotations + bottomLayerRotations + middleLayerRotations + upFaceCrossRotations
    
        result['solution'] = finalSolution
        result['status'] = 'ok'    
        result['integrity'] = ''                    #future
                     
    return result