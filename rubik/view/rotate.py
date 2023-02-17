from rubik.model.cube import Cube

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    encodedCube = parms.get('cube')
    
    validKeys = 'cube', 'dir', 'op', 'solve'
    keys = parms.keys()
    
    for key in keys:
        if key not in validKeys:
            result['status'] = 'error: extraneous key detected'
            return result
        
   
    if not _cubeLengthValidation(encodedCube):
        result['status'] = 'error: cube can not be empty'
        return result
    else:
        theCube = Cube(encodedCube)
        
    
    try:
        directions = parms.get('dir')
    except:
        result['status'] = 'error: invalid cube'
        return result
    
    if Cube._validation(encodedCube, directions) == False:
        result['status'] = 'error: invalid cube'
        return result
    
    theCube.rotate(directions)
     
    
    result['cube'] = theCube.get()
    result['status'] = 'ok'                     
    return result

def _cubeLengthValidation(encodedCube):
    if encodedCube == None or encodedCube == '':
        return False
    return True
    