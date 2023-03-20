from rubik.controller.bottomCross import _solveBottomCross
from rubik.controller.bottomLayer import _solveBottomLayer
from rubik.controller.middleLayer import _solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.view.rotate import _cubeLengthValidation, _isCubeValid, _validKeys
 
def _solve(parms):
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
        theCube, bottomCrossRotations = _solveBottomCross(theCube, rotationList)      #iteration 2
        theCube, bottomLayerRotations = _solveBottomLayer(theCube, rotationList)      #iteration 3
        theCube, middleLayerRotations = _solveMiddleLayer(theCube, rotationList)      #iteration 4
        futureRotations = solveUpCross(theCube)          #iteration 5
        futureRotations = solveUpSurface(theCube)        #iteration 5
        futureRotations = solveUpperLayer(theCube)       #iteration 6
        
        finalSolution = bottomCrossRotations + bottomLayerRotations + middleLayerRotations
    
        result['solution'] = finalSolution
        result['status'] = 'ok'    
        result['integrity'] = ''                    #future
                     
    return result