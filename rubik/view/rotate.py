from rubik.model.cube import Cube

def _rotate(parms):
    """Return rotated cube""" 
    result = {}
    encodedCube = parms.get('cube')
    
    if not _validKeys(parms):
        result['status'] = 'error: invalid key'
        return result       
    elif not _cubeLengthValidation(encodedCube):
        result['status'] = 'error: cube can not be empty'
        return result
    else:
        theCube = Cube(encodedCube)
        
    
    try:
        directions = parms.get('dir')
    except:
        result['status'] = 'error: could not get direction'
        return result
    
    if not _isCubeValid(encodedCube, directions):
        result['status'] = 'error: invalid cube'
        return result
    else:
        theCube._rotate(directions)
     
    
    result['cube'] = theCube.get()
    result['status'] = 'ok'                     
    return result

def _cubeLengthValidation(encodedCube):
    if encodedCube == None or encodedCube == '':
        return False
    return True

def _validKeys(parms):
    validKeys = 'cube', 'dir', 'op', 'solve'
    keys = parms.keys()
    
    for key in keys:
        if key not in validKeys:
            return False
    return True

def _isCubeValid(encodedCube, directions):
    if Cube._validation(encodedCube, directions) == False:
        return False
    return True
    
    