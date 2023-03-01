from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.view.rotate import cubeLengthValidation, isCubeValid, validKeys
 
def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    theCube, rotations = parms.get('cube'), ''
    
    if not cubeLengthValidation(theCube):
        result['status'] = 'error: cube can not be empty'
        return result
    if not isCubeValid(theCube, rotations):
        result['status'] = 'error: invalid cube'
        return result
    if not validKeys(parms):
        result['status'] = 'error: invalid key'
        return result
    else:
        _, bottomCrossRotations = solveBottomCross(theCube, rotations)      #iteration 2
        _, bottomLayerRotations = solveBottomLayer(theCube, rotations)      #iteration 3
        futureRotations = solveMiddleLayer(theCube)      #iteration 4
        futureRotations = solveUpCross(theCube)          #iteration 5
        futureRotations = solveUpSurface(theCube)        #iteration 5
        futureRotations = solveUpperLayer(theCube)       #iteration 6
        
        finalSolution = bottomCrossRotations + bottomLayerRotations
    
        result['solution'] = finalSolution
        result['status'] = 'ok'    
        result['integrity'] = ''                    #future
                     
    return result